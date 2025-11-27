from playwright.sync_api import Page, expect
from main.pages.navigation import Navigation
from main.locators.home_page_locators import HomePageLocators

class StratpointHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = HomePageLocators(page)
        self.navigation = Navigation(page)
        self.contact_us_link = page.get_by_role("link", name="Contact Us")
        self.about_link = page.get_by_role("link", name="About 3")

    def navigate_to_stratpoint(self):
        self.navigation.navigate_to_stratpoint_home()

    def click_contact_us(self):
        self.contact_us_link.click()

    def click_about(self):
        self.about_link.click()

    def verify_lets_connect_heading_visible(self):
        """Verify Let's Connect heading is visible"""
        expect(self.locators.lets_connect_heading).to_be_visible()

    def verify_homepage_loaded(self):
        expect(self.page).to_have_url("https://stratpoint.com/")

    def verify_banner_heading_visible(self):
        expect(self.locators.home_banner_heading).to_be_visible()
