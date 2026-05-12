from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.purchase_modal import PurchaseModal


class CartPage(BasePage):

    PLACE_ORDER = (By.XPATH, "//button[text()='Place Order']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "sweet-alert")

    def click_place_order(self):
        self.click(self.PLACE_ORDER)
        return PurchaseModal(self.driver)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)
