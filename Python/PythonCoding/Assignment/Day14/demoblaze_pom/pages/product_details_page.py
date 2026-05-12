import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


logging.basicConfig(level=logging.INFO)


class ProductDetailsPage(BasePage):

    ADD_TO_CART = (By.LINK_TEXT, "Add to cart")

    def add_product_to_cart(self):
        self.click(self.ADD_TO_CART)

        WebDriverWait(self.driver, 10).until(
            EC.alert_is_present()
        )

        alert = self.driver.switch_to.alert
        logging.info(f"Alert Message: {alert.text}")

        alert.accept()

        logging.info("Product added to cart successfully")
