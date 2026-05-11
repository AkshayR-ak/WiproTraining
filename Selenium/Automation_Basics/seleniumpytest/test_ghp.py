import time
import pytest
from pytest_check import check
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Edge()  # service=Service("../resources/msedgedriver.exe"))
    driver.maximize_window()
    driver.get('https://www.google.com')
    yield driver
    driver.quit()

def test_ghpload(driver):
    pagetitle = driver.title
    assert pagetitle == 'Google', 'Google Home Page Not Loaded'

def test_imagespageload(driver):
    driver.find_element(By.LINK_TEXT, "Images").click()
    pagetitle = driver.title
    assert pagetitle == 'Google Images', 'Images Page Not Loaded'

def test_businesslink(driver):
    driver.find_element(By.LINK_TEXT, "Business").click()
    wait = WebDriverWait(driver, 10)    #Explicit Wait
    wait.until(EC.title_contains("Business"))
    # assert "Business" in driver.title, 'Business Page Not Loaded - Title check'
    # assert "business" in driver.current_url, 'Business Page Not Loaded - URL check'
    check.is_in("Business", driver.title,  "Business Page Not Loaded - Title check")
    check.is_in("business", driver.current_url, "Business page not loaded - URL check")

    