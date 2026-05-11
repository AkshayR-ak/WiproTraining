from locators.login_locators import LoginLocators
from utils.waits import WaitUtils
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil

import allure

logger = LogGen.loggen()


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_login_menu(self):
        logger.info("Clicking Login Menu")
        WaitUtils.wait_for_element_clickable(
            self.driver,
            LoginLocators.LOGIN_MENU
        ).click()

    def enter_username(self, username):
        logger.info(
            f"Entering Username : {username}"
        )
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            LoginLocators.USERNAME
        )
        element.clear()
        element.send_keys(username)

    def enter_password(self, password):
        logger.info("Entering Password")
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            LoginLocators.PASSWORD
        )
        element.clear()
        element.send_keys(password)

    def click_login_button(self):
        logger.info("Clicking Login Button")
        WaitUtils.wait_for_element_clickable(
            self.driver,
            LoginLocators.LOGIN_BUTTON
        ).click()

    def verify_successful_login(self):
        logger.info(
            "Verifying Successful Login"
        )
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            LoginLocators.LOGOUT_BUTTON
        )
        assert element.is_displayed()
        logger.info(
            "Login Successful"
        )

    def verify_login_alert(self):
        logger.info(
            "Verifying Login Alert"
        )
        alert = WaitUtils.wait_for_alert(
            self.driver
        )
        alert_text = alert.text
        logger.info(
            f"Alert Message : {alert_text}"
        )
        ScreenshotUtil.capture_screenshot(
            self.driver,
            "login_alert"
        )
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Login Alert Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
        alert.accept()
        return alert_text

    def click_logout(self):
        logger.info(
            "Clicking Logout Button"
        )
        WaitUtils.wait_for_element_clickable(
            self.driver,
            LoginLocators.LOGOUT_BUTTON
        ).click()

    def verify_logout(self):
        logger.info(
            "Verifying Logout"
        )
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            LoginLocators.LOGIN_MENU
        )
        assert element.is_displayed()
        logger.info(
            "Logout Successful"
        )


        