from selenium.webdriver.common.by import By

from locators.product_locators import ProductLocators
from utils.waits import WaitUtils
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil

import allure


logger = LogGen.loggen()


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

    def select_product(self, product_name):
        logger.info(
            f"Selecting Product : {product_name}"
        )
        product = (
            By.LINK_TEXT,
            product_name
        )
        WaitUtils.wait_for_element_clickable(
            self.driver,
            product
        ).click()

    def add_product_to_cart(self):
        logger.info(
            "Adding Product To Cart"
        )
        WaitUtils.wait_for_element_clickable(
            self.driver,
            ProductLocators.ADD_TO_CART_BUTTON
        ).click()
        alert = WaitUtils.wait_for_alert(
            self.driver
        )
        logger.info(
            f"Alert Message : {alert.text}"
        )
        alert.accept()

    def navigate_to_cart(self):
        logger.info(
            "Navigating To Cart"
        )
        WaitUtils.wait_for_element_clickable(
            self.driver,
            ProductLocators.CART_MENU
        ).click()

    def click_place_order(self):
        logger.info(
            "Clicking Place Order"
        )
        WaitUtils.wait_for_element_clickable(
            self.driver,
            ProductLocators.PLACE_ORDER_BUTTON
        ).click()

    def enter_purchase_details(
            self,
            details
    ):
        logger.info(
            "Entering Purchase Details"
        )
        WaitUtils.wait_for_element_visible(
            self.driver,
            ProductLocators.NAME
        ).send_keys(details["name"])
        self.driver.find_element(
            *ProductLocators.COUNTRY
        ).send_keys(details["country"])
        self.driver.find_element(
            *ProductLocators.CITY
        ).send_keys(details["city"])
        self.driver.find_element(
            *ProductLocators.CARD
        ).send_keys(details["card"])
        self.driver.find_element(
            *ProductLocators.MONTH
        ).send_keys(details["month"])
        self.driver.find_element(
            *ProductLocators.YEAR
        ).send_keys(details["year"])

    def click_purchase_button(self):
        logger.info(
            "Clicking Purchase Button"
        )
        WaitUtils.wait_for_element_clickable(
            self.driver,
            ProductLocators.PURCHASE_BUTTON
        ).click()

    def verify_purchase_success(self):
        logger.info(
            "Verifying Purchase Success"
        )
        element = WaitUtils.wait_for_element_visible(
            self.driver,
            ProductLocators.PURCHASE_SUCCESS_MESSAGE
        )
        assert element.is_displayed()
        screenshot_path = (
            ScreenshotUtil.capture_screenshot(
                self.driver,
                "purchase_success"
            )
        )
        logger.info(
            f"Screenshot Captured : "
            f"{screenshot_path}"
        )
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="Purchase Success",
            attachment_type=allure.attachment_type.PNG
        )

    def remove_product_from_cart(self):
        logger.info(
            "Removing Product From Cart"
        )
        WaitUtils.wait_for_element_clickable(
            self.driver,
            ProductLocators.DELETE_BUTTON
        ).click()

    def verify_cart_empty(self):
        logger.info(
            "Verifying Cart Empty"
        )
        elements = self.driver.find_elements(
            *ProductLocators.EMPTY_CART
        )
        assert len(elements) == 0
        logger.info(
            "Cart Verified Empty"
        )

