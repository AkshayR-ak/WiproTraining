from pages.home_page import HomePage


def test_product_search(driver):

    home = HomePage(driver)

    category = home.click_phones()

    product_names = category.get_all_product_names()

    assert "Samsung galaxy s6" in product_names
