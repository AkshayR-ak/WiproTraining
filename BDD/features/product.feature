Feature: Product Purchase Functionality

  Background:
    Given User launches Demoblaze application

  @smoke @purchase
  Scenario: Successful Product Purchase
    When User logs into the application
    And User selects product "Samsung galaxy s6"
    And User adds the product to cart
    And User navigates to cart page
    And User clicks Place Order button
    And User enters purchase details
      | name    | John Doe     |
      | country | India        |
      | city    | Chennai      |
      | card    | 123456789012 |
      | month   | May          |
      | year    | 2026         |
    And User clicks Purchase button
    Then User should see purchase confirmation message

  @regression @cart
  Scenario Outline: Add multiple products to cart
    When User selects product "<product_name>"
    And User adds the product to cart
    Then Product "<product_name>" should be added successfully

    Examples:
      | product_name      |
      | Samsung galaxy s6 |
      | Nokia lumia 1520  |
      | Nexus 6           |

  @negative @purchase
  Scenario: Attempt purchase with empty order form
    When User selects product "Samsung galaxy s6"
    And User adds the product to cart
    And User navigates to cart page
    And User clicks Place Order button
    And User clicks Purchase button
    Then User should see purchase validation message

  @negative @cart
  Scenario: Remove product from cart
    When User selects product "Samsung galaxy s6"
    And User adds the product to cart
    And User navigates to cart page
    And User removes the product from cart
    Then Cart should be empty

  @regression @purchase
  Scenario Outline: Purchase different products
    When User selects product "<product_name>"
    And User adds the product to cart
    And User navigates to cart page
    And User completes purchase for "<product_name>"
    Then Order should be placed successfully

    Examples:
      | product_name      |
      | Samsung galaxy s6 |
      | Sony vaio i5      |
      | Apple monitor 24  |