from pages.home_page import HomePage


def test_laptop_navigation(driver):

    home = HomePage(driver)

    home.click_laptops().verify_laptop_list_presence()