import pytest
import pytest_html
from playwright.sync_api import sync_playwright
from pathlib import Path
from datetime import datetime
import base64

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser, request):
    # Create directories for screenshots and traces
    screenshot_dir = Path("reports/screenshots/failures")
    trace_dir = Path("reports/traces")
    screenshot_dir.mkdir(parents=True, exist_ok=True)
    trace_dir.mkdir(parents=True, exist_ok=True)

    # Create context with tracing enabled
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    # Store test name on page object for screenshot utility
    page.test_name = request.node.name
    yield page

    # Check if test failed
    if request.node.rep_call.failed:
        # Generate timestamp and test name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name

        # Take screenshot on failure
        screenshot_path = screenshot_dir / f"{test_name}_{timestamp}.png"
        page.screenshot(path=str(screenshot_path))
        print(f"\n❌ Test failed - Screenshot saved: {screenshot_path}")

        # Save trace on failure
        trace_path = trace_dir / f"{test_name}_{timestamp}.zip"
        context.tracing.stop(path=str(trace_path))
        print(f"📊 Trace saved: {trace_path}")
    else:
        # Stop tracing without saving if test passed
        context.tracing.stop()

    page.close()
    context.close()

@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook to capture test results and attach screenshots to HTML report"""
    outcome = yield
    report = outcome.get_result()

    # Set report attribute for fixture access
    setattr(item, f"rep_{report.when}", report)

    # Attach screenshots to HTML report
    extra = getattr(report, "extras", [])

    if report.when == "call":
        # Add failure screenshot if test failed
        if report.failed:
            screenshot_files = list(Path("reports/screenshots/failures").glob(f"{item.name}_*.png"))

            if screenshot_files:
                # Get the most recent screenshot
                latest_screenshot = max(screenshot_files, key=lambda p: p.stat().st_mtime)

                with open(latest_screenshot, "rb") as f:
                    screenshot_bytes = f.read()
                    screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')
                    html_img = f'<div style="margin-top:10px;"><strong style="color:#dc3545;">❌ Failure Screenshot:</strong><br/><img src="data:image/png;base64,{screenshot_base64}" style="width:600px; border:2px solid #dc3545; margin-top:5px;"/></div>'
                    extra.append(pytest_html.extras.html(html_img))

        # Add custom screenshots from contact_page directory for all tests (both passed and failed)
        test_name = item.name
        custom_screenshots = list(Path("reports/screenshots/contact_page").glob(f"{test_name}_*.png"))

        if custom_screenshots:
            # Sort by modification time to show in chronological order
            custom_screenshots.sort(key=lambda p: p.stat().st_mtime)

            for screenshot_path in custom_screenshots:
                with open(screenshot_path, "rb") as f:
                    screenshot_bytes = f.read()
                    # Convert bytes to base64 string for pytest-html
                    screenshot_base64 = base64.b64encode(screenshot_bytes).decode('utf-8')
                    # Extract method name from filename (remove test_name prefix and timestamp)
                    screenshot_name = screenshot_path.stem.replace(f"{test_name}_", "")
                    # Remove timestamp from the end
                    screenshot_name = "_".join(screenshot_name.split("_")[:-2]) if "_" in screenshot_name else screenshot_name
                    # Add each screenshot as a separate extra using png method
                    extra.append(pytest_html.extras.png(screenshot_base64, name=screenshot_name))

        report.extras = extra