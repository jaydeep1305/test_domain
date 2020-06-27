# import re
# import json
# import requests
# from loguru import logger

# session = requests.Session()
# captcha_response = "03AGdBq26YRti4CsYlcIioLje8mHZw4JH0kBwd_q3teTWR3VMsmCU-T9JH5GYdTeTDl_pBjtxr6p-5v74MpFIPdTQRlLSQjQUnWuAJU4b7XrYvcHEqSA2ItJHtJXRfQGpZL--Y5tPUdOrEVSTl-CIPCFcDCbhpjsiSp8MSmxHW8ZrT3wvLlkm56nTNdbNL2li_s-2Hs2vpg22rJneiL6um1LsG0Rj-xnti85dfJCxzI9bgPDHxSt_gFpjl2yweypj598K6Gr217SUUDMtkHmmZn3UlJwwEfzee6NBQ0C7aemxx1QFz2qht82O5uqibMtFZyZuKI6Cewejs7A2-Ypsvm6J2ZOPf1T0IOYglK8T7wLes-LgL_O9XcJZG5tMHQiNXx3_ITM6FrfWlBwwdIpgR_Bucx0O8OrSuC06bKHTBCCWeoALh2Ma-zYk"

# cookies = {
#     'YSB_ELEVATED_PRIVACY':'false',
#     'LV':'1.2&idm=1',
#     'CONSENT':'11111.1593036582106',
#     'anyid':'96af01ea-22da-4887-94f2-ec623dd804b1',
#     '_pin_unauth':'dWlkPU1URTVNRFJqTmprdE1UTmhOeTAwTUdRekxXRXhabVV0Tm1JM05qWTVOVFE0T1RWag',
#     'A3':'d=AQABBA6X814CEKH-o_p9ZcWoV0EGx-YaK3IFEgEBAQHo9F79XgAAAAAA_SMAAAcIDpfzXuYaK3I&S=AQAAAulj0DEWfi_9nk11JG9djT8',
#     'B':'74aoqspff75oe&b=3&s=s8',
#     '_mkto_trk':'id:986-MCG-755&token:_mch-yahoo.com-1593022224105-89202',
#     '_ce.s':'v~UHeC_xAIxdFkEQ00Ryylceqtn1U~ir~1'
# }
# headers = {
#     'Host': 'smallbusiness.yahoo.com',
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Accept-Encoding': 'gzip, deflate',
#     'Content-Type': 'application/json',
#     'X-Requested-With': 'XMLHttpRequest',
#     'Origin': 'https://smallbusiness.yahoo.com',
#     'Referer': 'https://smallbusiness.yahoo.com/businessmaker/payitforward',
#     'Upgrade-Insecure-Requests': '1',
# }

# # Csrf Generate
# response = session.get('https://smallbusiness.yahoo.com/_xhr/_proxy/api/csrf/token', headers=headers, cookies=cookies)
# csrf = json.loads(response.text)["data"]["token"]
# logger.info(csrf)

# data = {"_csrf":csrf,"businessCategory":"Business Billing & Collection","businessCategoryId":"96932170","businessName":"Billing Cagex23"}
# response = session.post('https://smallbusiness.yahoo.com/_xhr/_proxy/api/marketing/business/recommendations', headers=headers, cookies=cookies, json=data)

# # # Register

# cookies = {
#     'YSB_ELEVATED_PRIVACY': 'false',
#     'LV': '1.2&idm=1',
#     'CONSENT': '11111.1593036582106',
#     'anyid': '96af01ea-22da-4887-94f2-ec623dd804b1',
#     '_ga': 'GA1.2.1431927048.1593022216',
#     '_gid': 'GA1.2.1450332677.1593022216',
#     '_gcl_au': '1.1.427969124.1593022219',
#     '_pin_unauth': 'dWlkPU1URTVNRFJqTmprdE1UTmhOeTAwTUdRekxXRXhabVV0Tm1JM05qWTVOVFE0T1RWag',
#     'A3': 'd=AQABBA6X814CEKH-o_p9ZcWoV0EGx-YaK3IFEgEBAQHo9F79XgAAAAAA_SMAAAcIDpfzXuYaK3I&S=AQAAAulj0DEWfi_9nk11JG9djT8',
#     'B': '74aoqspff75oe&b=3&s=s8',
#     '_mkto_trk': 'id:986-MCG-755&token:_mch-yahoo.com-1593022224105-89202',
#     '_fbp': 'fb.1.1593022224605.1597742356',
#     '_ce.s': 'v~UHeC_xAIxdFkEQ00Ryylceqtn1U~ir~1',
# }

# headers2 = {
#     'Host': 'platform-api.yahoosmallbusiness.com',
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Accept-Encoding': 'gzip, deflate',
#     'Content-Type': 'application/json',
#     'Origin': 'https://checkout.yahoosmallbusiness.com',
#     'Referer': 'https://checkout.yahoosmallbusiness.com/bmcheckout/login',
#     'Upgrade-Insecure-Requests': '1',
# }

# data = {"_csrf":csrf,"userInfo":{"firstName":"Jaydeep","lastName":"Patel","userid":"jaydeep25@keepjpg.com","passwd":"Nopassword1305@","marketingConsent":"on","dataConsent":"off","agreetos":"on","bibUser":True},"bizInfo":{"businessType":"BUSINESS","name":"Billing Cagex","ownerName":"Jaydeep Patel","role":"","category":"Business Billing &amp; Collection","categoryId":"96932170","subCategory":"","subCategoryId":"","businessProfile":{"workPlace":"","emplyeeCount":"","yearsOfOperation":"","annualRevenue":"","topConcern":"NONE","howSell":"","howReserve":"","stage":"early","presenceType":""}},"addressInfo":{"address1":"","address2":"","addressType":"LOCATION","presenceType":"PHYSICAL","city":"","state":"","country":"","zipcode":""},"ysbcaptchatoken":captcha_response}
# response = session.post('https://platform-api.yahoosmallbusiness.com/api/businesses/signup', headers=headers2, cookies=cookies, json=data)
# logger.info(response.text)
# with open('cookie.txt', 'w') as f:
#     json.dump(requests.utils.dict_from_cookiejar(session.cookies), f)
        
# response = session.get('https://platform-api.yahoosmallbusiness.com/api/user/payment/wallet?_csrf='+csrf, headers=headers2, cookies=cookies)
# logger.info(response.text)

# # Get Paypal Url
# response = session.get('https://platform-api.yahoosmallbusiness.com/api/user/payment/paypalurl?isBib=true&_csrf='+csrf, headers=headers2, cookies=cookies)
# paypal_url = json.loads(response.text)["data"]["paypalUrl"]
# logger.info(paypal_url)
# token = paypal_url.rsplit("=",1)[1]


# headers3 = {
#     'Host': 'checkout.yahoosmallbusiness.com',
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Accept-Encoding': 'gzip, deflate',
#     'Referer': 'https://www.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token='+token,
#     'Upgrade-Insecure-Requests': '1',
# }

# response = session.get('https://checkout.yahoosmallbusiness.com/paypal-bib/redirect/path/success/confirmation/cancel/payment?token='+token, headers=headers3, cookies=cookies,allow_redirects=False)
# logger.info(response.text)

# with open('cookie2.txt', 'w') as f:
#     json.dump(requests.utils.dict_from_cookiejar(session.cookies), f)
        

