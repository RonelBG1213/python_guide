class AboutPageLocators:
    def __init__(self, page):
        self.about_heading = page.locator("h1, h2").first
        self.company_description = page.locator("div.et_pb_text_inner").first
        self.navigation_menu = page.locator("#top-menu-nav")
        self.footer = page.locator("footer")
