from playwright.sync_api import Page, expect
from main.pages.navigation import Navigation
from main.locators.about_page_locators import AboutPageLocators
from main.utils.screenshot_utils import take_screenshot


class AboutPage:
    def __init__(self, page):
        self.page = page
        self.locators = AboutPageLocators(page)
        self.navigation = Navigation(page)

    def verify_about_page_loaded(self):
        expect(self.page).to_have_url("https://stratpoint.com/about-us/")
        take_screenshot(self.page, "verify_about_page_loaded", "reports/screenshots/about_page")

    def verify_about_heading_visible(self):
        expect(self.locators.about_heading).to_be_visible()
        take_screenshot(self.page, "verify_about_heading_visible", "reports/screenshots/about_page")

    def verify_company_description_visible(self):
        expect(self.locators.company_description).to_be_visible()
        take_screenshot(self.page, "verify_company_description_visible", "reports/screenshots/about_page")

    def verify_navigation_menu_visible(self):
        expect(self.locators.navigation_menu).to_be_visible()
        take_screenshot(self.page, "verify_navigation_menu_visible", "reports/screenshots/about_page")

    def verify_footer_visible(self):
        expect(self.locators.footer).to_be_visible()
        take_screenshot(self.page, "verify_footer_visible", "reports/screenshots/about_page")
