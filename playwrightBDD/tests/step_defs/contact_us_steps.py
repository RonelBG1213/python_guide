from pytest_bdd import given, when, then, scenarios, parsers
from main.pages.contact_page import ContactPage
from main.pages.navigation import Navigation

scenarios('../../features/contact_us.feature')

# Given steps
@given('I navigate directly to the Contact Us page')
def navigate_to_contact_page_directly(page):
    navigation = Navigation(page)
    navigation.navigate_to_contact_us()

@given('I am on the Contact Us page')
def navigate_to_contact_page(page):
    navigation = Navigation(page)
    navigation.navigate_to_contact_us()
    contact_page = ContactPage(page)
    contact_page.verify_contact_page_loaded()

# Then steps
@then('I should be on the Contact Us page')
def verify_on_contact_page(page):
    contact_page = ContactPage(page)
    contact_page.verify_contact_page_loaded()

@then('I should see the name input field')
def verify_name_field(page):
    contact_page = ContactPage(page)
    contact_page.verify_name_field_visible()

@then('I should see the email input field')
def verify_email_field(page):
    contact_page = ContactPage(page)
    contact_page.verify_email_field_visible()

@then('I should see the contact number field')
def verify_contact_number_field(page):
    contact_page = ContactPage(page)
    contact_page.verify_contact_number_field_visible()

@then('I should see the company input field')
def verify_company_field(page):
    contact_page = ContactPage(page)
    contact_page.verify_company_field_visible()

@then('I should see the job title field')
def verify_job_title_field(page):
    contact_page = ContactPage(page)
    contact_page.verify_job_title_field_visible()

@then('I should see the subject field')
def verify_subject_field(page):
    contact_page = ContactPage(page)
    contact_page.verify_subject_field_visible()

@then('I should see the message textarea')
def verify_message_field(page):
    contact_page = ContactPage(page)
    contact_page.verify_message_field_visible()

@then('I should see the send button')
def verify_send_button(page):
    contact_page = ContactPage(page)
    contact_page.verify_send_button_visible()

# When steps
@when('I fill in the contact form with:')
def fill_contact_form(page, datatable):
    contact_page = ContactPage(page)
    # Skip header row and convert to dict
    data = {row[0]: row[1] for row in datatable[1:]}
    contact_page.fill_contact_form(
        name=data['name'],
        email=data['email'],
        contact_number=data['contact_number'],
        company=data['company'],
        job_title=data['job_title'],
        type_of_inquiry=data['type_of_inquiry'],
        subject=data['subject'],
        message=data['message']
    )

@when('I click on the Privacy Notice link')
def click_privacy_notice(page):
    contact_page = ContactPage(page)
    privacy_page = contact_page.open_privacy_notice_in_new_tab()
    page.context._privacy_page = privacy_page

@then('the form should be filled correctly')
def verify_form_filled(page):
    pass

@then('the Privacy Notice should open in a new tab')
def verify_new_tab_opened(page):
    contact_page = ContactPage(page)
    privacy_page = page.context._privacy_page
    contact_page.verify_privacy_notice_opened(privacy_page)

@then(parsers.parse('the new tab URL should be "{url}"'))
def verify_new_tab_url(page, url):
    contact_page = ContactPage(page)
    privacy_page = page.context._privacy_page
    contact_page.verify_privacy_notice_url(privacy_page, url)
