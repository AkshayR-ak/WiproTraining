from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.personal_details_page import PersonalDetailsPage


class PIMPage:

    def __init__(self, driver):
        self.driver = driver

    def view_first_employee_details(self):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "(//div[@role='row'])[2]")
            )
        )

        employee = self.driver.find_element(
            By.XPATH,
            "(//div[@role='row'])[2]"
        )

        employee.click()

        return PersonalDetailsPage(self.driver)