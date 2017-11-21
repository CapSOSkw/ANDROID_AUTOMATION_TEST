from behave import *
from appium import webdriver
import config
from pages import *
from pages.settings import SettingsPage
import time

@given('a user is logged in')
def step_impl(context):
	page = LoginPage(context)
	page.check_if_user_is_logged_in()

@then('user clicks the back button')
def step_impl(context):
	page = LoginPage(context)
	page.click_android_back_button()
	page.wait_time()
	pass

@when('user clicks the menu button')
def step_impl(context):
	page = MapPage(context)
	page.click_menu_button()
	pass

@then('user can see the menu list')
def step_impl(context):
	page = MapPage(context)
	time.sleep(2)
	pass

@then('user backs to homepage')
def step_impl(context):
	page = MapPage(context)
	page.back_to_homepage()
	time.sleep(2)
	pass

@then('confirm english is the main language')
def step_impl(context):
	page = SettingsPage(context)
	page.switch_to_english_as_main_language()
	pass