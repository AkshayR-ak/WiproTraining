*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}         https://www.saucedemo.com
${BROWSER}     chrome

*** Keywords ***
Open Browser To Application
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait    5s

Close Browser Session
    Close Browser

Capture Failure Screenshot
    ${timestamp}=    Get Time    epoch
    Run Keyword If Test Failed    Capture Page Screenshot    failure_${TEST_NAME}_${timestamp}.png
