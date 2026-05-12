from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.common.by import By

class ProductPage:

    def get_product_price_by_name(self, product_name):

        sl = BuiltIn().get_library_instance('SeleniumLibrary')
        driver = sl.driver

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")

        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text

            if name == product_name:
                price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
                return float(price.replace("$", ""))

        raise Exception(f"Product '{product_name}' not found")