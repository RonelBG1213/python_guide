class ContactPageLocators:
    def __init__(self, page):
        self.name_input = page.get_by_role("textbox", name="name_field")
        self.email_input = page.get_by_role("textbox", name="email_field")
        self.contact_number = page.get_by_role("textbox", name="contact_field")
        self.company_input = page.get_by_role("textbox", name="company")
        self.job_title_input = page.get_by_role("textbox", name="job_field")
        self.type_of_inquiry_dropdown_down = page.get_by_role("textbox", name="recipient")
        self.subject_input = page.get_by_role("textbox", name="subject_field")
        self.privacy_notice_link = page.get_by_role("link", name="Privacy Notice")
        self.message_textarea = page.get_by_role("textbox", name="message_field")
        self.send_button = page.get_by_role("button", name="Send")
        self.success_message = page.get_by_text("Thank you")
