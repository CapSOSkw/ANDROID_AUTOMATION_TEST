from locators.locators import *
from .base import BasePage
import config
import time
from datetime import datetime,timedelta,date
from dateutil.relativedelta import relativedelta
import random
import requests

class FlightPage(BasePage):
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

    def click_flight_check_menu_btn(self):
        self.find_element(*MenuPageLocators.FLIGHT_CHECK_MENU).click()

    def verify_in_flight_check(self):
        self.find_element(*MenuPageLocators.FLIGHT_CHECK_BTN)

    def click_flight_check_calendar(self):
        self.find_element(*MenuPageLocators.FLIGHT_CHECK_CALENDAR).click()

    def enter_flight_airline(self, airline):
        el = self.find_element(*MenuPageLocators.FLIGHT_CHECK_AIRLINE)
        el.click()
        el.send_keys(airline)
        self.hide_keyboard()

    def enter_flight_airline_number(self, number):
        el = self.find_element(*MenuPageLocators.FLIGHT_CHECK_AIRLINE_NUMBER)
        el.click()
        el.send_keys(number)
        self.hide_keyboard()

    def click_calendar_ok_button(self):
        self.find_element(*MenuPageLocators.FLIGHT_CHECK_CALENDAR_OK_BTN).click()

    def click_flight_check_button(self):
        self.find_element(*MenuPageLocators.FLIGHT_CHECK_BTN).click()

    def verify_flight_check_result(self):
        self.find_element(*MenuPageLocators.FLIGHT_CHECK_ARRIVAL_AIRPORT)

    def random_choose_day_before_or_after(self):
        today = date.today()
        value = random.choice([-3,-2,-1,0,1,2])
        d = date(today.year, today.month, today.day) + relativedelta(days=value)
        day = d.strftime("%d %B %Y")
        random_date = (By.XPATH, "//android.view.View[@content-desc= '" + day + "']")
        try:
            self.find_element(*random_date).click()
        except:
            pass