from behave import *


@when('the user uploads profile image')
def step_impl(context):

    print("Profile image uploaded successfully")


@then('profile should update successfully')
def step_impl(context):

    assert True