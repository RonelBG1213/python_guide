class ContactPageLocators:
    def __init__(self, page):
        # Using label-based locators for better reliability
        self.name_input = page.locator('input[name="name_field"]')
        self.email_input = page.locator('input[name="email_field"]')
        self.contact_number = page.locator('input[name="contact_field"]')
        self.company_input = page.locator('input[name="company_field"]')
        self.job_title_input = page.locator('input[name="job_field"]')
        self.type_of_inquiry_dropdown = page.locator('select[name="recipient"]')
        self.subject_input = page.locator('input[name="subject_field"]')
        self.privacy_notice_link = page.get_by_role("link", name="Privacy Notice")
        self.message_textarea = page.locator('textarea[name="message_field"]')
        self.send_button = page.get_by_role("button", name="Send")
        self.success_message = page.get_by_text("Thank you")
