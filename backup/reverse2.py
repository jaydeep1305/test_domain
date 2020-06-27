import re
import time
import json
import requests
import random
from loguru import logger
from init import *
try:
    from http.cookiejar import LWPCookieJar
except ImportError:
    from cookielib import LWPCookieJar


anyid = "35857df0-b8a8-4468-751a-9209bb9b6a7c"
subscriptions_id = "69da4e2-9ef8-4f8c-954a-3380fc47ecb0"

registe_obj = Register(CAPTCHA_API,SITE_KEY_RECAPTCHA,DOMAIN_NAME)

captcha_response = ""
captcha_response = registe_obj.captcha_request()

session = requests.Session()
session.cookies = LWPCookieJar('cookiejar')

cookies = {
    'YSB_ELEVATED_PRIVACY':'false',
    'LV':'1.2&idm=1',
    'CONSENT':'11111.1593036582106',
    'anyid':anyid,
    '_pin_unauth':'dWlkPU1URTVNRFJqTmprdE1UTmhOeTAwTUdRekxXRXhabVV0Tm1JM05qWTVOVFE0T1RWag',
    'A3':'d=AQABBA6X814CEKH-o_p9ZcWoV0EGx-YaK3IFEgEBAQHo9F79XgAAAAAA_SMAAAcIDpfzXuYaK3I&S=AQAAAulj0DEWfi_9nk11JG9djT8',
    'B':'74aoqspff75oe&b=3&s=s8',
    '_mkto_trk':'id:986-MCG-755&token:_mch-yahoo.com-1593022224105-89202',
    '_ce.s':'v~UHeC_xAIxdFkEQ00Ryylceqtn1U~ir~1',
    '_uetsid':'03119019-576b-62eb-a30c-54192c719f25',
    '_uetvid':'35484e1c-c601-cc71-fc3c-97c7fc02da6a'
}
headers = {
    'Host': 'smallbusiness.yahoo.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://smallbusiness.yahoo.com',
    'Referer': 'https://smallbusiness.yahoo.com/businessmaker/payitforward',
    'Upgrade-Insecure-Requests': '1',
}
headers_cart = {
    'Host': 'smallbusiness.yahoo.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://smallbusiness.yahoo.com',
    'Referer': 'https://smallbusiness.yahoo.com/businessmaker/payitforward',
}

# Csrf Generate
response = session.get('https://smallbusiness.yahoo.com/_xhr/_proxy/api/csrf/token', headers=headers, cookies=cookies)
csrf = json.loads(response.text)["data"]["token"]

data = {"_csrf":csrf,"businessCategory":"Business Billing & Collection","businessCategoryId":"96932170","businessName":"Billing Cagex23"}
response = session.post('https://smallbusiness.yahoo.com/_xhr/_proxy/api/marketing/business/recommendations', headers=headers, cookies=cookies, json=data)

#put request to cart

data = '_csrf='+csrf+'&subscriptions=[{"id":"'+subscriptions_id+'","baseProductId":"bmaker","meta":{},"addRatePlans":[{"ratePlanId":"bmaker_t12m","productId":"bmaker","type":"base"},{"ratePlanId":"acctfree_t1m","productId":"acctfree","type":"addon"},{"ratePlanId":"wsite_t12m","productId":"wsite","type":"addon"},{"ratePlanId":"lwfree_t1m","productId":"lwfree","type":"addon"}]}]&promo=PAYITFORWARD&domainBundles=[]'
response = session.put('https://smallbusiness.yahoo.com/_xhr/_proxy/api/ordering/cart', headers=headers_cart, cookies=cookies, data=data)
session.cookies.save()

headers2 = {
    'Host': 'platform-api.yahoosmallbusiness.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json',
    'Origin': 'https://checkout.yahoosmallbusiness.com',
    'Referer': 'https://checkout.yahoosmallbusiness.com/bmcheckout/login',
    'Upgrade-Insecure-Requests': '1',
}

data = {"_csrf":csrf,"userInfo":{"firstName":"Jaydeep","lastName":"Patel","userid":"jaydeep"+str(random.randint(50,5055))+"@keepjpg.com","passwd":"Nopassword1305@","marketingConsent":"on","dataConsent":"off","agreetos":"on","bibUser":True},"bizInfo":{"businessType":"BUSINESS","name":"Billing Cagex","ownerName":"Jaydeep Patel","role":"","category":"Business Billing &amp; Collection","categoryId":"96932170","subCategory":"","subCategoryId":"","businessProfile":{"workPlace":"","emplyeeCount":"","yearsOfOperation":"","annualRevenue":"","topConcern":"NONE","howSell":"","howReserve":"","stage":"early","presenceType":""}},"addressInfo":{"address1":"","address2":"","addressType":"LOCATION","presenceType":"PHYSICAL","city":"","state":"","country":"","zipcode":""},"ysbcaptchatoken":captcha_response}
response = session.post('https://platform-api.yahoosmallbusiness.com/api/businesses/signup', headers=headers2, cookies=cookies, json=data)

headers = {
    'Host': 'checkout.yahoosmallbusiness.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://smallbusiness.yahoo.com/businessmaker/payitforward',
    'Upgrade-Insecure-Requests': '1',
}

response = session.get('https://checkout.yahoosmallbusiness.com/bmcheckout?_anyid='+anyid+'&_ga=2.54325288.1450332677.1593022216-1431927048.1593022216', headers=headers, cookies=cookies)
session.cookies.save()

# Get Paypal Url
response = session.get('https://platform-api.yahoosmallbusiness.com/api/user/payment/paypalurl?isBib=true&_csrf='+csrf, headers=headers2, cookies=cookies)
paypal_url = json.loads(response.text)["data"]["paypalUrl"]
session.cookies.save()
token = paypal_url.rsplit("=",1)[1]
logger.info(paypal_url)
logger.info('https://platform-api.yahoosmallbusiness.com/api/user/payment/paypalurl?isBib=true&_csrf='+csrf)

time.sleep(60)

response = session.get('https://checkout.yahoosmallbusiness.com/paypal-bib/redirect/path/success/confirmation/cancel/payment?token='+token, headers=headers, cookies=cookies,allow_redirects=False)
pid = re.search("pid=(.*?)&amp",response.text).group(1)
logger.info(pid)

data = {"_csrf":csrf,"paymentToken":pid,"userEntity":{}}
response = session.post('https://platform-api.yahoosmallbusiness.com/api/ordering/cart/placeorder', headers=headers2, cookies=cookies, json=data)
logger.info(response.text)


