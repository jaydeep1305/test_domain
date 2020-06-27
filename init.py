import os
import requests
from loguru import logger
from register import Register
from paypal import Paypal
from login import Login

CAPTCHA_API = "081908c87d8ecb5815af6ea10d53bd55"
SITE_KEY_RECAPTCHA = "6LeSLyEUAAAAAHV9Kw4-7FwgrLwEvpkPiksqgoOb"
SITE_KEY_RECAPTCHA_LOGIN = "6LfTIAgTAAAAAFdcrP4gOyUi7MPu-rBAyXuaKWhj"
DOMAIN_NAME = os.environ['DOMAIN_NAME']
IMAP_SERVER = "imap.zoho.com"
IMAP_USER = "admin@keepjpg.com"
IMAP_PASS = "memyself555"
IMAP_FOLDER = "ZMNotification"
