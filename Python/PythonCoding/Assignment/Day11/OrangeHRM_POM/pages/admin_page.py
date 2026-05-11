from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.components.side_menu_component import SideMenuComponent


class AdminPage:

    def __init__(self, driver):
        self.driver = driver
        self.side_menu = SideMenuComponent(driver)

    def get_all_usernames(self):

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(
                (By.XPATH, "//div[@role='table']//div[@role='row']/div[2]")
            )
        )

        users = self.driver.find_elements(
            By.XPATH,
            "//div[@role='table']//div[@role='row']/div[2]"
        )

        usernames = []

        for user in users:
            usernames.append(user.text)

        return usernames

    def verify_user_exists(self, username):

        usernames = self.get_all_usernames()

        return username in usernames
