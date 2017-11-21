from pages.favorite_drivers import FavoriteDriversPage
from appium import webdriver
from behave import *
from time import sleep

@then('user clicks favorite drivers menu button')
def step_impl(context):
    page = FavoriteDriversPage(context)
    page.click_favorite_drivers_menu_button()
    pass

@then('user can see favorite drivers information')
def step_impl(context):
    page = FavoriteDriversPage(context)
    page.verify_favorite_drivers()
    pass

@then('user clicks add a new favorite driver button')
def step_impl(context):
    page = FavoriteDriversPage(context)
    page.click_add_a_new_favorite_driver()
    pass

@then('user enters driver username')
def step_impl(context):
    page = FavoriteDriversPage(context)
    page.enter_driver_username_in_search_box()
    pass

@then('user clicks the 1st dropdown adding request button')
def step_impl(context):
    page = FavoriteDriversPage(context)
    page.click_1st_dropdown_adding_button()
    pass

@then('a favorite adding request is sending')
def step_impl(context):
    page = FavoriteDriversPage(context)
    sleep(5)
    pass

@then('user clicks delete a favorite driver button')
def step_impl(context):
    page = FavoriteDriversPage(context)
    page.click_delete_driver_button()
    pass

@then('user clicks cancel or remove button')
def step_impl(context):
    page = FavoriteDriversPage(context)
    page.cancel_or_remove()   #default is cancel, or remove==True
    pass

@then('a favorite driver is deleted')
def step_impl(context):
    page = FavoriteDriversPage(context)
    sleep(5)
    pass


@then('user clicks the request button from the 1st driver')
def step_impl(context):
    page = FavoriteDriversPage(context)
    page.click_request_button_from_1st_driver()
    sleep(2)
    pass

@then('user enters pickup location in the request page')
def step_impl(context):
    page = FavoriteDriversPage(context)
    page.click_pickup_location_box()
    page.enter_pickup_location()
    page.click_location_1st_dropdown()
    sleep(2)
    pass

@then('user enters destination location in the request page')
def step_impl(context):
    page = FavoriteDriversPage(context)
    page.click_destination_location_box()
    page.enter_destination_location()
    page.click_location_1st_dropdown()
    sleep(2)
    pass

@then('user can cancel or send request')
def step_impl(context):
    page = FavoriteDriversPage(context)
    page.click_cancel_or_request_submit_button()   #default is cancel, or request==True
    sleep(5)
    pass