import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge()  # service=Service("../resources/msedgedriver.exe"))
    driver.maximize_window()
    driver.get("https://www.amazon.in")
    time.sleep(2)
    driver.maximize_window()
    yield driver
    driver.quit()