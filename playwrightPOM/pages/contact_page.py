from playwright.sync_api import Page, expect
from pages.navigation import Navigation
from locators.contact_page_locators import ContactPageLocators

class ContactPage:
    def __init__(self, page: Page):
        self.page = page
        self.locators = ContactPageLocators(page)
        self.navigation = Navigation(page)

    def verify_contact_page_loaded(self):
        """Verify we're on the contact page"""
        expect(self.page).to_have_url("https://stratpoint.com/contact-us/")

    def fill_contact_form(self, name, email, contact_number, company, job_title, type_of_inquiry, subject, message):
        self.locators.name_input.fill(name)
        self.locators.email_input.fill(email)
        self.locators.contact_number.fill(contact_number)
        self.locators.company_input.fill(company)
        self.locators.job_title_input.fill(job_title)
        self.locators.type_of_inquiry_dropdown_down.fill(type_of_inquiry)
        self.locators.subject_input.fill(subject)
        self.locators.message_textarea.fill(message)

    def submit_form(self):
        """Submit the contact form"""
        self.locators.send_button.click()

    def verify_form_submitted(self):
        """Verify submission success"""
        expect(self.locators.success_message).to_be_visible()

    def open_privacy_notice_in_new_tab(self):
        privacy_notice_href = self.locators.privacy_notice_link.get_attribute("href")

        with self.page.context.expect_page() as new_page_info:
            self.page.evaluate(f"window.open('{privacy_notice_href}', '_blank')")

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page
