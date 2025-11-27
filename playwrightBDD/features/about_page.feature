Feature: About Page
  As a user
  I want to navigate to the About page
  So that I can learn more about Stratpoint

  Scenario: Navigate to About page from homepage
    Given I am on the Stratpoint homepage
    When I click on the "About" link
    Then I should be on the About page

  Scenario: Verify About page content is visible
    Given I am on the About page
    Then I should see the About page heading
    And I should see the company description section

  Scenario: Verify About page navigation links
    Given I am on the About page
    Then the navigation menu should be visible
    And the footer should be visible

  Scenario: Verify About page elements are present
    Given I am on the About page
    Then I should see the following page elements:
      | Element         | Expected State |
      | About Heading   | Visible        |
      | Description     | Visible        |
      | Navigation Menu | Visible        |
      | Footer          | Visible        |
