Feature: Admin Search

  Scenario: Search user with data table
    Given the user is logged into OrangeHRM
    When I enter the following search criteria:
      | field      | value   |
      | Username   | Admin   |
      | User Role  | Admin   |
      | Status     | Enabled |
    Then matching records should be displayed