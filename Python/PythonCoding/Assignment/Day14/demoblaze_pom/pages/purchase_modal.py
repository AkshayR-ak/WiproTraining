import allure

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class PurchaseModal(BasePage):

    NAME = (By.ID, "name")
    COUNTRY = (By.ID, "country")
    CITY = (By.ID, "city")
    CARD = (By.ID, "card")
    MONTH = (By.ID, "month")
    YEAR = (By.ID, "year")
    PURCHASE = (By.XPATH, "//button[text()='Purchase']")

    def fill_purchase_form(self, data):

        with allure.step("Entering Name"):
            self.type(self.NAME, data["name"])

        with allure.step("Entering Country"):
            self.type(self.COUNTRY, data["country"])

        with allure.step("Entering City"):
            self.type(self.CITY, data["city"])

        with allure.step("Entering Card"):
            self.type(self.CARD, data["card"])

        with allure.step("Entering Month"):
            self.type(self.MONTH, data["month"])

        with allure.step("Entering Year"):
            self.type(self.YEAR, data["year"])

    def click_purchase(self):
        self.click(self.PURCHASE)
