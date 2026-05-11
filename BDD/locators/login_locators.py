from selenium.webdriver.common.by import By


class LoginLocators:

    LOGIN_MENU = (
        By.ID,
        "login2"
    )

    USERNAME = (
        By.ID,
        "loginusername"
    )

    PASSWORD = (
        By.ID,
        "loginpassword"
    )

    LOGIN_BUTTON = (
        By.XPATH,
        "//button[text()='Log in']"
    )

    LOGOUT_BUTTON = (
        By.ID,
        "logout2"
    )

    LOGIN_ERROR_MESSAGE = (
        By.XPATH,
        "//div[contains(text(),'Wrong password')]"
    )

