from selenium.webdriver.common.by import By

class LoginPageLocators(object):
  SKIP_BTN      = (By.ID, 'username')
  PASSWORD      = (By.ID, 'password')
  SUBMIT_BUTTON = (By.NAME, 'submit')
  MESSAGE_LABEL = (By.XPATH,'//*[@id="log-in-main-container"]/div[2]/div/div[1]')
  ENGLISH_LANGUAGE      = (By.XPATH, '//*[@id="language"]/option[1]')
  CHINESE_LANGUAGE      = (By.XPATH, '//*[@id="language"]/option[2]')
  LANGUAGE_PICKER       = (By.ID, 'language')