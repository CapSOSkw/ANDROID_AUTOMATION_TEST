from pages.settings import SettingsPage
from appium import webdriver
from behave import *
from time import sleep
import random

@then('user clicks settings button menu')
def step_impl(context):
    page = SettingsPage(context)
    page.click_setting_menu_button()
    pass

@then('user can see setting options')
def step_impl(context):
    page = SettingsPage(context)
    page.verify_setting_options()
    pass

@then('user clicks sign out button')
def step_impl(context):
    page = SettingsPage(context)
    page.click_sign_out_button()
    pass

@then('user can cancel or sign out')
def step_impl(context):
    page = SettingsPage(context)
    page.cancel_or_sign_out()
    sleep(5)
    pass

@then('user clicks edit profile button')
def step_impl(context):
    page = SettingsPage(context)
    page.click_edit_profile_button()
    pass


@then('user clicks the driver preference button')
def step_impl(context):
    page = SettingsPage(context)
    page.click_driver_preferences()
    pass


@then('user can see the preference options')
def step_impl(context):
    page = SettingsPage(context)
    page.verify_driver_preference_elements()
    pass

@then('user can choose different preferences')
def step_impl(context):
    page = SettingsPage(context)
    page.prefer_favorite_driver(on=random.choice([True,False]))
    page.wheelchair_assistance(on=random.choice([True,False]))
    page.select_driver_gener()
    page.select_driver_language()
    page.select_driving_exp()
    page.select_vehicle_brand()
    page.select_country_origin()
    pass

@then('user can save the preference changes')
def step_impl(context):
    page = SettingsPage(context)
    page.click_driver_prefenerce_save_button()
    pass

@then('user clicks the language button')
def step_impl(context):
    page = SettingsPage(context)
    page.click_language_button()
    pass

@then('user can choose english or chinese')
def step_impl(context):
    page = SettingsPage(context)
    page.click_language_chinese()
    pass

@then('the language is changed')
def step_impl(context):
    page = SettingsPage(context)
    page.verify_switch_to_chinese_succeed()
    pass