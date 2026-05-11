
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.EdgeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Edge(options=options)
driver.implicitly_wait(10)
driver.get("https://www.amazon.in")

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.ID, "twotabsearchtextbox")
    )
)
time.sleep(3)
title = driver.title
print("Page Title:", title)

assert driver.current_url.startswith("https://www.amazon")

mobiles_link = driver.find_element(By.LINK_TEXT, "Mobiles")
mobiles_link.click()
print("Navigated to Mobiles Page")
time.sleep(3)

driver.back()
print("Navigated Back to Home Page")
time.sleep(3)

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("Wireless Headphones")

search_button = driver.find_element(
    By.XPATH,
    "//input[@id='nav-search-submit-button']"
)

search_button.click()

result_text = driver.find_element(
    By.XPATH,
    "//span[contains(text(),'Wireless Headphones')]"
).text

print("Search Result Text:", result_text)

assert "Wireless Headphones" in result_text

time.sleep(3)


search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("Dell Laptop")

search_button = driver.find_element(
    By.XPATH,
    "//input[@id='nav-search-submit-button']"
)

search_button.click()

wait = WebDriverWait(driver, 15)

first_product = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "(//img[contains(@class,'s-image')])[1]")
    )
)

first_product.click()

print("First Laptop Product Clicked")

time.sleep(3)

driver.get("https://www.amazon.in")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)

try:
    close_popup = driver.find_element(
        By.XPATH,
        "//button[@data-action='a-popover-close']"
    )
    close_popup.click()
    time.sleep(2)

except:
    pass

# Locate About Us link
about_us = driver.find_element(
    By.CSS_SELECTOR,
    "a[href*='aboutamazon']"
)

driver.execute_script("arguments[0].scrollIntoView();", about_us)

time.sleep(2)

driver.execute_script("arguments[0].click();", about_us)

time.sleep(3)

careers_link = driver.find_element(By.LINK_TEXT, "Careers")

print("Text Content:", careers_link.text)

time.sleep(3)

driver.get("https://www.amazon.in")

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("Smart Watches")

search_button = driver.find_element(
    By.XPATH,
    "//input[@id='nav-search-submit-button']"
)
search_button.click()
wait = WebDriverWait(driver, 15)
time.sleep(5)
brand_filter = driver.find_element(
    By.XPATH,
    "//span[contains(text(),'Samsung')]"
)

driver.execute_script(
    "arguments[0].scrollIntoView();",
    brand_filter
)
time.sleep(2)
driver.execute_script(
    "arguments[0].click();",
    brand_filter
)
brand_filter.click()
wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//div[@data-component-type='s-search-result']")
    )
)
products = driver.find_elements(
    By.XPATH,
    "//div[@data-component-type='s-search-result']"
)
print("Number of Products Displayed:", len(products))
time.sleep(5)

driver.quit()