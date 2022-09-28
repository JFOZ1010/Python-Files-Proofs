from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class GooglePage(object):
    def __init__(self, driver):
        self._driver = driver
        self._url = 'http://www.google.com'
        self.search_locator = 'q'

    @property
    def is_loaded(self):
        WebDriverWait(self._driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
        return True

    @property
    def keyboard(self):
        input_field = self._driver.find_element(by="name", value='q')
        return input_field.get_attribute('value')

    def open(self):
        self._driver.get(self._url)

    def type_search(self, keyboard):
        input_field = self._driver.find_element(by="name", value='q')
        input_field.send_keys(keyboard)
    
    def click_submit(self):
        input_field = self._driver.find_element(by="name", value='q')
        input_field.submit()

    def search(self, keyboard):
        self.type_search(keyboard)
        self.click_submit()
    
    

