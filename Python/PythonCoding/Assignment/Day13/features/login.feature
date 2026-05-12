Feature: User Authentication

  Background:
    Given the user launches the browser
    And the user navigates to the OrangeHRM login page

  Scenario: Successful login
    When the user enters username "Admin" and password "admin123"
    And the user clicks the login button
    Then the user should be redirected to dashboard