from locators.locators import *
from .base import BasePage
import config
import time
import requests
from appium.webdriver.common.touch_action import TouchAction


class FavoriteDriversPage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context)

    def click_menu_button(self):
        try:
            self.verify_if_on_menu_list()
        except:

            self.find_element(*MapPageLocators.MENU_BTN).click()

    def verify_if_on_menu_list(self):
        self.find_element(*MenuPageLocators.MY_TRIP_MENU)
        self.find_element(*MenuPageLocators.FAVORITE_DRIVERS_MENU)
        self.find_element(*MenuPageLocators.FLIGHT_CHECK_MENU)

    def back_to_homepage(self):
        try:
            self.verify_if_on_menu_list()
            self.android_back()
        except:
            try:
                self.find_element(*MapPageLocators.DESTINATION_BOX)
                self.find_element(*MapPageLocators.CURRENT_LOCATION_BTN)
                self.find_element(*MapPageLocators.PICKUP_LOCATION_BOX)
            except:
                self.android_back()
                time.sleep(2)
                self.back_to_homepage()

    def click_favorite_drivers_menu_button(self):
        self.find_element(*MenuPageLocators.FAVORITE_DRIVERS_MENU).click()

    def verify_favorite_drivers(self):
        self.find_element(*MenuPageLocators.ADD_A_NEW_FAVORITE_DRIVER)

    def click_add_a_new_favorite_driver(self):
        self.find_element(*MenuPageLocators.ADD_A_NEW_FAVORITE_DRIVER).click()

    def enter_driver_username_in_search_box(self):
        el = self.find_element(*MenuPageLocators.ADD_DRIVER_SEARCH_BOX)
        el.click()
        el.send_keys('Johnny7')
        self.hide_keyboard()

    def click_1st_dropdown_adding_button(self):
        self.find_element(*MenuPageLocators.ADD_DRIVER_BUTTON_1ST).click()

    def click_delete_driver_button(self):
        self.find_element(*MenuPageLocators.DELETE_A_FAVORITE_DRIVER).click()

    def cancel_or_remove(self, remove=False):
        if remove==True:
            self.find_element(*MenuPageLocators.REMOVE_FAVORITE_DRIVER_YES).click()

        else:
            self.find_element(*MenuPageLocators.CANCEL_REMOVE_FAVORITE_DRIVER).click()

    def click_request_button_from_1st_driver(self):
        # self.find_element(*MenuPageLocators.ASK_FOR_REQUEST_1ST_DRIVER).click()
        position1 = [(910,870)]
        position2 = [(910,1500)]


    def click_pickup_location_box(self):
        self.find_element(*MenuPageLocators.REQUEST_PICKUP_LOCATION).click()

    def enter_pickup_location(self):
        el = self.find_element(*MapPageLocators.SEARCH_BOX)
        el.click()
        el.send_keys('130-30 31 St Ave')
        self.hide_keyboard()

    def click_location_1st_dropdown(self):
        try:
            self.find_element(*MapPageLocators.LOCATION_1ST_DROPDOWN).click()
        except:
            self.click_location_1st_dropdown()

    def click_destination_location_box(self):
        self.find_element(*MenuPageLocators.REQUEST_DESTINATION).click()

    def enter_destination_location(self):
        el = self.find_element(*MapPageLocators.SEARCH_BOX)
        el.click()
        el.clear()
        el.send_keys('Corner 28')
        self.hide_keyboard()

    def click_cancel_or_request_submit_button(self, request=False):
        if request==True:
            self.find_element(*MenuPageLocators.REQUEST_SUBMIT_BTN).click()

        else:
            self.find_element(*MenuPageLocators.CANCEL_REQUEST).click()