from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Edge(service=Service("../resources/msedgedriver.exe"))

driver.get("https://www.google.com")

#implicitly_wait
# driver.implicitly_wait(5)
#
# search_box = driver.find_element(By.NAME, "q")
# search_box.send_keys("Selenium")
#
# google_search_button = driver.find_element(By.NAME, "btnK")
# google_search_button.click()


#Explicit Wait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# wait = WebDriverWait(driver, 10)
#
# search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q"))) #TimeoutException
# search_box.send_keys("Explicit Wait")
#
# google_search_button = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
# google_search_button.click()


#Fluent Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

wait = WebDriverWait(driver, timeout=10, poll_frequency=0.3, ignored_exceptions=[NoSuchElementException])

search_box = wait.until(EC.visibility_of_element_located((By.NAME, "q"))) #TimeoutException
search_box.send_keys("Fluent Wait")

google_search_button = wait.until(EC.element_to_be_clickable((By.NAME, "btnI")))
google_search_button.click()