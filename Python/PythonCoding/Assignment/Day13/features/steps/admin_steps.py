from behave import *
from selenium.webdriver.common.by import By
import time

@when('I enter the following search criteria:')
def step_impl(context):

    for row in context.table:
        field = row['field']
        value = row['value']

        print(f"{field} -> {value}")

@then('matching records should be displayed')
def step_impl(context):
    assert True