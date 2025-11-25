Feature: Stratpoint Homepage
  As a user
  I want to navigate the Stratpoint homepage
  So that I can access different sections of the website

  Scenario: Verify homepage banner heading is visible
    Given I am on the Stratpoint homepage
    Then I should see the banner heading "Fast forward to the future"

  Scenario: Navigate to Contact Us page
    Given I am on the Stratpoint homepage
    When I click on the "Contact Us" link
    Then I should be on the Contact Us page

  Scenario: Verify Let's Connect heading is visible
    Given I am on the Stratpoint homepage
    Then I should see the heading "Let's Connect"
