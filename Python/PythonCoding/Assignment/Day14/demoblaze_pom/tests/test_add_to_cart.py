import time

from pages.home_page import HomePage


def test_add_product_to_cart(driver):

    home = HomePage(driver)

    category = home.click_laptops()

    product_page = category.open_product("Sony vaio i5")

    time.sleep(2)

    product_page.add_product_to_cart()
