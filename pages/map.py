from locators.locators import *
from .base import BasePage
import config
import time
import requests
from appium.webdriver.common.touch_action import TouchAction


class MapPage(BasePage):

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

	def click_current_location_btn(self):
		self.find_element(*MapPageLocators.CURRENT_LOCATION_BTN).click()

	def click_pickup_location_box(self):
		el = self.find_element(*MapPageLocators.PICKUP_LOCATION_BOX)
		action = TouchAction(self.driver)
		action.tap(el).perform()

	def enter_pickup_location(self):
		el = self.find_element(*MapPageLocators.SEARCH_BOX)
		el.click()
		el.clear()
		el.send_keys('130-30 31 St Ave')
		self.hide_keyboard()

	def click_location_1st_dropdown(self):
		try:
			self.find_element(*MapPageLocators.LOCATION_1ST_DROPDOWN).click()
		except:
			self.click_location_1st_dropdown()


	def click_destination_location_box(self):
		self.find_element(*MapPageLocators.DESTINATION_BOX).click()

	def enter_destination_location(self):
		el = self.find_element(*MapPageLocators.SEARCH_BOX)
		el.click()
		el.clear()
		el.send_keys('Corner 28')
		self.hide_keyboard()

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


	def see_preschedule_route(self):
		self.find_element(*MapPageLocators.ORDER_NOW_BUTTON)
		self.find_element(*MapPageLocators.RESERVE_TRIP_BUTTON)
		self.find_element(*MapPageLocators.STAR_DESTINATION)

	def star_destination(self):
		self.find_element(*MapPageLocators.STAR_DESTINATION).click()

	def click_order_or_reserve(self,reserve=False):
		if reserve==True:
			self.find_element(*MapPageLocators.RESERVE_TRIP_BUTTON).click()
		else:
			self.find_element(*MapPageLocators.ORDER_NOW_BUTTON).click()

	def click_vehicle_type(self):
		self.find_element(*MapPageLocators.SELECT_VEHICLE).click()

	def click_request_ride_button(self):
		self.find_element(*MapPageLocators.REQUEST_RIDE_BTN).click()

	def click_my_trips(self):
		self.find_element(*MenuPageLocators.MY_TRIP_MENU).click()

	def verify_my_trips_elements(self):
		self.find_element(*MenuPageLocators.SWITCH_TO_PAST_TRIP)
		self.find_element(*MenuPageLocators.SWITCH_TO_UPCOMING_TRIP)

	def click_the_lastest_trip(self):
		self.find_element(*MenuPageLocators.THE_LASTEST_TRIP).click()

	def verify_the_lastest_trip_elements(self):
		self.find_element(*MenuPageLocators.REPORT_LOST_ITEM)
		self.find_element(*MenuPageLocators.ADD_DRIVER_TO_FACORITE_BTN)

	def favorite_or_block_driver(self,block=False):
		if block==True:
			self.find_element(*MenuPageLocators.BLOCK_DRIVER_BTN).click()

		else:
			self.find_element(*MenuPageLocators.ADD_DRIVER_TO_FACORITE_BTN).click()

	def yes_or_no_buttons(self, no=False):
		if no==True:
			self.find_element(*MenuPageLocators.NO_BUTTON).click()

		else:
			self.find_element(*MenuPageLocators.YES_BUTTON).click()

	def click_report_lost_item(self):
		self.find_element(*MenuPageLocators.REPORT_LOST_ITEM).click()

	def enter_report_title(self, title):
		el = self.find_element(*MenuPageLocators.REPORT_TITLE)
		el.click()
		el.send_keys(title)
		self.hide_keyboard()

	def enter_report_description(self, des):
		el = self.find_element(*MenuPageLocators.REPORT_DESCRIPTION)
		el.click()
		el.send_keys(des)
		self.hide_keyboard()

	def cancel_or_report(self,cancel=False):
		if cancel==True:
			self.find_element(*MenuPageLocators.REPORT_CANCEL_BTN).click()

		else:
			self.find_element(*MenuPageLocators.REPORT_REPORT_BTN).click()