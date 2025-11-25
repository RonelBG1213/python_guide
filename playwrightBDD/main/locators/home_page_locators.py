class HomePageLocators:
     def __init__(self, page):
        self.home_banner_heading = page.get_by_role("heading", name="Fast forward to the future")
        self.lets_connect_heading = page.get_by_role("heading", name="Let's Connect")
