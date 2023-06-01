import time

from selenium.webdriver.common.by import By
from pom_pytest_model.base.basepage import BasePage


class One(BasePage):

    a_loc = (By.XPATH, 'xxx')
    b_loc = (By.XPATH, 'xx')
    c_loc = (By.XPATH, 'xx')
    d_loc = (By.XPATH, 'x')

    def enter(self):
        self.click_element(One.a_loc)

    def create(self, code):
        self.send_key(One.b_loc, "test" + self.get_now())
        self.send_key(One.c_loc, code)

    def edit(self,):
        self.click_element(One.d_loc)
        self.driver.quit()
