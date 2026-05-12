*** Settings ***
Library      SeleniumLibrary
Resource     ../Resources/common.resource
Resource     ../Resources/login_page.resource

Suite Setup      Open Browser To Application
Suite Teardown   Close Browser Session
Test Teardown    Capture Failure Screenshot

Test Template    Invalid Login Scenario

*** Test Cases ***                      USERNAME           PASSWORD        ERROR MESSAGE
Invalid User Test                      invalid_user       secret_sauce    Epic sadface: Username and password do not match any user in this service
Locked User Test                       locked_out_user    secret_sauce    Epic sadface: Sorry, this user has been locked out.
Problem User Test                      problem_user       wrong_pass      Epic sadface: Username and password do not match any user in this service
