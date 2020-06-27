import time 
import json
from loguru import logger
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bounded_pool_executor import BoundedProcessPoolExecutor

class Anyid():
    def get_value(self):
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.set_headless()
        driver = webdriver.Firefox(firefox_options=fireFoxOptions)
        driver.set_page_load_timeout(10)
        try: 
            driver.get("https://smallbusiness.yahoo.com/businessmaker/payitforward")
        except Exception as ex:
            pass
        finally:
            cookies_list = driver.get_cookies()
            driver.quit()
            cookies_dict = {}
            for cookie in cookies_list:
                cookies_dict[cookie['name']] = cookie['value']
            return cookies_dict["anyid"]

def thread():
    anyid_obj = Anyid()
    print(anyid_obj.get_value())

worker = BoundedProcessPoolExecutor(max_workers=17)
while True:
    t1 = worker.submit(thread)
