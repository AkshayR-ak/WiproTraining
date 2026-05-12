from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('the user is logged into OrangeHRM')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait = WebDriverWait(context.driver, 20)

    username = wait.until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    password = wait.until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )

    username.send_keys("Admin")
    password.send_keys("admin123")
    context.driver.find_element(By.TAG_NAME, "button").click()

@when('I enter "{firstname}" and "{lastname}"')
def step_impl(context, firstname, lastname):

    wait = WebDriverWait(context.driver, 20)

    context.driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/pim/addEmployee"
    )

    context.driver.refresh()

    first = wait.until(
        EC.visibility_of_element_located((By.NAME, "firstName"))
    )

    first.clear()
    first.send_keys(firstname)

    last = context.driver.find_element(By.NAME, "lastName")

    last.clear()
    last.send_keys(lastname)

    save_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")
        )
    )

    context.driver.execute_script(
        "arguments[0].click();",
        save_btn
    )

@then('employee should be created successfully')
def step_impl(context):

    assert "pim" in context.driver.current_url.lower()