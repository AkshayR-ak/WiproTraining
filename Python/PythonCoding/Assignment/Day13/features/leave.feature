Feature: Leave Workflow

  Scenario: Apply Medical Leave
    Given the user is logged into OrangeHRM
    When the user applies medical leave
    Then success toast message should appear
    And leave balance should reduce by 1