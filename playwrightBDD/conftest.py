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

def get_feature_steps(item):
    """Extract feature file steps and data tables for BDD tests"""
    try:
        # Get scenario from pytest-bdd
        if hasattr(item, 'obj') and hasattr(item.obj, '__scenario__'):
            scenario = item.obj.__scenario__
            feature = scenario.feature

            # Build feature/scenario info HTML
            feature_html = f'''
            <div style="background-color:#f8f9fa; padding:15px; border-radius:5px; margin:10px 0; border-left:4px solid #0d6efd;">
                <h4 style="margin:0 0 10px 0; color:#0d6efd;">📋 Feature: {feature.name}</h4>
                <p style="margin:5px 0; color:#6c757d; font-style:italic;">{feature.description or ''}</p>
                <h5 style="margin:15px 0 10px 0; color:#198754;">🎯 Scenario: {scenario.name}</h5>
                <ol style="margin:10px 0; padding-left:20px;">
            '''

            # Add steps with data tables
            for step in scenario.steps:
                step_color = {
                    'given': '#6f42c1',
                    'when': '#fd7e14',
                    'then': '#20c997'
                }.get(step.keyword.lower().strip(), '#212529')

                feature_html += f'<li style="margin:5px 0;"><strong style="color:{step_color};">{step.keyword}</strong> {step.name}'

                # Add data table if present
                if hasattr(step, 'datatable') and step.datatable:
                    try:
                        # DataTable has rows attribute, each row has cells, each cell has value
                        if hasattr(step.datatable, 'rows') and step.datatable.rows:
                            feature_html += '''
                            <table style="margin:10px 0 10px 20px; border-collapse:collapse; font-size:0.9em; width:90%; background-color:#fff; box-shadow:0 1px 3px rgba(0,0,0,0.1);">
                                <thead style="background-color:#e9ecef;">
                            '''

                            # Add table headers (first row)
                            header_row = step.datatable.rows[0]
                            feature_html += '<tr>'
                            for cell in header_row.cells:
                                feature_html += f'<th style="border:1px solid #dee2e6; padding:8px; text-align:left; font-weight:600; color:#212529;">{cell.value}</th>'
                            feature_html += '</tr></thead><tbody>'

                            # Add table data rows (remaining rows)
                            for row in step.datatable.rows[1:]:
                                feature_html += '<tr style="background-color:#fff;">'
                                for cell in row.cells:
                                    feature_html += f'<td style="border:1px solid #dee2e6; padding:8px; color:#495057;">{cell.value}</td>'
                                feature_html += '</tr>'

                            feature_html += '</tbody></table>'
                    except Exception as e:
                        # If table extraction fails, just continue without it
                        pass

                feature_html += '</li>'

            feature_html += '</ol></div>'
            return feature_html
    except Exception as e:
        return None
    return None

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
        # Add feature file steps for BDD tests
        feature_steps_html = get_feature_steps(item)
        if feature_steps_html:
            extra.append(pytest_html.extras.html(feature_steps_html))

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

        # Add custom screenshots from contact_page and about_page directories for all tests (both passed and failed)
        test_name = item.name

        # Search in both contact_page and about_page directories
        for screenshot_dir in ["contact_page", "about_page"]:
            custom_screenshots = list(Path(f"reports/screenshots/{screenshot_dir}").glob(f"{test_name}_*.png"))

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