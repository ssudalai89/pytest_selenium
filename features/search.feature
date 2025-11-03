Feature: Google Search Functionality

  Scenario: Verify Google search works correctly
    Given I open the Google homepage
    When I search for "Pytest BDD tutorial"
    Then I should see search results related to "Pytest BDD tutorial"
