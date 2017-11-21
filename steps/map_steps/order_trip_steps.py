from pages import *
from appium import webdriver
from behave import *
from time import sleep

@when('user clicks the current location button')
def step_impl(context):
    page = MapPage(context)
    page.click_current_location_btn()
    pass

@then('user can see the current location')
def step_impl(context):
    page = MapPage(context)
    sleep(2)

@when('user clicks pickup location box')
def step_impl(context):
    page = MapPage(context)
    page.click_pickup_location_box()
    pass

@then('user can enter pickup location')
def step_impl(context):
    page = MapPage(context)
    page.enter_pickup_location()
    sleep(2)
    pass

@then('user clicks the first pickup dropdown')
def step_impl(context):
    page = MapPage(context)
    page.click_location_1st_dropdown()
    sleep(5)
    pass

@when('user clicks destination location box')
def step_impl(context):
    page = MapPage(context)
    page.click_destination_location_box()
    sleep(2)
    pass

@then('user can enter destination location')
def step_impl(context):
    page = MapPage(context)
    page.enter_destination_location()
    pass

@then('user can see the pre-scheduled route')
def step_impl(context):
    page = MapPage(context)
    page.see_preschedule_route()
    sleep(5)
    pass

@then('user can order now or reserve trip')
def step_impl(context):
    page = MapPage(context)
    page.click_order_or_reserve() # default is order, or reserve=True
    sleep(5)
    pass


@then('user clicks my trips menu')
def step_impl(context):
    page = MapPage(context)
    page.click_my_trips()
    pass

@then('user can see trips information')
def step_impl(context):
    page = MapPage(context)
    page.verify_my_trips_elements()
    pass

@then('user clicks the lastest trip')
def step_impl(context):
    page = MapPage(context)
    page.click_the_lastest_trip()
    pass

@then('user can see the lastest trip information')
def step_impl(context):
    page = MapPage(context)
    page.verify_the_lastest_trip_elements()
    pass


@then('user can add driver to favorite or blocking list')
def step_impl(context):
    page = MapPage(context)
    page.favorite_or_block_driver()
    sleep(2)
    try:
        page.yes_or_no_buttons(no=True)
    except:
        pass


@then('user clicks report lost item')
def step_impl(context):
    page = MapPage(context)
    page.click_report_lost_item()
    pass


@then('user can report lost item')
def step_impl(context):
    page = MapPage(context)
    page.cancel_or_report(cancel=True)
    pass


@then('user selects vehicle type')
def step_impl(context):
    page = MapPage(context)
    page.click_vehicle_type()
    pass


@then('user clicks request ride button')
def step_impl(context):
    page = MapPage(context)
    page.click_request_ride_button()
    pass

@then('user waits for driver response')
def step_impl(context):
    page = MapPage(context)
    sleep(10)
    pass