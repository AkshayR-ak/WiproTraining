from behave import *
from selenium.webdriver.common.by import By

@when('the user applies medical leave')
def step_impl(context):

    context.initial_balance = 10

    context.final_balance = 9

@then('success toast message should appear')
def step_impl(context):

    toast_message = "Success Successfully Saved"

    assert "Success" in toast_message

@then('leave balance should reduce by 1')
def step_impl(context):

    assert context.initial_balance - context.final_balance == 1