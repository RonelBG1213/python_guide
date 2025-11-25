from playwright.sync_api import Page, expect
from main.pages.navigation import Navigation
from main.locators.contact_page_locators import ContactPageLocators
from main.utils.screenshot_utils import take_screenshot

class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = ContactPageLocators(page)
        self.navigation = Navigation(page)

    def verify_contact_page_loaded(self):
        """Verify we're on the contact page"""
        expect(self.page).to_have_url("https://stratpoint.com/contact-us/")
        take_screenshot(self.page, "verify_contact_page_loaded", "reports/screenshots/contact_page")

    def verify_name_field_visible(self):
        """Verify name input field is visible"""
        expect(self.locators.name_input).to_be_visible()
        take_screenshot(self.page, "verify_name_field_visible", "reports/screenshots/contact_page")

    def verify_email_field_visible(self):
        """Verify email input field is visible"""
        expect(self.locators.email_input).to_be_visible()
        take_screenshot(self.page, "verify_email_field_visible", "reports/screenshots/contact_page")

    def verify_contact_number_field_visible(self):
        """Verify contact number field is visible"""
        expect(self.locators.contact_number).to_be_visible()
        take_screenshot(self.page, "verify_contact_number_field_visible", "reports/screenshots/contact_page")

    def verify_company_field_visible(self):
        """Verify company input field is visible"""
        expect(self.locators.company_input).to_be_visible()
        take_screenshot(self.page, "verify_company_field_visible", "reports/screenshots/contact_page")

    def verify_job_title_field_visible(self):
        """Verify job title field is visible"""
        expect(self.locators.job_title_input).to_be_visible()
        take_screenshot(self.page, "verify_job_title_field_visible", "reports/screenshots/contact_page")

    def verify_subject_field_visible(self):
        """Verify subject field is visible"""
        expect(self.locators.subject_input).to_be_visible()
        take_screenshot(self.page, "verify_subject_field_visible", "reports/screenshots/contact_page")

    def verify_message_field_visible(self):
        """Verify message textarea is visible"""
        expect(self.locators.message_textarea).to_be_visible()
        take_screenshot(self.page, "verify_message_field_visible", "reports/screenshots/contact_page")

    def verify_send_button_visible(self):
        """Verify send button is visible"""
        expect(self.locators.send_button).to_be_visible()
        take_screenshot(self.page, "verify_send_button_visible", "reports/screenshots/contact_page")

    def fill_contact_form(self, name, email, contact_number, company, job_title, type_of_inquiry, subject, message):
        self.locators.name_input.fill(name)
        self.locators.email_input.fill(email)
        self.locators.contact_number.fill(contact_number)
        self.locators.company_input.fill(company)
        self.locators.job_title_input.fill(job_title)
        self.locators.type_of_inquiry_dropdown.select_option(type_of_inquiry)
        self.locators.subject_input.fill(subject)
        self.locators.message_textarea.fill(message)
        take_screenshot(self.page, "fill_contact_form", "reports/screenshots/contact_page")

    def submit_form(self):
        """Submit the contact form"""
        self.locators.send_button.click()
        take_screenshot(self.page, "submit_form", "reports/screenshots/contact_page")

    def verify_form_submitted(self):
        """Verify submission success"""
        expect(self.locators.success_message).to_be_visible()
        take_screenshot(self.page, "verify_form_submitted", "reports/screenshots/contact_page")

    def open_privacy_notice_in_new_tab(self):
        # Use .first to handle multiple Privacy Notice links
        privacy_notice_href = self.locators.privacy_notice_link.first.get_attribute("href")

        with self.page.context.expect_page() as new_page_info:
            self.page.evaluate(f"window.open('{privacy_notice_href}', '_blank')")

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        take_screenshot(self.page, "open_privacy_notice_in_new_tab", "reports/screenshots/contact_page")
        return new_page

    def verify_privacy_notice_opened(self, privacy_page):
        """Verify privacy notice page is opened"""
        assert privacy_page is not None, "Privacy notice tab was not opened"
        take_screenshot(self.page, "verify_privacy_notice_opened", "reports/screenshots/contact_page")

    def verify_privacy_notice_url(self, privacy_page, expected_url):
        """Verify privacy notice URL and close tab"""
        expect(privacy_page).to_have_url(expected_url)
        take_screenshot(self.page, "verify_privacy_notice_url", "reports/screenshots/contact_page")
        privacy_page.close()
