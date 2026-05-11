from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[text()='Dashboard']")
            )
        )

    def get_dashboard_heading(self):
        return self.driver.find_element(
            By.XPATH,
            "//h6[text()='Dashboard']"
        ).text
