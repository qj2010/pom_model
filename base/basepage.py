import json
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from data.object_path import boe, cookie_as


class BasePage:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(boe)
        try:
            self.driver.set_page_load_timeout(0.5)
            self.driver.get(boe)
        except:
            self.driver.set_page_load_timeout(15)
            with open(cookie_as, 'r') as f:
                cookie_list = json.load(f)
                for cookie in cookie_list:
                    cookie.pop("domain")
                    self.driver.add_cookie(cookie)
            self.driver.get(boe)

        self.driver.implicitly_wait(20)

    def locator_element(self, loc):
        return self.driver.find_element(*loc)

    def locator_elements(self, loc):
        return self.driver.find_elements(*loc)

    def click_element(self, loc):
        self.locator_element(loc).click()

    def click_elements(self, loc, place):
        self.locator_elements(loc)[place].click()

    def send_key(self, loc, value):
        self.locator_element(loc).send_keys(value)

    def send_keys(self, loc, value, place):
        self.locator_elements(loc)[place].send_keys(value)

    def act_click(self, loc):
        ActionChains(self.driver).click(self.locator_element(loc)).perform()

    def get_now(self):
        now = time.localtime()
        return time.strftime('%m.%d', now)

