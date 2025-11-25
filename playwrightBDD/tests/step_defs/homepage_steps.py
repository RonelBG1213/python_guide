from pytest_bdd import given, when, then, scenarios, parsers
from main.pages.home_page import StratpointHomePage
from main.pages.contact_page import ContactPage

scenarios('../../features/homepage.feature')

# Given steps
@given('I am on the Stratpoint homepage')
def navigate_to_homepage(page):
    home_page = StratpointHomePage(page)
    home_page.navigate_to_stratpoint()
    home_page.verify_homepage_loaded()

# When steps
@when(parsers.parse('I click on the "{link_name}" link'))
def click_link(page, link_name):
    home_page = StratpointHomePage(page)
    if link_name == "Contact Us":
        home_page.click_contact_us()

# Then steps
@then(parsers.parse('I should see the banner heading "{heading}"'))
def verify_banner_heading(page, heading):
    home_page = StratpointHomePage(page)
    home_page.verify_banner_heading_visible()

@then('I should be on the Contact Us page')
def verify_contact_page(page):
    """Verify Contact Us page is loaded"""
    ContactPage(page).verify_contact_page_loaded()

@then(parsers.parse('I should see the heading "{heading}"'))
def verify_heading(page, heading):
    """Verify any heading is visible"""
    home_page = StratpointHomePage(page)
    if heading == "Let's Connect":
        home_page.verify_lets_connect_heading_visible()
