@Smoke @Regression @Profile
Feature: Profile Update

  Scenario: Upload profile photo
    Given the user is logged into OrangeHRM
    When the user uploads profile image
    Then profile should update successfully