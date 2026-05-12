*** Settings ***
Library      SeleniumLibrary
Library      ../Libraries/ProductPage.py
Resource     ../Resources/common.resource
Resource     ../Resources/login_page.resource

Suite Setup      Open Browser To Application
Suite Teardown   Close Browser Session
Test Teardown    Capture Failure Screenshot

*** Keywords ***
Go To Login Page
    Go To    https://www.saucedemo.com

*** Test Cases ***
Valid Login Test
    [Tags]    Critical    Smoke    Regression
    Set Test Documentation    Verify successful login with valid credentials

    Go To Login Page
    Login To Application    standard_user    secret_sauce
    Verify Products Page

Verify Product Prices
    [Tags]    Regression
    Set Test Documentation    Verify total price calculation using custom Python library

    Go To Login Page
    Login To Application    standard_user    secret_sauce
    Verify Products Page

    ${price1}=    Get Product Price By Name    Sauce Labs Backpack
    ${price2}=    Get Product Price By Name    Sauce Labs Bike Light

    ${total}=    Evaluate    ${price1} + ${price2}

    Should Be Equal As Numbers    ${total}    39.98