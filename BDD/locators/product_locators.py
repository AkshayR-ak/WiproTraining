from selenium.webdriver.common.by import By


class ProductLocators:

    PRODUCT_LINK = (
        By.LINK_TEXT,
        "Samsung galaxy s6"
    )

    ADD_TO_CART_BUTTON = (
        By.XPATH,
        "//a[text()='Add to cart']"
    )

    CART_MENU = (
        By.ID,
        "cartur"
    )

    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//button[text()='Place Order']"
    )

    NAME = (
        By.ID,
        "name"
    )

    COUNTRY = (
        By.ID,
        "country"
    )

    CITY = (
        By.ID,
        "city"
    )

    CARD = (
        By.ID,
        "card"
    )

    MONTH = (
        By.ID,
        "month"
    )

    YEAR = (
        By.ID,
        "year"
    )

    PURCHASE_BUTTON = (
        By.XPATH,
        "//button[text()='Purchase']"
    )

    PURCHASE_SUCCESS_MESSAGE = (
        By.XPATH,
        "//h2[text()='Thank you for your purchase!']"
    )

    DELETE_BUTTON = (
        By.LINK_TEXT,
        "Delete"
    )

    EMPTY_CART = (
        By.XPATH,
        "//tbody[@id='tbodyid']/tr"
    )