import os
import unittest
from appium import webdriver
from time import sleep
global driver

def before_all(context):
	desired_caps = {}
	desired_caps['platformName'] = 'Android'
	desired_caps['platformVersion'] = '8.0' #8.0
	desired_caps['deviceName'] = 'Pixel1'   #Pixel1
	# desired_caps['app'] = os.path.join(
	# 	"C:\\Users\\EMamerto\\Desktop\\android_automation\\",
	# 	"app-dev.apk")
	desired_caps['app'] = os.path.join(
		"/Users/KeyuanWu/Desktop/Mobile_Automation_Test/",
		"app-dev.apk")
	desired_caps['automationName'] = 'uiautomator2'
	desired_caps['appPackage'] = 'com.operr.operr'
	desired_caps['appActivity'] = 'com.operr.operr.Splash'
	context.driver = webdriver.Remote(
		'http://localhost:4723/wd/hub', desired_caps)

def after_all(context):
	context.driver.quit()
	
