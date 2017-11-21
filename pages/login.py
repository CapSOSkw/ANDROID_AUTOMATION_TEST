from locators.locators import *
from .base import BasePage
import unittest
import time
from time import sleep
from appium import webdriver
import sys,json,re,argparse



class LoginPage(BasePage):

	def __init__(self, context):
		BasePage.__init__(self, context)

	def wait_time(self):
		time.sleep(3)

	def verify_login_page(self):
		try:
			self.find_element(*LoginPageLocators.SKIP_BTN).click()
		except:
			pass
		#assert is on login page


	def enter_username(self):
		username = self.find_element(*LoginPageLocators.USERNAME)
		# username = self.driver.find_element_by_xpath("//android.widget.EditText[@index='0']")
		username.click()
		username.send_keys('keyuan')
		self.driver.hide_keyboard()


	def enter_password(self):
		password = self.find_element(*LoginPageLocators.PASSWORD)
		password.click()
		password.send_keys('123456')
		self.hide_keyboard()

	def click_login_btn(self):
		self.find_element(*LoginPageLocators.LOGIN_BTN).click()
		# self.driver.find_element_by_xpath("android.widget.Button[@text='LogIn']").click()


	def click_notification_submit(self):
		try:
			while(self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button")):
				self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
				sleep(1)
		except:
			pass


	def verify_logged_in(self):
		self.find_element(*MapPageLocators.DESTINATION_BOX)
		self.find_element(*MapPageLocators.CURRENT_LOCATION_BTN)
		self.find_element(*MapPageLocators.PICKUP_LOCATION_BOX)
		self.find_element(*MapPageLocators.MENU_BTN)


	def click_android_back_button(self):
		self.android_back()

	def check_if_user_is_logged_in(self):
		try:
			self.verify_logged_in()

		except:
			self.verify_login_page()
			self.enter_username()
			self.enter_password()
			self.click_login_btn()
			self.click_notification_submit()
			self.verify_logged_in()