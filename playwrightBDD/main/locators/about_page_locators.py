class AboutPageLocators:
    def __init__(self, page):
        self.page = page

    # About page elements
    @property
    def about_heading(self):
        return self.page.locator("h1, h2").first

    @property
    def company_description(self):
        return self.page.locator("div.et_pb_text_inner").first

    @property
    def navigation_menu(self):
        return self.page.locator("#top-menu-nav")

    @property
    def footer(self):
        return self.page.locator("footer")
