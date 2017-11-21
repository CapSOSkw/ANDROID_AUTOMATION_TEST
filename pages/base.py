from appium import webdriver
from locators.locators import *
import config
import time


class BasePage(object):
    def __init__(self, context):
        self.driver = context.driver
 
    def find_element(self, *locator):
        self.driver.implicitly_wait(5)
        time.sleep(2)
        return self.driver.find_element(*locator)

    def hide_keyboard(self):
        return self.driver.hide_keyboard()

    def send_keyz(self, element, keyz):
        element.send_keys(keyz)
        self.hide_keyboard()

    def android_back(self):
        self.driver.back()

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

    def click_menu_button(self):
        try:
            self.verify_if_on_menu_list()
        except:

            self.find_element(*MapPageLocators.MENU_BTN).click()

    def verify_if_on_menu_list(self):
        self.find_element(*MenuPageLocators.MY_TRIP_MENU)
        self.find_element(*MenuPageLocators.FAVORITE_DRIVERS_MENU)
        self.find_element(*MenuPageLocators.FLIGHT_CHECK_MENU)




    """
    This function checks to see if user is already logged in.
    """
    # def check_if_logged_in(self):
		# try:
		# 	self.find_element(*MapPageLocators.DESTINATION)
		# except:
		# 	"""
		# 	Splash Page Click Skip Button
		# 	"""
		# 	self.find_element(*LoginPageLocators.SKIP_BTN).click()
		# 	"""
		# 	Username is entered
		# 	"""
		# 	username = self.find_element(*LoginPageLocators.USERNAME)
		# 	username.click()
		# 	username.send_keys(config.default_user)
		# 	self.hide_keyboard()
		# 	"""
		# 	Password is entered
		# 	"""
		# 	password = self.find_element(*LoginPageLocators.PASSWORD)
		# 	password.click()
		# 	password.send_keys(config.default_pword)
		# 	self.hide_keyboard()
		# 	"""
		# 	Login button is clicked
		# 	"""
		# 	self.find_element(*LoginPageLocators.LOGIN_BTN).click()
		# 	"""
		# 	Verify if user is really logged in
		# 	"""
		# 	self.find_element(*MapPageLocators.DESTINATION)
		# 	time.sleep(10)