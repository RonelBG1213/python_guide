# Playwright POM Framework

A Page Object Model (POM) framework for Playwright Python tests with support for debugging and tracing.

## Project Structure

```
playwrightPOM/
├── locators/           # Page element locators
│   ├── home_page_locators.py
│   └── contact_page_locators.py
├── pages/              # Page Object Models
│   ├── home_page.py
│   ├── contact_page.py
│   └── navigation.py
├── tests/              # Test files
│   ├── test_homepage.py
│   └── test_contact_us.py
├── conftest.py         # Pytest fixtures
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Project dependencies
└── README.md
```

## Setup

### 1. Install Dependencies

```bash
# Install all dependencies from requirements.txt
pip install -r requirements.txt
```

**Or install manually:**
```bash
pip install playwright pytest pytest-html pytest-xdist
```

### 2. Install Browsers

```bash
playwright install
```

## Running Tests

### Basic Test Execution

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_homepage.py

# Run with verbose output
pytest -v

# Run specific test
pytest tests/test_homepage.py::test_homepage_banner_heading
```

### Parallel Execution

```bash
# Install pytest-xdist
pip install pytest-xdist

# Run tests in parallel (4 workers)
pytest -n 4
```

## Debugging & Tracing

### Method 1: Playwright Inspector (Debugger)

The Playwright Inspector allows you to step through your tests, inspect elements, and debug issues interactively.

#### Step-by-Step Guide:

**Option A: Using PWDEBUG Environment Variable**

1. **Windows (PowerShell):**
   ```powershell
   $env:PWDEBUG=1; pytest tests/test_homepage.py
   ```

2. **Windows (Command Prompt):**
   ```cmd
   set PWDEBUG=1 && pytest tests/test_homepage.py
   ```

3. **macOS/Linux:**
   ```bash
   PWDEBUG=1 pytest tests/test_homepage.py
   ```

**Option B: Using page.pause() in Code**

1. Add `page.pause()` in your test where you want to debug:
   ```python
   def test_homepage_banner_heading(page: Page):
       home_page = StratpointHomePage(page)
       home_page.navigate_to_stratpoint()
       page.pause()  # Debugger will open here
       home_page.verify_homepage_loaded()
   ```

2. Run the test normally:
   ```bash
   pytest tests/test_homepage.py::test_homepage_banner_heading
   ```

**Using the Inspector:**
- **Step Over**: Execute one action at a time
- **Resume**: Continue test execution
- **Inspect**: Click element picker to inspect page elements
- **Record**: Generate new test code
- **Console**: View browser console output

### Method 2: Trace Viewer

Trace Viewer provides a detailed timeline of your test execution with screenshots, network activity, and DOM snapshots.

#### Step-by-Step Guide:

**1. Enable Tracing in conftest.py**

Update your `conftest.py`:

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()

    # Start tracing
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    yield page

    # Stop tracing and save
    context.tracing.stop(path="trace.zip")
    page.close()
    context.close()
```

**2. Run Your Tests**

```bash
pytest tests/test_homepage.py
```

This will generate a `trace.zip` file.

**3. View the Trace**

```bash
playwright show-trace trace.zip
```

**Trace Viewer Features:**
- **Timeline**: See all actions in chronological order
- **Screenshots**: Visual state at each step
- **Network**: All network requests and responses
- **Console**: Browser console logs
- **Source**: Source code of each action
- **Snapshots**: DOM state at each step

### Method 3: Headed Mode (Visual Debugging)

Run tests with browser visible (already configured in conftest.py):

```bash
pytest tests/test_homepage.py
```

To run in headless mode, update `conftest.py`:
```python
browser = playwright.chromium.launch(headless=True)
```

### Method 4: Screenshots on Failure

Add to `conftest.py`:

```python
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            page.screenshot(path=f"screenshots/failure_{item.name}.png")
```

### Method 5: Video Recording

Enable video recording in `conftest.py`:

```python
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()
    yield page
    page.close()
    context.close()
```

## Debugging Tips

### Common Issues

**1. Element not found:**
```bash
# Use Inspector to verify selectors
PWDEBUG=1 pytest tests/test_homepage.py
```

**2. Timing issues:**
```python
# Add explicit waits
page.wait_for_selector("button[type='submit']")
```

**3. Network issues:**
```bash
# Use trace viewer to inspect network
playwright show-trace trace.zip
```

### Best Practices

1. **Use headed mode during development** - See what's happening
2. **Use trace viewer for CI failures** - Analyze failed tests in detail
3. **Add page.pause() for specific debugging** - Stop at exact point
4. **Enable video for flaky tests** - Capture intermittent issues
5. **Use screenshots on failure** - Quick visual debugging

## Generate HTML Reports

```bash
# Install pytest-html
pip install pytest-html

# Run tests with report
pytest --html=report.html

# Run with self-contained report
pytest --html=report.html --self-contained-html
```

## CI/CD Integration

For headless execution in CI:

```python
# conftest.py
import os

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as playwright:
        headless = os.getenv("CI", "false") == "true"
        browser = playwright.chromium.launch(headless=headless)
        yield browser
        browser.close()
```

Run in CI:
```bash
CI=true pytest
```

## Page Object Model Benefits

- **Separation of concerns**: Test logic separated from page interactions
- **Reusability**: Page objects used across multiple tests
- **Maintainability**: UI changes only require updates to page objects
- **Readability**: Tests are clean and easy to understand
- **Scalability**: Easy to add new pages and tests

## Support

For issues or questions:
1. Check Playwright documentation: https://playwright.dev/python/
2. Review test execution output
3. Use debugging tools described above
4. Check browser console in Inspector