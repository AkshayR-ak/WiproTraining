
Feature: Login Functionality

  Background:
    Given User launches application

  @smoke @login
  Scenario: Valid Login
    When User clicks on Login menu
    And User enters valid username "userppppp"
    And User enters valid password "pwdppppp"
    And User clicks Login button
    Then User should login successfully

  @regression @login @negative
  Scenario Outline: Invalid Login with incorrect credentials
    When User clicks on Login menu
    And User enters username "<username>"
    And User enters password "<password>"
    And User clicks Login button
    Then User should see login error message

    Examples:
      | username   | password   |
      | invalid1   | invalid123 |
      | admin      | wrongpass  |
      | wronguser  | test123    |

  @negative @login
  Scenario Outline: Login with empty fields
    When User clicks on Login menu
    And User enters username "<username>"
    And User enters password "<password>"
    And User clicks Login button
    Then User should see validation alert

    Examples:
      | username | password |
      |          | test123  |
      | testuser |          |
      |          |          |

  @regression @login
  Scenario: Logout functionality
    When User clicks on Login menu
    And User enters valid username "userppppp"
    And User enters valid password "pwdppppp"
    And User clicks Login button
    And User clicks Logout button
    Then User should logout successfully