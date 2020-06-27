import time 
import json
from loguru import logger
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class Paypal:

    def verification(self,url):
        logger.debug("paypal requested .... ")
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.set_headless()
        driver = webdriver.Firefox(firefox_options=fireFoxOptions)
        driver.get("https://www.paypal.com/smartchat/open/eligibility")
        file = open("paypal-cookie.json")
        cookies = json.loads(file.read())
        for cookie in cookies:
            # logger.info(cookie)
            driver.add_cookie(cookie)
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#confirmButtonTop")))
        time.sleep(10)
        flag = False
        try:
            driver.execute_script("document.getElementById('preloaderSpinner').remove()")
        except Exception as ex:
            pass

        try:
            driver.execute_script("document.getElementById('spinner').remove()")
            driver.execute_script("document.getElementById('spinner').remove()")
        except Exception as ex:
            pass

        try:
            driver.execute_script("document.getElementById('confirmButtonTop').click()")
            flag = True
        except Exception as ex:
            pass

        try:
            driver.find_element_by_id('confirmButtonTop').click()
            flag = True
        except Exception as ex :
            pass

        try:
            driver.find_element_by_id('confirmButtonTop').click()
            flag = True
        except Exception as ex :
            pass
        finally :
            driver.quit()
    
        if flag:
            logger.info("Paypal Verified.")
        else :
            logger.error("Paypal Error")
        
        return flag
