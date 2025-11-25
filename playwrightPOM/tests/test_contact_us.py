from playwright.sync_api import expect
from pages.home_page import StratpointHomePage
from pages.contact_page import ContactPage
from pages.navigation import Navigation

def test_navigate_to_contact_us(page):
    home_page = StratpointHomePage(page)
    contact_page = ContactPage(page)

    home_page.navigate_to_stratpoint()
    home_page.verify_homepage_loaded()
    home_page.click_contact_us()
    contact_page.verify_contact_page_loaded()

def test_fill_contact_form(page):
    navigation = Navigation(page)
    contact_page = ContactPage(page)

    navigation.navigate_to_contact_us()
    contact_page.fill_contact_form(
        name="John Doe",
        email="john.doe@example.com",
        contact_number="+1234567890",
        company="Test Company",
        job_title="QA Engineer",
        type_of_inquiry="Testing",
        subject="Test Inquiry",
        message="This is a test message"
    )

def test_privacy_notice_link(page):
    navigation = Navigation(page)
    contact_page = ContactPage(page)

    navigation.navigate_to_contact_us()
    contact_page.verify_contact_page_loaded()

    privacy_page = contact_page.open_privacy_notice_in_new_tab()
    expect(privacy_page).to_have_url("https://stratpoint.com/privacy-notice/")
    privacy_page.close()

def test_contact_form_fields_visible(page):
    navigation = Navigation(page)
    contact_page = ContactPage(page)

    navigation.navigate_to_contact_us()
    contact_page.verify_contact_page_loaded()

    expect(contact_page.locators.name_input).to_be_visible()
    expect(contact_page.locators.email_input).to_be_visible()
    expect(contact_page.locators.contact_number).to_be_visible()
    expect(contact_page.locators.company_input).to_be_visible()
    expect(contact_page.locators.job_title_input).to_be_visible()
    expect(contact_page.locators.subject_input).to_be_visible()
    expect(contact_page.locators.message_textarea).to_be_visible()
    expect(contact_page.locators.send_button).to_be_visible()

