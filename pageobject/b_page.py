import time

from selenium.webdriver.common.by import By
from pom_pytest_model.base.basepage import BasePage


class Two(BasePage):

    a_loc = (By.XPATH, 'xxx')
    b_loc = (By.XPATH, 'xx')

    def enter(self):
        self.click_element(Two.a_loc)

    def create(self, history):
        self.click_element(Two.b_loc)
        self.driver.quit()
