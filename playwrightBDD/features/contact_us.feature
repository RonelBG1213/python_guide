Feature: Contact Us Form
  As a user
  I want to fill out the contact form
  So that I can get in touch with Stratpoint

  Scenario: Navigate to Contact Us page directly
    Given I navigate directly to the Contact Us page
    Then I should be on the Contact Us page

  Scenario: Verify all contact form fields are visible
    Given I am on the Contact Us page
    Then I should see the name input field
    And I should see the email input field
    And I should see the contact number field
    And I should see the company input field
    And I should see the job title field
    And I should see the subject field
    And I should see the message textarea
    And I should see the send button

  Scenario: Fill out contact form
    Given I am on the Contact Us page
    When I fill in the contact form with:
      | field          | value                  |
      | name           | John Doe               |
      | email          | john.doe@example.com   |
      | contact_number | +1234567890            |
      | company        | Test Company           |
      | job_title      | QA Engineer            |
      | type_of_inquiry| Services               |
      | subject        | Test Inquiry           |
      | message        | This is a test message |
    Then the form should be filled correctly

  Scenario: Open Privacy Notice in new tab
    Given I am on the Contact Us page
    When I click on the Privacy Notice link
    Then the Privacy Notice should open in a new tab
    And the new tab URL should be "https://stratpoint.com/privacy-notice/"
