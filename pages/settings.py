# -*- coding: utf-8 -*-
from locators.locators import *
from .base import BasePage
import config
import time,random
import numpy as np
import requests
from appium.webdriver.common.touch_action import TouchAction


class SettingsPage(BasePage):
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

    def click_setting_menu_button(self):
        self.find_element(*MenuPageLocators.SETTINGS_BUTTON_MENU).click()

    def verify_setting_options(self):
        self.find_element(*MenuPageLocators.DRIVER_PREFERENCES)
        self.find_element(*MenuPageLocators.SIGN_OUT)
        self.find_element(*MenuPageLocators.LANGUAGE)

    def click_sign_out_button(self):
        self.find_element(*MenuPageLocators.SIGN_OUT).click()

    def cancel_or_sign_out(self, out=False):
        if out==True:
            self.find_element(*MenuPageLocators.SIGN_OUT_YES).click()

        else:
            self.find_element(*MenuPageLocators.SIGN_OUT_CANCEL).click()

    def click_edit_profile_button(self):
        self.find_element(*MenuPageLocators.EDIT_PROFILE).click()

    def click_driver_preferences(self):
        self.find_element(*MenuPageLocators.DRIVER_PREFERENCES).click()

    def verify_driver_preference_elements(self):
        self.find_element(*MenuPageLocators.SELECT_DRIVER_GENDER)
        self.find_element(*MenuPageLocators.SELECT_DRIVER_LANGUAGE)
        self.find_element(*MenuPageLocators.SELECT_COUNTRY_ORIGIN)
        self.find_element(*MenuPageLocators.DRIVER_PREFERENCE_SAVE_BUTTON)

    def prefer_favorite_driver(self, on=False):
        if (on==True):
            try:
                self.find_element(*MenuPageLocators.PREFER_FAVORITE_DRIVER_OFF).click()

            except:
                pass

        if (on==False):
            try:
                self.find_element(*MenuPageLocators.PREFER_FAVORITE_DRIVER_ON).click()

            except:
                pass

    def wheelchair_assistance(self, on=False):
        if (on==True):
            try:
                (self.find_element(*MenuPageLocators.WHEELCHAIR_ASSISTANCE_OFF).click())
            except:
                pass

        if (on==False):
            try:
                self.find_element(*MenuPageLocators.WHEELCHAIR_ASSISTANCE_ON).click()
            except:
                pass

    def select_driver_gener(self):
        index = random.choice([0,1,2])
        self.find_element(*MenuPageLocators.SELECT_DRIVER_GENDER).click()
        OPTIONS_GENDER = (By.XPATH, "//android.widget.CheckedTextView[@index='"+ str(index) + "']")
        self.find_element(*OPTIONS_GENDER).click()

    def select_driver_language(self):
        index = random.choice(np.arange(0,6))
        self.find_element(*MenuPageLocators.SELECT_DRIVER_LANGUAGE).click()
        OPTIONS_LANGUAGE = (By.XPATH, "//android.widget.CheckedTextView[@index='"+ str(index) + "']")
        self.find_element(*OPTIONS_LANGUAGE).click()

    def select_driving_exp(self):
        index = random.choice(np.arange(0,5))
        self.find_element(*MenuPageLocators.SELECT_DRIVING_EXPERIENCE).click()
        OPTIONS_EXP = (By.XPATH, "//android.widget.CheckedTextView[@index='"+ str(index) + "']")
        self.find_element(*OPTIONS_EXP).click()

    def select_vehicle_brand(self):
        index = random.choice(np.arange(0,8))
        self.find_element(*MenuPageLocators.SELECT_VEHICLE_BRAND).click()
        OPTIONS_BRAND = (By.XPATH, "//android.widget.CheckedTextView[@index='"+ str(index) + "']")
        self.find_element(*OPTIONS_BRAND).click()

    def select_country_origin(self):
        index = random.choice(np.arange(0, 9))
        self.find_element(*MenuPageLocators.SELECT_COUNTRY_ORIGIN).click()
        OPTIONS_COUNTRY = (By.XPATH, "//android.widget.CheckedTextView[@index='"+ str(index) + "']")
        self.find_element(*OPTIONS_COUNTRY).click()

    def click_driver_prefenerce_save_button(self):
        self.find_element(*MenuPageLocators.DRIVER_PREFERENCE_SAVE_BUTTON).click()

    def click_language_button(self):
        self.find_element(*MenuPageLocators.LANGUAGE).click()

    def click_language_english(self):
        self.find_element(*MenuPageLocators.LANGUAGE_TO_ENGLISH).click()

    def click_language_chinese(self):
        self.find_element(*MenuPageLocators.LANGUAGE_TO_CHINESE).click()

    def verify_switch_to_chinese_succeed(self):
        self.click_menu_button()
        HISTORY = (By.XPATH, "//android.widget.CheckedTextView[@index='0' and @text='历史']")
        self.find_element(*HISTORY)

    def verify_switch_to_english_succeed(self):
        self.back_to_homepage()
        self.click_menu_button()
        MYTRIP = (By.XPATH, "//android.widget.CheckedTextView[@index='0' and @text='My Trips']")
        self.find_element(*MYTRIP)

    def switch_to_english_as_main_language(self):
        try:
            self.verify_switch_to_english_succeed()
            self.back_to_homepage()

        except:
            self.back_to_homepage()
            self.click_menu_button()
            self.click_setting_menu_button()
            self.click_language_button()
            self.click_language_english()
            self.verify_switch_to_english_succeed()
            self.back_to_homepage()