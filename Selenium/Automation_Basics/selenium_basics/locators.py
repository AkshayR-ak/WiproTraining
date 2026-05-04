import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

driver = webdriver.Edge(service = Service("../resources/msedgedriver.exe"))

# driver.get('https://google.com')

#ID
# search_input = driver.find_element(By.ID, "APjFqb")
# search_input.send_keys('selenium')
# time.sleep(3)
# search_input.clear()

#NAME
# search_input = driver.find_element(By.NAME, "q")
# search_input.send_keys('locators')
# time.sleep(3)

#NAME
# googlesearch_button = driver.find_element(By.NAME, "btnK")
# googlesearch_button.click()
# time.sleep(3)

#CLASS_NAME
# imfl_button = driver.find_element(By.CLASS_NAME, "RNmpXc")
# imfl_button.click()
# time.sleep(3)

#TAG_NAME
# href_elements = driver.find_elements(By.TAG_NAME, "a")
# for elmt in href_elements:
#     print(f' {elmt.text} - {elmt.get_attribute("href")}')

#LINK_TEXT
# image_link = driver.find_element(By.LINK_TEXT, "Images")
# image_link.click()
# time.sleep(10)

#PARTIAL_LINK_TEXT
# image_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Ima") #ma - Gmail
# image_link.click()
# time.sleep(10)

#CSS_SELECTOR
# search_input = driver.find_element(By.CSS_SELECTOR, "div > textarea")
# search_input.send_keys('selenium')
# time.sleep(3)

#Xpath
# settings_text = driver.find_element(By.XPATH, ""
#                                              "/html/body/div[2]/div[7]/div/div[2]/div[2]/span/span/g-popup/div[1]/div")
# print(settings_text.text)
# time.sleep(3)

# driver.get("https://the-internet.herokuapp.com/tables")
# time.sleep(3)

# and_example = driver.find_element(By.XPATH, "//td[text()='Tim' and @class='first-name']")
# print(f"AND Example -> found with both conditions: {and_example.text}")
#
# or_example = driver.find_element(By.XPATH, "//td[text()='Tim' or text()='Frank']")
# print(f"OR Example -> found with OR conditions: {or_example.text}")
#
#
# # Child - select all 'td' elements that are direct children of a row
# rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr/td")
# print(f"Child Example -> Found {len(rows)} columns in the first table.")
#
# # Parent - get the parent row of a particular cell
# email_cell = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']")
# parent_row = driver.find_element(By.XPATH, "//table[@id='table1']//td[text()='jdoe@hotmail.com']/parent::tr")
#
# print(f"Parent Example -> Email '{email_cell.text}' belongs to row with first name: "
#       f"{parent_row.find_element(By.XPATH, './td[2]').text}")

# Ancestor - get the table element that is an ancestor of a cell
# ancestor_table = driver.find_element(
#     By.XPATH,
#     "//td[text()='jsmith@gmail.com']/ancestor::table"
# )
# print(f"Ancestor Example -> Table ID: {ancestor_table.get_attribute('id')}")
#
# # Descendant - find all descendants (cells) under table body
# descendants = driver.find_elements(
#     By.XPATH,
#     "//table[@id='table1']/descendant::td"
# )
# print(f"Descendant Example -> Found {len(descendants)} descendant cells.")
#

driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Elements used for reference
username_field = driver.find_element(By.ID, "user-name")
password_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login-button")

# above → element located above another
label_above_password = driver.find_element(
    locate_with(By.TAG_NAME, "input").above(password_field)
)

print(f"Above Example -> Text above password: {label_above_password.get_attribute('placeholder')}")
label_above_password.send_keys("standard_user")

# below → element located below another
field_below_username = driver.find_element(
    locate_with(By.TAG_NAME, "input").below(username_field)
)

print(f"Below Example -> Placeholder below username: {field_below_username.get_attribute('placeholder')}")
field_below_username.send_keys("secret_sauce")
time.sleep(5)
login_button.click()
time.sleep(5)

# toRightOf → element to the left of another
twitter_icon = driver.find_element(By.LINK_TEXT, "Twitter")

facebook_icon = driver.find_element(
    locate_with(By.TAG_NAME, "a").to_right_of(twitter_icon)
)

print(f"toRightOf Example -> Element to the right of Twitter icon has href: {facebook_icon.get_attribute('href')}")

# toLeftOf → element to the right of another
left_icon = driver.find_element(
    locate_with(By.TAG_NAME, "a").to_left_of(facebook_icon)
)

print(f"toLeftOf Example -> Element to the left of Facebook icon has href: {left_icon.get_attribute('href')}")

# near → element close to another (within ~50px by default)
near_twitter = driver.find_elements(
    locate_with(By.TAG_NAME, "a").near(twitter_icon)
)
for element in near_twitter:
    print(f"Near Example -> Element near Twitter icon has href: {element.get_attribute('href')}")

time.sleep(3)


driver.quit()

