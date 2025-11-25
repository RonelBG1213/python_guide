from pages.home_page import StratpointHomePage
from pages.navigation import Navigation

def test_homepage_banner_heading(page):
    home_page = StratpointHomePage(page)
    home_page.navigate_to_stratpoint()
    home_page.verify_homepage_loaded()
    home_page.verify_banner_heading_visible()

def test_homepage_reload(page):
    home_page = StratpointHomePage(page)
    navigation = Navigation(page)

    home_page.navigate_to_stratpoint()
    home_page.verify_homepage_loaded()
    navigation.reload_page()
    home_page.verify_homepage_loaded()

