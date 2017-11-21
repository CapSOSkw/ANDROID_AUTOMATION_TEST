from behave import *
from appium import webdriver
import config
from pages.profile import ProfilePage
import time,random,string


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@when('user clicks image profile button')
def step_impl(context):
    page = ProfilePage(context)
    page.click_image_profile_button_menu()
    pass

@then('user can see profile information')
def step_impl(context):
    page = ProfilePage(context)
    page.verify_in_profile_page()
    pass


@when('user clicks QR code button')
def step_impl(context):
    page = ProfilePage(context)
    page.click_QR_code_button()
    pass

@then('user can see QR code')
def step_impl(context):
    page = ProfilePage(context)
    page.verify_QR_code_exist()
    pass

@then('user clicks QR code cancel button')
def step_impl(context):
    page = ProfilePage(context)
    page.click_QR_code_cancel_button()
    pass

@then('user clicks profile save button')
def step_impl(context):
    page = ProfilePage(context)
    page.click_profile_save_button()
    pass

@then('user can save the change')
def step_impl(context):
    page = ProfilePage(context)
    page.verify_save_succeed()
    pass


@then('user can edit first name')
def step_impl(context):
    page = ProfilePage(context)
    page.edit_firstname('Keyuan'+randomword(1))
    pass

@then('user can edit last name')
def step_impl(context):
    page = ProfilePage(context)
    page.edit_lastname('Wu'+randomword(1))
    pass