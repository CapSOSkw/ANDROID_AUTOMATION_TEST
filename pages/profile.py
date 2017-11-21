from locators.locators import *
from .base import BasePage
import config
import time
import requests

class ProfilePage(BasePage):
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

    def click_image_profile_button_menu(self):
        self.find_element(*MenuPageLocators.IMAGE_PROFILE_MENU).click()

    def verify_in_profile_page(self):
        self.find_element(*MenuPageLocators.PROFILE_QR_CODE)
        self.find_element(*MenuPageLocators.PROFILE_USERNAME_BOX)
        self.find_element(*MenuPageLocators.PROFILE_SAVE_BTN)

    def verify_QR_code_exist(self):
        self.find_element(*MenuPageLocators.PROFILE_QR_CODE_CANCEL)
        time.sleep(2)

    def click_QR_code_button(self):
        self.find_element(*MenuPageLocators.PROFILE_QR_CODE).click()

    def click_QR_code_cancel_button(self):
        self.find_element(*MenuPageLocators.PROFILE_QR_CODE_CANCEL).click()

    def edit_username(self, username):
        el = self.find_element(*MenuPageLocators.PROFILE_USERNAME_BOX)
        el.click()
        el.clear()
        el.send_keys(username)
        self.hide_keyboard()

    def edit_firstname(self,firstname):
        config.test_data_kw['PROFILE_PAGE'][0]['FIRSTNAME'] = firstname
        el = self.find_element(*MenuPageLocators.PROFILE_FIRSTNAME_BOX)
        el.click()
        el.clear()
        el.send_keys(firstname)
        self.hide_keyboard()

    def edit_lastname(self, lastname):
        config.test_data_kw['PROFILE_PAGE'][0]['LASTNAME'] = lastname
        el = self.find_element(*MenuPageLocators.PROFILE_LASTNAME_BOX)
        el.click()
        el.clear()
        el.send_keys(lastname)
        self.hide_keyboard()

    def click_profile_save_button(self):
        self.find_element(*MenuPageLocators.PROFILE_SAVE_BTN).click()

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

    def verify_save_succeed(self):
        self.back_to_homepage()
        self.click_menu_button()
        time.sleep(2)
        self.click_image_profile_button_menu()
        time.sleep(2)
        assert config.test_data_kw['PROFILE_PAGE'][0]['FIRSTNAME'] == self.find_element(*MenuPageLocators.PROFILE_FIRSTNAME_BOX).text
        assert config.test_data_kw['PROFILE_PAGE'][0]['LASTNAME'] == self.find_element(*MenuPageLocators.PROFILE_LASTNAME_BOX).text