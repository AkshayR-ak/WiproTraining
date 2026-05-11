from selenium.webdriver.common.by import By


class SideMenuComponent:

    def __init__(self, driver):
        self.driver = driver

    def click_admin(self):
        self.driver.find_element(
            By.XPATH,
            "//span[text()='Admin']"
        ).click()

    def click_pim(self):
        self.driver.find_element(
            By.XPATH,
            "//span[text()='PIM']"
        ).click()

    def click_leave(self):
        self.driver.find_element(
            By.XPATH,
            "//span[text()='Leave']"
        ).click()
