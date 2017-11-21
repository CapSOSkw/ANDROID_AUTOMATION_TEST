from selenium.webdriver.common.by import By
import config
from appium import webdriver

class LoginPageLocators(object):
  SKIP_BTN = (By.XPATH, "//android.widget.TextView[@text='Skip']")
  USERNAME = (By.XPATH, "//android.widget.EditText[@index='0' and @text='Username/Email']")
  PASSWORD = (By.XPATH, "//android.widget.EditText[@index='1']")
  LOGIN_BTN = (By.XPATH, "//android.widget.Button[@index='0']")
  NOTIFICATION_YES = (By.XPATH, "//android.widget.Button[@text='Allow']")

class MenuPageLocators(object):
  ############################################FLIGHT CHECK LOCATORS###############################################################
  FLIGHT_CHECK_MENU = (By.XPATH, "//android.widget.CheckedTextView[@text='Flight Check']")
  FLIGHT_CHECK_BTN = (By.XPATH, "//android.widget.Button[@text='Check']")
  FLIGHT_CHECK_CALENDAR = (By.XPATH, "//android.widget.ImageButton[contains(@resource-id, 'select_flight_date_flightCheckActivity')]")
  FLIGHT_CHECK_AIRLINE = (By.XPATH, "//android.widget.EditText[@text='Airline']")
  FLIGHT_CHECK_AIRLINE_NUMBER = (By.XPATH, "//android.widget.EditText[@text='Number']")
  FLIGHT_CHECK_CALENDAR_OK_BTN = (By.XPATH, "//android.widget.Button[@text='OK']")
  FLIGHT_CHECK_CALENDAR_CANCEL_BTN = (By.XPATH, "//android.widget.Button[@text='Cancel']")
  FLIGHT_CHECK_ARRIVAL_AIRPORT = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'arrival_airport')]")
  ###########################################PROFILE LOCATORS######################################################################
  IMAGE_PROFILE_MENU = (By.XPATH, "//android.widget.ImageView[contains(@resource-id, 'profile_image_nav_header')]")
  PROFILE_QR_CODE = (By.XPATH, "//android.widget.TextView[@content-desc='QR Code']")
  PROFILE_QR_CODE_CANCEL = (By.XPATH, "//android.widget.Button[@text='Cancel' and @index='0']")
  PROFILE_USERNAME_BOX = (By.XPATH, "//android.widget.EditText[@index='2']")
  PROFILE_FIRSTNAME_BOX = (By.XPATH, "//android.widget.EditText[@index='3']")
  PROFILE_LASTNAME_BOX = (By.XPATH, "//android.widget.EditText[@index='4']")
  PROFILE_SAVE_BTN = (By.XPATH, "//android.widget.TextView[@content-desc='Save' and @index='1']")
  ###########################################MY TRIPS LOCATORS#####################################################################
  MY_TRIP_MENU = (By.XPATH, "//android.widget.CheckedTextView[@text='My Trips']")
  SWITCH_TO_PAST_TRIP = (By.XPATH, "//android.widget.TextView[@text='PAST TRIPS']")
  SWITCH_TO_UPCOMING_TRIP = (By.XPATH, "//android.widget.TextView[@text='UPCOMING TRIPS']")
  THE_LASTEST_TRIP = (By.XPATH, "//android.widget.RelativeLayout[@index='0']")
  ADD_DRIVER_TO_FACORITE_BTN = (By.XPATH, "//android.widget.Button[@text='Add Favorite']")
  BLOCK_DRIVER_BTN = (By.XPATH, "//android.widget.Button[@text='Block Driver']")
  REPORT_LOST_ITEM = (By.XPATH, "//android.widget.Button[@text='Report lost item']")
  REPORT_TITLE = (By.XPATH, "//android.widget.EditText[@index='0']")
  REPORT_DESCRIPTION = (By.XPATH, "//android.widget.EditText[@index='1']")
  REPORT_CANCEL_BTN = (By.XPATH, "//android.widget.Button[@index='0']")
  REPORT_REPORT_BTN = (By.XPATH, "//android.widget.Button[@index='1']")
  YES_BUTTON = (By.XPATH, "//android.widget.Button[@text='YES']")
  NO_BUTTON = (By.XPATH, "//android.widget.Button[@text='NO']")
################################################FAVORITE DRIVERS MENU LOCATORS########################################################
  FAVORITE_DRIVERS_MENU = (By.XPATH, "//android.widget.CheckedTextView[@text='Favorite Drivers']")
  ADD_A_NEW_FAVORITE_DRIVER = (By.XPATH, "//android.widget.ImageView[@index='2']")
  DELETE_A_FAVORITE_DRIVER = (By.XPATH, "//android.widget.ImageButton[contains(@resource-id, 'button_delete_item_favorite_driver')]")
  ASK_FOR_REQUEST_1ST_DRIVER = (By.XPATH, "//(android.widget.Button[contains(@resource-id, 'button_request_item_favorite_driver')]")
  ADD_DRIVER_SEARCH_BOX = (By.XPATH, "//android.widget.EditText[@text='Search']")
  ADD_DRIVER_BUTTON_1ST = (By.XPATH, "//android.widget.ImageButton[contains(@resource-id, 'button_send_request_item_search_driver')]")
  REMOVE_FAVORITE_DRIVER_YES = (By.XPATH, "//android.widget.Button[@text='REMOVE']")
  CANCEL_REMOVE_FAVORITE_DRIVER = (By.XPATH, "//android.widget.Button[@text='Cancel']")
  REQUEST_PICKUP_LOCATION = (By.XPATH, "//android.widget.Button[@text='Pickup location'")
  REQUEST_DESTINATION = (By.XPATH, "//android.widget.Button[@text='Destination']")
  REQUEST_YOUR_FARE_OFFER = (By.XPATH, "//android.widget.EditText[@text='Your fare offer']")
  SELECT_PAYMENT_METHOD = (By.XPATH, "//android.widget.RelativeLayout[@index='4']/android.widget.TextView[@index='1']")
  SELECT_PROMOTION_CODE = (By.XPATH, "//android.widget.TextView[@text='Promotion Code']")
  REQUEST_SUBMIT_BTN = (By.XPATH, "//android.widget.Button[@text='Request']")
  CANCEL_REQUEST = (By.XPATH, "//android.widget.ImageView[@index='1']")
