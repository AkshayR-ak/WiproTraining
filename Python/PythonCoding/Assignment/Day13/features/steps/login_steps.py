from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('the user launches the browser')
def step_impl(context):
    pass


@given('the user navigates to the OrangeHRM login page')
def step_impl(context):
    context.driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )


@when('the user enters username "{username}" and password "{password}"')
def step_impl(context, username, password):

    wait = WebDriverWait(context.driver, 20)

    username_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    password_field = wait.until(
        EC.visibility_of_element_located((By.NAME, "password"))
    )

    username_field.send_keys(username)
    password_field.send_keys(password)


@when('the user clicks the login button')
def step_impl(context):

    wait = WebDriverWait(context.driver, 20)

    login_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )

    login_btn.click()


@then('the user should be redirected to dashboard')
def step_impl(context):

    wait = WebDriverWait(context.driver, 20)

    wait.until(EC.url_contains("dashboard"))

    assert "dashboard" in context.driver.current_url.lower()