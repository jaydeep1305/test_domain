import os
import re
import csv
import time
import json
import random
import string
import shutil
import requests
from loguru import logger
from imap_tools import MailBox, Q
from tempfile import NamedTemporaryFile
try:
    from http.cookiejar import LWPCookieJar
except ImportError:
    from cookielib import LWPCookieJar

class Login:

    def __init__(self,CAPTCHA_API,SITE_KEY_RECAPTCHA,IMAP_SERVER,IMAP_USER,IMAP_PASS,IMAP_FOLDER):
        self.SITE_KEY_RECAPTCHA = SITE_KEY_RECAPTCHA
        self.CAPTCHA_API = CAPTCHA_API
        self.REGISTER_TRY = 5
        self.CAPTCHA_TRY = 3

        filename = 'ids2.csv'
        tempfile = NamedTemporaryFile(mode='w', delete=False)


        flag = True
        fields = ['Email', 'Password', 'First_name', 'Last_name', 'Business_name','id1','id2','Status']
        with open(filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=fields)
            writer = csv.DictWriter(tempfile, fieldnames=fields)
            for row in reader:
                try:
                    if row['Status'] == "registered" :
                        if flag:
                            self.EMAIL = row["Email"]
                            self.PASSWORD = row["Password"]
                            self.FIRST_NAME = row["First_name"]
                            self.LAST_NAME = row["Last_name"]
                            self.BUSINESS_NAME = row["Business_name"]
                            row['Status'] = "login"
                            flag = False
                except Exception as ex:
                    logger.error(ex)
                writer.writerow(row)
        shutil.move(tempfile.name, filename)

        self.ALT_EMAIL = self.randomString(5)+"@keepjpg.com"
        self.MOBILE = "99" + str(random.randint(1000,9999)) + str(random.randint(1000,9999)) 
        self.ANS_1 = self.randomString(7)
        self.ANS_2 = self.randomString(7)
        self.IMAP_SERVER = IMAP_SERVER
        self.IMAP_USER = IMAP_USER
        self.IMAP_PASS = IMAP_PASS
        self.IMAP_FOLDER = IMAP_FOLDER

    def randomString(self,stringLength=12):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))+"@"

    def captcha_request(self,SITE_KEY):
        if SITE_KEY:
            self.SITE_KEY_RECAPTCHA = SITE_KEY
            logger.info(SITE_KEY)

        response = requests.get("https://2captcha.com/in.php?key="+self.CAPTCHA_API+"&method=userrecaptcha&googlekey="+self.SITE_KEY_RECAPTCHA+"&pageurl=https://login.yahoosmallbusiness.com/signup")
        response = response.content.decode()
        if "OK" == response[:2] : 
            captcha_process = response[3:]
            captcha_res = self.captcha_response(captcha_process)
        captcha_res = captcha_res[3:]
        # logger.debug(captcha_res)
        if len(captcha_res) < 30 :
            self.CAPTCHA_TRY -= 1
            if self.CAPTCHA_TRY >= 0 :
                logger.debug("CAPCHA TRY -- " + str(self.CAPTCHA_TRY))
                return self.captcha_request(SITE_KEY)
        return captcha_res
    
    def captcha_response(self,captcha_process):
        response_2captcha = requests.get("https://2captcha.com/res.php?key=" + self.CAPTCHA_API + "&action=get&id=" + captcha_process)
        response = response_2captcha.content.decode()
        response = response.strip()
        if response == "CAPCHA_NOT_READY" :
            logger.info(response)
            time.sleep(15)
            return self.captcha_response(captcha_process)
        else :
            return response


    def check_mail(self):
        logger.info("checking mail of " + self.EMAIL)
        link = ""
        mailbox = MailBox(self.IMAP_SERVER)
        mailbox.login(self.IMAP_USER, self.IMAP_PASS, initial_folder=self.IMAP_FOLDER)
        mails = [msg for msg in mailbox.fetch(Q(text=self.EMAIL))]

        for mail in mails:
            if "Activate" in mail.subject:
                content = mail.text
                link = re.search('<(.*)>',content).group(1)                

        if link == "" :
            logger.info("didn't receive mail or mail problem")
            return self.check_mail()

        return link

    def login(self,captcha_response,login_link) :
        session = requests.Session()
        session.cookies = LWPCookieJar('cookiejar')

        cookies = {
            'YSB_ELEVATED_PRIVACY': 'false',
            '_ga': 'GA1.3.1795022144.1592989294',
            '_gid': 'GA1.3.1810868418.1592989294',
            '_gat': '1',
            '_gali': 'btnLogin',
        }
        activation_code = login_link[51:]
        headers = {
            'Host': 'login.yahoosmallbusiness.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://login.yahoosmallbusiness.com',
            'Referer' : login_link+"?activate=1&userid="+self.EMAIL+".done=https://login.yahoosmallbusiness.com/activate?.done=https://dashboard.yahoosmallbusiness.com&sign="+activation_code.strip(),
            'Upgrade-Insecure-Requests': '1',
        }
        params = (
            ('activate', '1'),
            ('userid', self.EMAIL),
            ('.done', 'https://login.yahoosmallbusiness.com/activate?.done=https://dashboard.yahoosmallbusiness.com&sign='+activation_code.strip()),
        )
        login_link = "https://login.yahoosmallbusiness.com/login"
        response = session.get(login_link, headers=headers, params=params)
        response = response.content.decode()
        csrf = re.search('_csrf"  value="(.*?)"',response).group(1)
        logger.info(csrf)
        timestamp = re.search('_ts"  value="(.*?)"',response).group(1)
        ncforminfo = re.search('__ncforminfo" value="(.*?)"',response).group(1)
        done = re.search('done"  value="(.*?)"',response).group(1)
        time.sleep(5)
        data = 'userid='+self.EMAIL+'&passwd='+self.PASSWORD+'&g-recaptcha-response='+captcha_response+'&.persistent=on&_csrf='+csrf+'&.done='+done+'&_ts='+timestamp+'&_format=classic&nomigrate=&activate=1&activated=&__ncforminfo='+ncforminfo
        response = session.post('https://login.yahoosmallbusiness.com/login', headers=headers, data=data, cookies=cookies, allow_redirects=True)
        time.sleep(5)

        # headers2 = {
        #     'Host': 'platform-api.yahoosmallbusiness.com',
        #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
        #     'Accept': '*/*',
        #     'Accept-Language': 'en-US,en;q=0.5',
        #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        #     'Origin': 'https://dashboard.yahoosmallbusiness.com',
        # }

        # ts = time.time()
        # ts = round(ts)
        # ts = ts*1000

        # # get userid
        # response = session.get('https://platform-api.yahoosmallbusiness.com/api/user/info?_csrf='+csrf, headers=headers2, cookies=cookies)
        # logger.info(response.text)
        # user_id_json = json.loads(response.text)
        # user_id = user_id_json["data"]["id"]
        # logger.debug(user_id)

        # data = '_csrf='+csrf+'&id='+user_id+'&login='+self.EMAIL+'&firstName='+self.FIRST_NAME+'&lastName='+self.LAST_NAME+'&altEmail='+self.ALT_EMAIL+'&contactNum=&mobileNum='+self.MOBILE+'&mobileConsent=false&mobileNumVerified=false&businessType=BUSINESS&businessName=&businessOwnerName=&businessRole=&address1=&address2=&city=&state=&country=&zipcode=&billingAddress1=&billingAddress2=&billingCity=&billingState=&billingCountry=&billingZipcode=&workPlace=&category=&subCategory=&employeeCount=&yearsOfOperation=&annualRevenue=&topConcern=&howSell=&howReserve=&updateTs='+str(ts)+'&tfaEnabled=false&tfaType=&marketingConsent=true&dataConsent=false&bibUser=true&secretAnswerSet=false&secretQuestionsResetRequired=false&passwordResetRequired=false'
        # response = session.post('https://platform-api.yahoosmallbusiness.com/api/user/profile', headers=headers2, cookies=cookies, data=data)
        # logger.info(response.text)

        # headers3 = {
        #     'Host': 'platform-api.yahoosmallbusiness.com',
        #     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
        #     'Accept': 'application/json, text/javascript, */*; q=0.01',
        #     'Accept-Language': 'en-US,en;q=0.5',
        #     'Content-Type': 'application/json',
        #     'Origin': 'https://dashboard.yahoosmallbusiness.com',
        # }

        # json_data = {"_csrf":csrf,"sq1":"1","sa1":self.ANS_1,"sq2":"8","sa2":self.ANS_2}
        # response = requests.post('https://platform-api.yahoosmallbusiness.com/api/user/updateSqa', headers=headers3, cookies=cookies, json=json_data)
        # logger.info(response.text)

        with open('ids2_final.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            # spamwriter.writerow([self.EMAIL,self.PASSWORD,self.FIRST_NAME,self.LAST_NAME,self.BUSINESS_NAME,self.ALT_EMAIL,self.MOBILE,self.ANS_1,self.ANS_2])
            spamwriter.writerow([self.EMAIL,self.PASSWORD,self.FIRST_NAME,self.LAST_NAME,self.BUSINESS_NAME])
        
        logger.info(self.EMAIL + " : " + self.PASSWORD)