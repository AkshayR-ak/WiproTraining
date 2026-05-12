*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${USERNAME_FIELD}      id=user-name
${PASSWORD_FIELD}      id=password
${LOGIN_BUTTON}        id=login-button
${PRODUCT_TITLE}       xpath=//span[text()='Products']
${ERROR_MESSAGE}       xpath=//h3[@data-test='error']

*** Keywords ***
Login To Application
    [Arguments]    ${username}    ${password}
    Input Text    ${USERNAME_FIELD}    ${username}
    Input Password    ${PASSWORD_FIELD}    ${password}
    Click Button    ${LOGIN_BUTTON}

Verify Products Page
    Element Should Be Visible    ${PRODUCT_TITLE}

Invalid Login Scenario
    [Arguments]    ${username}    ${password}    ${expected_error}
    Login To Application    ${username}    ${password}
    Element Text Should Be    ${ERROR_MESSAGE}    ${expected_error}
