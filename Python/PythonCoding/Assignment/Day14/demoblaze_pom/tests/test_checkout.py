import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage
from pages.cart_page import CartPage


def test_checkout(driver):

    home = HomePage(driver)

    category = home.click_laptops()

    product_page = category.open_product("Sony vaio i5")

    time.sleep(2)

    product_page.add_product_to_cart()

    home.open_cart()

    cart = CartPage(driver)

    modal = cart.click_place_order()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "name"))
    )

    data = {
        "name": "Akshay",
        "country": "India",
        "city": "Chennai",
        "card": "123456789",
        "month": "05",
        "year": "2026"
    }

    modal.fill_purchase_form(data)

    modal.click_purchase()

    success_message = cart.get_success_message()

    assert "Thank you for your purchase!" in success_message