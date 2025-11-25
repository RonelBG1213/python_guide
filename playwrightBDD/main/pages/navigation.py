from playwright.sync_api import Page

class Navigation:
    """Handles all navigation-related methods"""

    def __init__(self, page: Page):
        self.page = page

    def navigate_to(self, url: str):
        self.page.goto(url)

    def navigate_to_stratpoint_home(self):
        self.navigate_to("https://stratpoint.com/")

    def navigate_to_contact_us(self):
        self.navigate_to("https://stratpoint.com/contact-us/")

    def go_back(self):
        self.page.go_back()

    def go_forward(self):
        self.page.go_forward()

    def reload_page(self):
        self.page.reload()

    def get_current_url(self):
        return self.page.url
