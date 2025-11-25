from playwright.sync_api import Page, expect
from pages.navigation import Navigation
from locators.home_page_locators import HomePageLocators

class StratpointHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = HomePageLocators(page)
        self.navigation = Navigation(page)
        self.contact_us_link = page.get_by_role("link", name="Contact Us")

    def navigate_to_stratpoint(self):
        self.navigation.navigate_to_stratpoint_home()

    def click_contact_us(self):
        self.contact_us_link.click()

    def click_lets_connect(self):
        self.locators.lets_connect_link.click()

    def verify_homepage_loaded(self):
        expect(self.page).to_have_url("https://stratpoint.com/")

    def verify_banner_heading_visible(self):
        expect(self.locators.home_banner_heading).to_be_visible()
