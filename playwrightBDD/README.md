# Playwright BDD Framework

A Behavior-Driven Development (BDD) framework using pytest-bdd and Playwright for testing the Stratpoint website.

## Project Structure

```
playwrightBDD/
├── features/           # Gherkin feature files (human-readable tests)
│   ├── homepage.feature
│   └── contact_us.feature
├── locators/           # Page element locators (centralized selectors)
│   ├── __init__.py
│   ├── home_page_locators.py
│   └── contact_page_locators.py
├── pages/              # Page Object Models (page interactions)
│   ├── home_page.py
│   ├── contact_page.py
│   └── navigation.py
├── tests/
│   └── step_defs/      # Step definitions (glue code)
│       ├── homepage_steps.py
│       └── contact_us_steps.py
├── conftest.py         # Pytest fixtures (browser & page setup)
├── pytest.ini          # Pytest configuration
├── requirements.txt    # Project dependencies
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

**Required packages:**
- `playwright==1.48.0` - Browser automation
- `pytest==8.3.3` - Testing framework
- `pytest-bdd==7.0.1` - BDD support for pytest
- `pytest-html==4.1.1` - HTML test reports
- `pytest-xdist==3.6.1` - Parallel test execution

### 2. Install Playwright Browsers

```bash
playwright install chromium
```

Or install all browsers:
```bash
playwright install
```

## Running the BDD Framework

### Basic Test Execution

```bash
# Run all BDD scenarios
pytest

# Run with verbose output (recommended)
pytest -v

# Run with detailed output
pytest -vv
```

### Run Specific Features

```bash
# Run only homepage scenarios
pytest tests/step_defs/homepage_steps.py

# Run only contact form scenarios
pytest tests/step_defs/contact_us_steps.py
```

### Filter by Scenario Name

```bash
# Run scenarios matching keyword
pytest -k "homepage"
pytest -k "contact"
pytest -k "Privacy Notice"
```

### Generate HTML Report

```bash
# Run tests and generate HTML report
pytest --html=reports/report.html --self-contained-html
```

### Parallel Execution

```bash
# Run tests in parallel with 4 workers
pytest -n 4

# Auto-detect CPU cores and run parallel
pytest -n auto
```

### Headless vs Headed Mode

By default, tests run in **headed mode** (browser visible).

To run in **headless mode**, edit `conftest.py`:
```python
browser = playwright.chromium.launch(headless=True)  # Change to True
```

## Common pytest Commands

```bash
# Show test collection without running
pytest --collect-only

# Stop on first failure
pytest -x

# Show local variables on failure
pytest -l

# Run last failed tests only
pytest --lf

# Show print statements
pytest -s

# Increase verbosity
pytest -vv
```

## Understanding BDD Framework

### What is BDD?

**Behavior-Driven Development (BDD)** is a software development approach where:
- Tests are written in **plain English** using Gherkin syntax
- **Non-technical stakeholders** can read and understand test scenarios
- Features describe **user behavior** and business requirements
- Promotes **collaboration** between developers, QA, and business teams

### BDD Framework Architecture

```
Feature File (Gherkin)  →  Step Definitions (Python)  →  Page Objects  →  Browser
     ↓                            ↓                           ↓              ↓
"Given I am on..."        navigate_to_homepage()      HomePage class    Playwright
```

### Key Components

| Component | Purpose | Example |
|-----------|---------|---------|
| **Feature Files** | Human-readable test scenarios | `homepage.feature` |
| **Step Definitions** | Python code linking Gherkin to actions | `homepage_steps.py` |
| **Page Objects** | Page interaction logic | `home_page.py` |
| **Locators** | Element selectors | `home_page_locators.py` |
| **Fixtures** | Test setup/teardown | `conftest.py` |

### Gherkin Syntax

Feature files use **Given-When-Then** format:

```gherkin
Feature: Brief description of feature being tested

  Scenario: Specific test case description
    Given [precondition - setup state]
    When [action - user performs something]
    Then [assertion - expected outcome]
    And [additional step of same type]
```

**Example:**
```gherkin
Feature: Contact Us Form
  Scenario: Submit contact form
    Given I am on the Contact Us page
    When I fill in the contact form with valid data
    And I click the Send button
    Then I should see a success message
```

## Framework Features

### Current Test Scenarios

**Homepage Feature** (`features/homepage.feature`):
- ✅ Verify homepage banner heading
- ✅ Navigate to Contact Us page
- ✅ Click Let's Connect link

**Contact Us Feature** (`features/contact_us.feature`):
- ✅ Navigate to Contact Us page directly
- ✅ Verify all form fields are visible
- ✅ Fill out complete contact form
- ✅ Open Privacy Notice in new tab

### Step Definitions Structure

**Step definitions act as "glue code"** between Gherkin and implementation:

```python
from pytest_bdd import given, when, then, scenarios

# Load all feature files from directory
scenarios('../../features/')

@given('I am on the Stratpoint homepage')
def navigate_to_homepage(page):
    home_page = StratpointHomePage(page)
    home_page.navigate_to_stratpoint()
    home_page.verify_homepage_loaded()