######################################SETTING LOCATORS############################################################
  SETTINGS_BUTTON_MENU = (By.XPATH, "//android.widget.CheckedTextView[@text='Settings']")

  DRIVER_PREFERENCES = (By.XPATH, "//android.widget.TextView[@text='Driver Preferences']")
  PREFER_FAVORITE_DRIVER_OFF = (By.XPATH, "//android.widget.Switch[contains(@resource-id, 'prefer_fav_driver_driver_preference') and @text='OFF']")
  PREFER_FAVORITE_DRIVER_ON = (By.XPATH, "//android.widget.Switch[contains(@resource-id, 'prefer_fav_driver_driver_preference') and @text='ON']")
  WHEELCHAIR_ASSISTANCE_OFF = (By.XPATH, "//android.widget.Switch[contains(@resource-id, 'wheelchair_driver_preference') and @text='OFF']")
  WHEELCHAIR_ASSISTANCE_ON = (By.XPATH, "//android.widget.Switch[contains(@resource-id, 'wheelchair_driver_preference') and @text='ON']")
  SELECT_DRIVER_GENDER = (By.XPATH, "//android.widget.FrameLayout[@index='0']/android.widget.Spinner[@index='0']")
  SELECT_DRIVER_LANGUAGE = (By.XPATH, "//android.widget.FrameLayout[@index='1']/android.widget.Spinner[@index='0']")
  SELECT_DRIVING_EXPERIENCE = (By.XPATH, "//android.widget.FrameLayout[@index='2']/android.widget.Spinner[@index='0']")
  SELECT_VEHICLE_BRAND = (By.XPATH, "//android.widget.FrameLayout[@index='3']/android.widget.Spinner[@index='0']")
  SELECT_COUNTRY_ORIGIN = (By.XPATH, "//android.widget.FrameLayout[@index='4']/android.widget.Spinner[@index='0']")
  DRIVER_PREFERENCE_SAVE_BUTTON = (By.XPATH, "//android.widget.Button[contains(@resource-id, 'save_driver_preference')]")

  EDIT_PROFILE = (By.XPATH, "//android.widget.TextView[@text='Edit Profile']")

  CHANGE_PASSWORD = (By.XPATH, "//android.widget.TextView[@text='Change Password']")

  LANGUAGE = (By.XPATH, "//android.widget.TextView[@text='Language']")
  LANGUAGE_TO_ENGLISH = (By.XPATH, "//android.widget.FrameLayout[@index='0']/android.widget.LinearLayout/android.widget.CheckBox[contains(@resource-id, 'english_language')]")
  LANGUAGE_TO_CHINESE = (By.XPATH, "//android.widget.FrameLayout[@index='1']/android.widget.LinearLayout/android.widget.CheckBox[contains(@resource-id, 'chinese_language')]")

  SIGN_OUT = (By.XPATH, "//android.widget.TextView[@text='Sign Out']")
  SIGN_OUT_CANCEL = (By.XPATH, "//android.widget.Button[@text='Cancel']")
  SIGN_OUT_YES = (By.XPATH, "//android.widget.Button[@text='SIGN OUT']")


class MapPageLocators(object):
  DESTINATION_BOX = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'destination_location_addressFragment')]")
  CURRENT_LOCATION_BTN = (By.XPATH, "//android.widget.ImageButton[contains(@resource-id, 'current_location_addressFragment')]")
  PICKUP_LOCATION_BOX = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'pickup_location_addressFragment')]")
  ESTIMATED_TIME =  (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'estimated_time_pickupLocationPinFragment')]")
  MENU_BTN = (By.XPATH, "//android.widget.ImageButton[@index='0']")
  CLEAR_SEARCH_BOX = (By.XPATH, "//android.widget.ImageButton[contains(@resource-id, 'clear_field_searchPlacesFragment')]")
  SWITCH_TO_SEARCH = (By.XPATH, "//android.widget.TextView[@index='0' and @text='Search']")
  SWITCH_TO_FAVORITE = (By.XPATH, "//android.widget.TextView[@index='0' and @text='Favorite']")
  SEARCH_BOX = (By.XPATH, "//android.widget.EditText[contains(@resource-id, 'search_field_searchPlacesFragment')]")
  LOCATION_1ST_DROPDOWN = (By.XPATH, "//android.widget.FrameLayout[@index='0']/android.widget.TextView[@index='0']")
  STAR_DESTINATION = (By.XPATH, "//android.widget.LinearLayout[@index='2']/android.widget.ImageButton[@index='1']")
  ORDER_NOW_BUTTON = (By.XPATH, "//android.widget.LinearLayout[@index='1']/android.widget.Button[@index='0']")
  RESERVE_TRIP_BUTTON = (By.XPATH, "//android.widget.LinearLayout[@index='1']/android.widget.Button[@index='1']")
  SELECT_VEHICLE = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'vehicle_name')]")
  REQUEST_RIDE_BTN = (By.XPATH, "//android.widget.Button[@text='Request Ride']")

