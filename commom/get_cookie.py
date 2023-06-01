import json
import os
from selenium import webdriver
import time
from data.object_path import boe, cookie_as


# print(os.path.dirname(__file__))
# options = webdriver.ChromeOptions()
# options.add_argument('requests_header')
# driver = webdriver.Chrome(options=options)

driver = webdriver.Chrome()
driver.get(boe)
time.sleep(15)
with open(cookie_as, 'w') as f:
    f.write(json.dumps(driver.get_cookies()))



