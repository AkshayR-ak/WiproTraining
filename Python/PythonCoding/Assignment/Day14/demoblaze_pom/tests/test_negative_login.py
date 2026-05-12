from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_page import HomePage


def test_invalid_login(driver):

    home = HomePage(driver)

    home.open_login()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "loginusername"))
    )

    driver.find_element(By.ID, "loginusername").send_keys("pavanol")

    driver.find_element(By.ID, "loginpassword").send_keys("wrongpassword")

    driver.find_element(By.XPATH, "//button[text()='Log in']").click()

    WebDriverWait(driver, 10).until(
        EC.alert_is_present()
    )

    alert = driver.switch_to.alert

    alert_text = alert.text

    alert.accept()

    # Intentional failure for screenshot capture
    assert alert_text == "Success"