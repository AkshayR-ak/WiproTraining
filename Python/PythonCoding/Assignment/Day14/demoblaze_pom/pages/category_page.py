from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.product_details_page import ProductDetailsPage


class CategoryPage(BasePage):

    PRODUCTS = (By.CLASS_NAME, "hrefch")

    def verify_laptop_list_presence(self):
        products = self.finds(self.PRODUCTS)
        assert len(products) > 0

    def get_all_product_names(self):
        products = self.finds(self.PRODUCTS)
        return [product.text for product in products]

    def open_product(self, product_name):
        products = self.finds(self.PRODUCTS)

        for product in products:
            if product.text == product_name:
                product.click()
                break

        return ProductDetailsPage(self.driver)
