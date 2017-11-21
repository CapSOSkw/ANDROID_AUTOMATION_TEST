from pages import *
from appium import webdriver
from behave import *

@given('the user is logging')
def step_impl(context):
	page = LoginPage(context)
	page.verify_login_page()
	page.wait_time()
	pass

@when('user enters username')
def step_impl(context):
	page = LoginPage(context)
	page.enter_username()
	pass

@when('user enters password')
def step_impl(context):
	page = LoginPage(context)
	page.enter_password()
	pass

@when('user clicks the login button')
def step_impl(context):
	page = LoginPage(context)
	page.click_login_btn()
	page.click_notification_submit()
	pass

@then('user should see the map')
def step_impl(context):
	page = LoginPage(context)
	page.wait_time()
	page.click_notification_submit()
	page.verify_logged_in()
	pass


