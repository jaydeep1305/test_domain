import csv
import time
import json
import threading
from init import *

while True:
    try :
        login_obj = Login(CAPTCHA_API,SITE_KEY_RECAPTCHA,IMAP_SERVER,IMAP_USER,IMAP_PASS,IMAP_FOLDER)
        login_link = login_obj.check_mail()
        logger.info(login_link)
        captcha_response = login_obj.captcha_request(SITE_KEY_RECAPTCHA_LOGIN)
        login_obj.login(captcha_response,login_link)
    except Exception as ex:
        logger.error(ex)