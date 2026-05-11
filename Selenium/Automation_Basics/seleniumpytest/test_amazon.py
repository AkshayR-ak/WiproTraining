import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Edge()  # service=Service("../resources/msedgedriver.exe"))
    driver.get("https://www.amazon.in")
    driver.maximize_window()

    time.sleep(5)
    yield driver
    driver.quit()

def test_open_amazon(driver):
    assert "amazon" in driver.current_url, 'URL for amazon is not correct'
    assert "amazon" in driver.title, 'Title for amazon is not correct'
    print("\nOpened Amazon Homepage. Title & URL verified.")

def test_search_product(driver):
    wait = WebDriverWait(driver, 5)
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.clear()
    search_box.send_keys("wireless mouse")
    time.sleep(2)

    search_button = driver.find_element(By.ID, "nav-search-submit-button")
    search_button.click()
    time.sleep(2)
    # assert "wireless" in driver.current_url
    assert driver.current_url.__contains__('wireless'), 'Search results page did not load.'
    assert driver.title.__contains__('wireless'), 'Search results page did not load.'
    print("\nSearch results page loaded successfully.")

def test_find_elements_amazon(driver):
    wait = WebDriverWait(driver, 15)

    # Single product title
    first_product = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a h2 span"))
    )
    print("\nFirst Product:", first_product.text)
    time.sleep(2)
    product_titles = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a h2 span"))
    )
    print(f"\nFound {len(product_titles)} product titles on page one.\n")
    time.sleep(2)
    for i, title in enumerate(product_titles[:5], start=1):
        print(f"{i}. {title.text}")
    time.sleep(2)
    assert len(product_titles) > 0, "No products found on Amazon search results!"

