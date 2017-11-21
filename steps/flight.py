from behave import *
from appium import webdriver
import config
from pages.flight_check import FlightPage
import time


@when('user clicks the flight check button in menu list')
def step_impl(context):
    page = FlightPage(context)
    page.click_flight_check_menu_btn()
    pass

@then('user can check flight')
def step_impl(context):
    page = FlightPage(context)
    page.verify_in_flight_check()
    pass

@then('user enters airline')
def step_impl(context):
    page = FlightPage(context)
    page.enter_flight_airline('UA')
    pass

@then('user enters airline number')
def step_impl(context):
    page = FlightPage(context)
    page.enter_flight_airline_number('87')
    pass


@then('user opens calendar')
def step_impl(context):
    page = FlightPage(context)
    page.click_flight_check_calendar()
    time.sleep(2)
    pass

@then('user clicks random date')
def step_impl(context):
    page = FlightPage(context)
    page.random_choose_day_before_or_after()
    time.sleep(2)
    pass

@then('user clicks calendar ok button')
def step_impl(context):
    page = FlightPage(context)
    page.click_calendar_ok_button()
    time.sleep(2)
    pass


@then('user clicks the flight check button')
def step_impl(context):
    page = FlightPage(context)
    page.click_flight_check_button()
    time.sleep(2)
    pass

@then('user can see the result of flight check')
def step_impl(context):
    page = FlightPage(context)
    page.verify_flight_check_result()
    pass