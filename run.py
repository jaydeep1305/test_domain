import time
import json
import threading
from init import *
from bounded_pool_executor import BoundedProcessPoolExecutor

def thread(anyid):
    try:
        if len(anyid) > 5:
	        paypal_obj = Paypal()
	        registe_obj = Register(CAPTCHA_API,SITE_KEY_RECAPTCHA,DOMAIN_NAME,paypal_obj)
	        captcha_response = registe_obj.captcha_request()
       		registe_obj.register(captcha_response,anyid)

    except Exception as ex:
        logger.error(ex)


f = open("anyids.txt", "r")
anyids = f.read()
anyids = anyids.split("\n")
threads = []
worker = BoundedProcessPoolExecutor(max_workers=2)
j = 1000
i = 0
while True:
    anyid = anyids[i]
    t1 = worker.submit(thread,anyid)
    logger.info(anyid)
    i += 1
    if i >= len(anyids) - 1 :
        i = 0

    j -= 1
    if j <= 0 : 
        break