```

**Key Points:**
- `scenarios('../../features/')` loads all `.feature` files automatically
- Decorators (`@given`, `@when`, `@then`) match Gherkin step text
- Step functions delegate to page objects for actual implementation
- All assertions handled in page object methods

## BDD vs Traditional Testing

### Traditional Test (POM)
```python
def test_homepage_banner_heading(page):
    home_page = StratpointHomePage(page)
    home_page.navigate_to_stratpoint()
    home_page.verify_homepage_loaded()
    home_page.verify_banner_heading_visible()
```

### BDD Test (pytest-bdd)
```gherkin
Scenario: Verify homepage banner heading is visible
  Given I am on the Stratpoint homepage
  Then I should see the banner heading "Fast forward to the future"
```

### BDD Advantages

| Benefit | Description |
|---------|-------------|
| **Readability** | Non-technical stakeholders can understand tests |
| **Living Documentation** | Feature files document system behavior |
| **Collaboration** | Business, QA, and Dev speak same language |
| **Reusability** | Step definitions shared across features |
| **User-Focused** | Tests written from user's perspective |
| **Maintainability** | Changes in one place affect all scenarios |

## Debugging Tests

### Using Playwright Inspector

**Windows PowerShell:**
```powershell
$env:PWDEBUG=1; pytest
```

**macOS/Linux:**
```bash
PWDEBUG=1 pytest
```

### Show Print Statements

```bash
pytest -s
```

### Run with Detailed Traceback

```bash
pytest -vv --tb=long
```

### Stop on First Failure

```bash
pytest -x
```

## Writing New Scenarios

### Step 1: Create Feature File

`features/login.feature`:
```gherkin
Feature: User Login
  As a registered user
  I want to log in to the system
  So that I can access my account

  Scenario: Successful login
    Given I am on the login page
    When I enter valid credentials
    And I click the Login button
    Then I should be logged in
    And I should see my dashboard
```

### Step 2: Create Step Definitions

`tests/step_defs/login_steps.py`:
```python
from pytest_bdd import given, when, then, scenarios
from pages.login_page import LoginPage

scenarios('../../features/')

@given('I am on the login page')
def navigate_to_login(page):
    login_page = LoginPage(page)
    login_page.navigate_to_login()

@when('I enter valid credentials')
def enter_credentials(page):
    login_page = LoginPage(page)
    login_page.enter_username("user@example.com")
    login_page.enter_password("Password123")

@then('I should be logged in')
def verify_logged_in(page):
    login_page = LoginPage(page)
    login_page.verify_login_successful()
```

### Step 3: Run New Tests

```bash
pytest tests/step_defs/login_steps.py -v
```

## Best Practices

### Feature File Guidelines

✅ **DO:**
- Write from user's perspective
- Use business language, not technical terms
- Keep scenarios independent
- Use descriptive scenario names
- Include Feature description with user story format

❌ **DON'T:**
- Include implementation details
- Create dependencies between scenarios
- Use technical jargon
- Make scenarios too long (max 10 steps)

### Step Definition Guidelines

✅ **DO:**
- Keep step functions simple and focused
- Delegate logic to page objects
- Reuse steps across multiple features
- Use descriptive function names
- Handle all assertions in page objects

❌ **DON'T:**
- Put business logic in step definitions
- Use `expect()` or `assert` in step functions
- Create duplicate steps
- Make steps too specific to one scenario

### Example: Good vs Bad

**❌ Bad (too technical):**
```gherkin
When I click the element with id "submit-btn"
Then the URL should contain "/success"
```

**✅ Good (user-focused):**
```gherkin
When I submit the contact form
Then I should see a success message
```

## Troubleshooting

### Issue: Step not found

```
StepDefinitionNotFoundError: Step is not defined
```

**Solution:** Ensure step text in `.feature` file **exactly matches** decorator text:
```python
@given('I am on the homepage')  # Must match feature file exactly
```

### Issue: Multiple step definitions

```
StepDefinitionAlreadyUsed: Step is already defined
```

**Solution:** Each step can only be defined once. Check for duplicate `@given/@when/@then` decorators with same text.

### Issue: Feature file not found

```
FeatureFileNotFound
```

**Solution:** Verify path in `scenarios()` call is correct relative to step definition file.

## CI/CD Integration

### GitHub Actions Example

`.github/workflows/bdd-tests.yml`:
```yaml
name: BDD Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          playwright install chromium

      - name: Run BDD tests
        run: pytest -v --html=report.html --self-contained-html

      - name: Upload report
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: test-report
          path: report.html
```

## Additional Resources

- **pytest-bdd Documentation:** https://pytest-bdd.readthedocs.io/
- **Playwright Python:** https://playwright.dev/python/
- **Gherkin Reference:** https://cucumber.io/docs/gherkin/reference/
- **BDD Best Practices:** https://cucumber.io/docs/bdd/

## License

This framework is for educational purposes.
