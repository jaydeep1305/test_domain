import time
import json
from init import *


# captcha_response = ""
registe_obj = Register(CAPTCHA_API,SITE_KEY_RECAPTCHA,DOMAIN_NAME)
# captcha_response = registe_obj.captcha_request()
# if registe_obj.register(captcha_response):
#     time.sleep(20)
#     login_link = registe_obj.check_mail()
#     logger.info(login_link)
login_link = "https://login.yahoosmallbusiness.com/activate?sign=cfkAHNmeQ05w5YEL8H8BLbrx9mLVckbG2tyPOedluMG75wc_Yaa5uXURnaukei6e4GsFTdGtrSqfiPz9T1wqoKCtYK_8K-Dv3k0l3SHgZY-pwyUtmwXr2CR1yGY30MyEXlIuws5saprPCSMcTsKx3eMIni4DsSV61eCjaRlWb05MyLCF6KAsJRIf59sMIjRpBDjPg4Q1YnnGWqrMzwvliLCRBBqrq6GgukFZMUl8lZYIyXokCTQofdTikJjw-R51"
captcha_response = registe_obj.captcha_request(SITE_KEY_RECAPTCHA_LOGIN)
registe_obj.login(captcha_response,login_link)
