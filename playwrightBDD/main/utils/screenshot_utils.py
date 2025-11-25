from pathlib import Path
from datetime import datetime


def take_screenshot(page, method_name, directory="reports/screenshots"):
    screenshot_dir = Path(directory)
    screenshot_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # Include test name in filename if available
    test_name = getattr(page, "test_name", None)
    if test_name:
        screenshot_path = screenshot_dir / f"{test_name}_{method_name}_{timestamp}.png"
    else:
        screenshot_path = screenshot_dir / f"{method_name}_{timestamp}.png"

    page.screenshot(path=str(screenshot_path))
    print(f"Screenshot saved: {screenshot_path}")

    return screenshot_path
