from pytest_bdd import given, when, then, scenario
from main.pages.home_page import StratpointHomePage
from main.pages.about_page import AboutPage
from main.pages.navigation import Navigation

# Scenario definitions using scenario decorator
@scenario('../../features/about_page.feature', 'Navigate to About page from homepage')
def test_navigate_to_about_page():
    """Test navigating to About page from homepage"""
    pass


@scenario('../../features/about_page.feature', 'Verify About page content is visible')
def test_verify_about_page_content():
    """Test About page content visibility"""
    pass


@scenario('../../features/about_page.feature', 'Verify About page navigation links')
def test_verify_about_page_navigation():
    """Test About page navigation elements"""
    pass


@scenario('../../features/about_page.feature', 'Verify About page elements are present')
def test_verify_about_page_elements_table():
    """Test About page elements using data table"""
    pass


# Given steps
@given('I am on the Stratpoint homepage')
def navigate_to_homepage(page):
    home_page = StratpointHomePage(page)
    home_page.navigate_to_stratpoint()
    home_page.verify_homepage_loaded()


@given('I am on the About page')
def navigate_to_about_page_directly(page):
    navigation = Navigation(page)
    page.goto("https://stratpoint.com/about-us/")
    about_page = AboutPage(page)
    about_page.verify_about_page_loaded()


# When steps
@when('I click on the "About" link')
def click_about_link(page):
    home_page = StratpointHomePage(page)
    home_page.click_about()


# Then steps
@then('I should be on the About page')
def verify_on_about_page(page):
    about_page = AboutPage(page)
    about_page.verify_about_page_loaded()


@then('I should see the About page heading')
def verify_about_heading(page):
    about_page = AboutPage(page)
    about_page.verify_about_heading_visible()


@then('I should see the company description section')
def verify_company_description(page):
    about_page = AboutPage(page)
    about_page.verify_company_description_visible()


@then('the navigation menu should be visible')
def verify_navigation_menu(page):
    about_page = AboutPage(page)
    about_page.verify_navigation_menu_visible()


@then('the footer should be visible')
def verify_footer(page):
    about_page = AboutPage(page)
    about_page.verify_footer_visible()


@then('I should see the following page elements:')
def verify_page_elements_from_table(page, datatable):
    about_page = AboutPage(page)

    # Iterate through data table rows (skip header)
    for row in datatable[1:]:
        element = row[0]
        expected_state = row[1]

        # Verify each element based on the table
        if element == "About Heading":
            about_page.verify_about_heading_visible()
        elif element == "Description":
            about_page.verify_company_description_visible()
        elif element == "Navigation Menu":
            about_page.verify_navigation_menu_visible()
        elif element == "Footer":
            about_page.verify_footer_visible()
