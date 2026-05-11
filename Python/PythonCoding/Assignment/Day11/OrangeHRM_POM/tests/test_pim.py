from pages.login_page import LoginPage
from pages.pim_page import PIMPage
from selenium.webdriver.common.by import By


def test_view_employee(driver):

    login_page = LoginPage(driver)

    login_page.login("Admin", "admin123")

    driver.find_element(By.XPATH, "//span[text()='PIM']").click()

    pim_page = PIMPage(driver)

    personal_page = pim_page.view_first_employee_details()

    assert "OrangeHRM" in personal_page.get_page_title()