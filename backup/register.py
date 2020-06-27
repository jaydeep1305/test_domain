import os
import re
import time
import requests
import json
import random
import string
from loguru import logger
from imap_tools import MailBox, Q
try:
    from http.cookiejar import LWPCookieJar
except ImportError:
    from cookielib import LWPCookieJar

class Register:

    def __init__(self,CAPTCHA_API,SITE_KEY_RECAPTCHA,DOMAIN_NAME):
        self.SITE_KEY_RECAPTCHA = SITE_KEY_RECAPTCHA
        self.CAPTCHA_API = CAPTCHA_API
        self.DOMAIN_NAME = DOMAIN_NAME
        self.REGISTER_TRY = 5
        self.CAPTCHA_TRY = 3

        json_data = json.loads('[{"catid":96930298,"catname":"Business Services","subcatid":96932170,"subcatname":"Business Billing & Collection"},{"catid":96930298,"catname":"Business Services","subcatid":96932156,"subcatname":"Trade Organizations"},{"catid":96930298,"catname":"Business Services","subcatid":96932169,"subcatname":"Business Brokers"},{"catid":96930298,"catname":"Business Services","subcatid":96932152,"subcatname":"Business Development"},{"catid":96930676,"catname":"Food Services","subcatid":96937265,"subcatname":"Business Coffee Service"},{"catid":96930298,"catname":"Business Services","subcatid":96932176,"subcatname":"Customer Service"},{"catid":96930298,"catname":"Business Services","subcatid":96932167,"subcatname":"Document Handling"},{"catid":96930298,"catname":"Business Services","subcatid":96937264,"subcatname":"Water Coolers"},{"catid":96930298,"catname":"Business Services","subcatid":96932181,"subcatname":"Employee Assistance"},{"catid":96930298,"catname":"Business Services","subcatid":96932179,"subcatname":"Employee Benefits"},{"catid":96930298,"catname":"Business Services","subcatid":96932186,"subcatname":"Employee Screening"},{"catid":96930298,"catname":"Business Services","subcatid":96932183,"subcatname":"Background Verification"},{"catid":96930298,"catname":"Business Services","subcatid":96932153,"subcatname":"Facilities Management"},{"catid":96930298,"catname":"Business Services","subcatid":96932150,"subcatname":"Franchising"},{"catid":96930298,"catname":"Business Services","subcatid":96932154,"subcatname":"Human Resources"},{"catid":96930298,"catname":"Business Services","subcatid":96932175,"subcatname":"Incorporation Services"},{"catid":96930298,"catname":"Business Services","subcatid":96932161,"subcatname":"Maintenance Services"},{"catid":96930298,"catname":"Business Services","subcatid":96932172,"subcatname":"Management & Consulting"},{"catid":96930298,"catname":"Business Services","subcatid":96932187,"subcatname":"Outsourcing"},{"catid":96930298,"catname":"Business Services","subcatid":96932174,"subcatname":"Public Relations"},{"catid":96930298,"catname":"Business Services","subcatid":96932171,"subcatname":"Purchasing & Supply"},{"catid":96930298,"catname":"Business Services","subcatid":96932185,"subcatname":"Recruitment & Placement"},{"catid":96930298,"catname":"Business Services","subcatid":96932151,"subcatname":"Secretarial"},{"catid":96930298,"catname":"Business Services","subcatid":96932168,"subcatname":"Transcription & Recording"},{"catid":96930298,"catname":"Business Services","subcatid":96932158,"subcatname":"Translation Services"},{"catid":96930298,"catname":"Business Services","subcatid":96937263,"subcatname":"Vending Machines"},{"catid":96930298,"catname":"Business Services","subcatid":96932163,"subcatname":"Warehouse Storage"},{"catid":96930298,"catname":"Business Services","subcatid":96932184,"subcatname":"Workplace Safety"},{"catid":96930289,"catname":"Communications & Media","subcatid":96930853,"subcatname":"Business Web Site Hosting"},{"catid":96930298,"catname":"Business Services","subcatid":96929861,"subcatname":"Board Level Components"},{"catid":98160039,"catname":"Computer & Electronics Services","subcatid":96932773,"subcatname":"Computer Business Solutions"},{"catid":98160039,"catname":"Computer & Electronics Services","subcatid":96932828,"subcatname":"Business Computer Cleaning"},{"catid":96930298,"catname":"Business Services","subcatid":96932825,"subcatname":"Computer Facilities Management"},{"catid":96932825,"catname":"Computer Facilities Management","subcatid":96932776,"subcatname":"Business Computer Consulting"},{"catid":96932688,"catname":"Software","subcatid":96932827,"subcatname":"Business Computer Equipment"},{"catid":96928703,"catname":"Office Furniture","subcatid":96932826,"subcatname":"Business Computer Furniture"},{"catid":96932172,"catname":"Management & Consulting","subcatid":96932770,"subcatname":"Business Information Systems"},{"catid":98160039,"catname":"Computer & Electronics Services","subcatid":96932777,"subcatname":"Business Computers Leasing"},{"catid":98160039,"catname":"Computer & Electronics Services","subcatid":96932769,"subcatname":"Business Computer Maintenance"},{"catid":96930298,"catname":"Business Services","subcatid":96932689,"subcatname":"Computer Recycling & Salvaging"},{"catid":96932827,"catname":"Business Computer Equipment","subcatid":96932690,"subcatname":"Computer Wholesale"},{"catid":96930298,"catname":"Business Services","subcatid":96929865,"subcatname":"RF & Microwave"},{"catid":98160039,"catname":"Computer & Electronics Services","subcatid":96932775,"subcatname":"Business Computers Support"},{"catid":96925690,"catname":"Real Estate","subcatid":96931803,"subcatname":"Real Estate Business Centers"},{"catid":96930300,"catname":"Corporate Finance & Investment","subcatid":96930976,"subcatname":"Business Taxes"},{"catid":96930298,"catname":"Business Services","subcatid":96930676,"subcatname":"Food Services"},{"catid":96928706,"catname":"Office Supplies","subcatid":96935163,"subcatname":"Office Paper Wholesale"},{"catid":96937316,"catname":"Printing","subcatid":96931894,"subcatname":"Business Forms Printing"},{"catid":96925702,"catname":"Car Security","subcatid":96933150,"subcatname":"Business Alarm Systems"},{"catid":96930298,"catname":"Business Services","subcatid":96925764,"subcatname":"Computer Multimedia"},{"catid":96930298,"catname":"Business Services","subcatid":96926933,"subcatname":"Computer User Groups"},{"catid":98201343,"catname":"Acting Schools","subcatid":96928483,"subcatname":"Business Schools"},{"catid":96930298,"catname":"Business Services","subcatid":96925785,"subcatname":"School Supplies"},{"catid":96928069,"catname":"Business Financing","subcatid":96927044,"subcatname":"Finance & Taxation"},{"catid":96925944,"catname":"Financing","subcatid":96928069,"subcatname":"Business Financing"},{"catid":96928706,"catname":"Office Supplies","subcatid":96928705,"subcatname":"Personal Stationery"},{"catid":96930298,"catname":"Business Services","subcatid":96928706,"subcatname":"Office Supplies"},{"catid":null,"catname":null,"subcatid":96930298,"subcatname":"Business Services"},{"catid":96930298,"catname":"Business Services","subcatid":96930295,"subcatname":"Conventions & Trade Shows"},{"catid":96930298,"catname":"Business Services","subcatid":96930300,"subcatname":"Corporate Finance & Investment"},{"catid":96930298,"catname":"Business Services","subcatid":96932166,"subcatname":"Commercial Security"},{"catid":96930298,"catname":"Business Services","subcatid":96930296,"subcatname":"Commercial Shipping"},{"catid":96930298,"catname":"Business Services","subcatid":96950266,"subcatname":"Commercial Transportation"},{"catid":96930298,"catname":"Business Services","subcatid":100005071,"subcatname":"Import & Export"}]')
        random_int = random.randint(0,60)
        i = 0
        random_data = ""
        for json_rand in json_data:
            if i == random_int :
                random_data = json_rand
                break
            i += 1

        self.CATEGORY_ID = random_data['catid']
        self.CATEGORY_NAME = random_data['catname']
        self.SUB_CATEGORY_ID = random_data['subcatid']
        self.SUB_CATEGORY_NAME = random_data['subcatname']

        self.FIRST_NAME_LIST='Aadi,Aarav,Aarnav,Aarush,Aayush,Abdul,Abeer,Abhimanyu,Abhiramnew,Aditya,Advaith,Advay,Advik,Agastya,Akshay,Amol,Anay,Anirudh,Anmol,Ansh,Arin,Arjun,Arnav,Aryan,Atharv,Avi,Ayaan,Ayush,Ayushman,Azaan,Azad,Brijesh,Bachittar,Bahadurjit,Bakhshi,Balendra,Balhaar,Baljiwan,Balvan,Balveer,Banjeet,Chaitanya,Chakradev,Chakradhar,Champak,Chanakya,Chandran,Chandresh,Charan,Chatresh,Chatura,Daksh,Darsh,Dev,Devansh,Dhruv,Dakshesh,Dalbir,Darpan,Ekansh,Ekalinga,Ekapad,Ekavir,Ekaraj,Ekbal,Farhan,Falan,Faqid,Faraj,Faras,Fitan,Fariq,Faris,Fiyaz,Frado,Gautam,Gagan,Gaurang,Girik,Girindra,Girish,Gopal,Gaurav,Gunbir,Guneet,Harsh,Harshil,Hredhaan,Hardik,Harish,Hritik,Hitesh,Hemang,Isaac,Ishaan,Imaran,Indrajit,Ikbal,Ishwar,Jainew,Jason,Jagdish,Jagat,Jatin,Jai,Jairaj,Jeet,Kabir,Kalpit,Karan,Kiaan,Krish,Krishna,Laksh,Lakshay,Lucky,Lakshit,Lohit,Laban,Manan,Mohammed,Madhav,Mitesh,Maanas,Manbir,Maanav,Manthan,Nachiket,Naksh,Nakul,Neel,Nakul,Naveen,Nihal,Nitesh,Om,Ojas,Omkaar,Onkar,Onveer,Orinder,Parth,Pranav,Praneel,Pranit,Pratyush,Qabil,Qadim,Qarin,Qasim,Rachit,Raghav,Ranbir,Ranveer,Rayaan,Rehaannew,Reyansh,Rishi,Rohan,Ronith,Rudranew,Rushil,Ryan,Sai,Saksham,Samaksh,Samar,Samarth,Samesh,Sarthak,Sathviknew,Shaurya,Shivansh,Siddharth,Tejas,Tanay,Tanish,Tarak,Teerth,Tanveer,Udant,Udarsh,Utkarsh,Umang,Upkaar,Vedant,Veer,Viaannew,Vihaan,Viraj,Vivaan,Wahab,Wazir,Warinder,Warjas,Wriddhish,Wridesh,Yash,Yug,Yatin,Yuvraj,Yagnesh,Yatan,Zayan,Zaid,Zayyan,Zashil,Zehaan'
        self.FIRST_NAME=self.FIRST_NAME_LIST.split(",")[random.randint(0,len(self.FIRST_NAME_LIST.split(","))-1)]
        self.LAST_NAME_LIST='Aambaliya,Abhangi,Ajani,Ajudia,Akbari,Akvaliya,Amin,Amipara,Amreliya,Andani,Antala,Asalaliya,Asodariya,Atkotiya,Babariya,Baldha,Bambharoliya,Barasiya,Barejiya,Barvadiya,Bhadani,Bhalara,Bhanderi,Bhayani,Bhesaniya,Bhingradiya,Bhudiya,Bhut,Bhuva,Bodar,Boghra,Borad,Borsadiya,Buha(busa),Butani,Chabhadiya,Chhayani.,Chhodavadiya,Chikhaliya,Chimediya,Chohaliya,Chothani,Chovatiya,Dabasiya,Damasiya,Dangariya,Desai,Devani,Dhaduk,Dhameliya,Dhami,Dhanani,Dhankecha,Dholariya,Dhorajiya,Dobariya,Domadiya,Donga,Dudhagara,Dudhat,Dudhatra,Dungarani,Faldu,Gadhethariya,Gadhiya,Gajera,Gajipara,Gami,Gangani,Garsondiya,Gelani,Gevariya,Ghelani,Ghoniya,Ginoya,Gothadiya,Godhani,Golani,Gondaliya,Gorasiya,Halai,Hapaliya,Hapani,Harkhani,Harsoda,Hidad,Hirani,Hirapara,Jagani,Jangvadiya,Jasani,Jesani,Jetani,Jiyani,Jodhani,Jogani,Kabariya,Kabra,Katba,Kachhadiya,Kachhi,Kakadiya,Kalkani,Kalsariya,Kamani,Kanani,Kapadiya,Kapupara,Kapuriya,Karad,Karkar,Kasvala,Kathiriya,Kathrotiya,Kerai,Khakhariya,Khatra,Khetani,Khichadiya,Khunt,Kikani,Kodinariya,Koladiya,Korat,Kotadiya,Kothari,Kothiya,Koyani,Kumbhani,Kunjadiya,Kyada,Lakhani,Lila,Limbani,Limbasiya,Lukhi,Lunagariya,Madani,Madhapariya,Malaviya(maraviya),Mandanka,Mangroliya,Mansara,Marakana,Mathukiya,Mavani,Mayani,Meghani,Mendpara,Mepani,Moliya,Monpara,Monpariya,Morad,Moradiya,Movaliya,Mulani,Mungra,Mungalpara,Nadiyadhara,Nagani,Nakrani,Nandaniya,Nariya,Nasit,Nonghanvadra,Padmani,Padariya,Padsala,Paghdar,Paladiya,Pambhar,Panchani,Paneliya,Pansara,Panseriya,Pansuriya,Parakhiya,Parsana,Patodiya,Pipaliya,Pipalva,Pirojiya,Pokar,Polra,Ponkiya,Poshiya,Rabadiya,Radadiya,Rafaliya,Raiyani,Rajani,Rakholiya,Ramani,Ramoliya,Rangani,Rank,Ranpariya,Ribadiya,Rokad,Rudani,Rupapara,Rupareliya,Sabalpara,Sabhaya,Sagpariya,Sakariya,Sakhiya,Sakhreliya,Sakhvada,Sangani,Sanghani,Sardhara,Sarkheliya,Satani,Satasiya,Satodiya,Savakiya,Savaliya,Seladiya,Senjaliya,Shankhavara,Shekhaliya,Shekhda,Shingala,Shiyani,Sidpara,Siroya,Sojitra,Sonani,Sorathiya,Sudani,Sutariya,Suvagiya,Tadhani,Talaviya,Tanti,Tarapara,Tejani,Thesiya,Thumar,Thumbar,Tilala,Timbadiya,Togadiya,Trada(tada),Trapasiya,Umretiya,Undhad,Usadad,Usadadiya,Vachhani,Vadi,Vadodariya,Vagadiya,Vaghajiani,Vaghani,Vaghasiya,Vaishnav,Vanpariya,Varsani,Vasani,Vasoya,Viradiya,Virani,Visavaliya,Vora,Vekariya,Zadafiya,Zalavadiya.,Chuvadia.,Dholakiya,Navadiya,Savani,Patoliya,Pandadiya,Goyani,Jivani,Shyani,Maniya,Bharodiya,Viththani,Gothaliya,Pethani,Gundaliya,Bonde,Babiya,Pedhadiya,Bagadiya,Hingladiya,Bandhaniya,Hala,Memagra,Akoliya,Valani,Gediya,Mangukiya,Saspara,Roy,Jajadiya'
        self.LAST_NAME=self.LAST_NAME_LIST.split(",")[random.randint(0,len(self.LAST_NAME_LIST.split(","))-1)]

        self.EMAIL = self.FIRST_NAME+self.LAST_NAME+str(random.randint(0,122))+"@"+self.DOMAIN_NAME
        self.PASSWORD = self.randomString()

        self.BUSINESS_SUFFIX = 'hunt,link,exim,world,drive,cafe'
        self.BUSINESS_NAME_LIST = 'Tested,Pursue,Match,Interactive,Liquid,Nest,Enterprise,Immense,Qualified,Syndicate,Hunt,Link,Advantage,Methodical,Paramount,Operate,Ium,Prism,Search,Cardinal,Rocket,Key,Masses,Headway,Domain,Strive,Spread,Flow,Adil,Netic,Performance,Forward,Bot,Growth,Ex,Complete,Blueocean,Quest,Advance,Dash,Ya,Intellect,Fluent,Magnetic,Drive,Chase,Unite,Vision,Thrive,Reactor,Pursuit,Vio,Society,Fuse,Infinite,Io,Verse,Arrowhead,Dynamic,Activator,Ado,Agitator,Globe,Connect,Plan,Progress,Citadel,Nexus,Suite,X,Native,Origin,Que,Altitude,Egy,International,Relevant,Motivate,Grow,Determined,Orama,Executive,Magnet,Arc,Pulse,Cycle,Inform,Engine,Scape,Meta,Motion,Check,Value,Illuminate,Pillar,Expand,Managed,Funnel,Sustained,Arrange,Progress,Operate,Key,Cornerstone,Insta,Analytics,Hunt,Major,Indicator,Arrowhead,Ster,Deck,Pursue,Globe,Tastic,Executive,Post,Ly,Origin,Authority,Eagle,Simple,Que,Bastion,Segment,Growth,Motivate,City,More,Progress,Bound,Strategic,Agitator,Support,Smash,Chase,Pitch,Think,Optimize,Dash,Vertex,Mesh,Metrics,Signal,Engine,Proof,Mention,Syndicate,Association,Pulse,Zoid,Split,Relevant,Point,Spire,Traffic,Magnetic,Immersive,Enterprise,Spread,Gonzo,Quest,Wired,X,Push,Thrive,Ella,Onus,Powerhouse,Link,Nest,Loop,Social,Bes,Plan,Flow,Performance,Intel,Know,Edge,Direct,Decide,Prospect,Intellect,Intuition,Complete,Brillant,Ooze,N,Tag,Send,Decision'
        self.BUSINESS_NAME = self.BUSINESS_NAME_LIST.split(",")[random.randint(0,len(self.BUSINESS_NAME_LIST.split(","))-1)] + self.BUSINESS_SUFFIX.split(",")[random.randint(0,len(self.BUSINESS_SUFFIX.split(","))-1)]


    def randomString(self,stringLength=12):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(stringLength))+"@"

    def captcha_request(self,SITE_KEY=""):
        if SITE_KEY:
            self.SITE_KEY_RECAPTCHA = SITE_KEY
            logger.info(SITE_KEY)

        response = requests.get("https://2captcha.com/in.php?key="+self.CAPTCHA_API+"&method=userrecaptcha&googlekey="+self.SITE_KEY_RECAPTCHA+"&pageurl=https://login.yahoosmallbusiness.com/signup")
        response = response.content.decode()
        if "OK" == response[:2] : 
            captcha_process = response[3:]
            captcha_res = self.captcha_response(captcha_process)
        captcha_res = captcha_res[3:]
        logger.debug(captcha_res)
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

    def register(self,captcha_response):
        json_data = '''{
            "_csrf": "1592916370.d5fd2670a5057caa93533be2250d98f874687b73",
            "userInfo": {
                "firstName": "'''+ self.FIRST_NAME +'''",
                "lastName": "'''+ self.LAST_NAME +'''",
                "userid": "'''+ self.EMAIL +'''",
                "passwd": "'''+ self.PASSWORD +'''",
                "marketingConsent": "on",
                "dataConsent": "off",
                "agreetos": "on",
                "bibUser": true
            },
            "bizInfo": {
                "businessType": "BUSINESS",
                "name": "'''+ self.BUSINESS_NAME +'''",
                "ownerName": "''' + self.FIRST_NAME + ''' ''' + self.LAST_NAME + '''",
                "role": "",
                "category": "''' + self.CATEGORY_NAME +  '''",
                "categoryId": "'''+ str(self.CATEGORY_ID) +'''",
                "subCategory": "''' + self.SUB_CATEGORY_NAME+'''",
                "subCategoryId": "'''+ str(self.SUB_CATEGORY_ID)+'''",
                "businessProfile": {
                    "workPlace": "",
                    "emplyeeCount": "",
                    "yearsOfOperation": "",
                    "annualRevenue": "",
                    "topConcern": "NONE",
                    "howSell": "",
                    "howReserve": "",
                    "stage": "early",
                    "presenceType": ""
                }
            },
            "addressInfo": {
                "address1": "",
                "address2": "",
                "addressType": "LOCATION",
                "presenceType": "PHYSICAL",
                "city": "",
                "state": "",
                "country": "",
                "zipcode": ""
            },
            "ysbcaptchatoken": "''' + captcha_response +'''"
        }'''    

        cookies = {
            'YSB_ELEVATED_PRIVACY': 'false',
            '_ga': 'GA1.2.1602069669.1592916267',
            '_gid': 'GA1.2.1397379951.1592916267',
            'anyid': 'e37003dc-2f40-4b45-9ca0-4ffcc511b93a',
            '_gcl_au': '1.1.1344470164.1592916378',
            '_uetsid': 'dcef7a95-418b-18b0-f2ad-f16f66532205',
            '_uetvid': '3c590313-ee62-55a6-3a51-548a359d6e47',
            '_mkto_trk': 'id:986-MCG-755&token:_mch-yahoosmallbusiness.com-1592916383490-36585',
            '_fbp': 'fb.1.1592916383607.850165273',
            'weird_get_top_level_domain': 'cookie',
            'CONSENT': '11111.1592916422024',
            '_gat_UA-69260790-1': '1',
        }

        headers = {
            'Host': 'platform-api.yahoosmallbusiness.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'Content-Length': '1231',
            'Origin': 'https://checkout.yahoosmallbusiness.com',
            'Connection': 'close',
            'Referer': 'https://checkout.yahoosmallbusiness.com/bmcheckout/login',
        }

        response = requests.post('https://platform-api.yahoosmallbusiness.com/api/businesses/signup', headers=headers, cookies=cookies, data=json_data)
        json_data = json.loads(response.text)
        logger.info(json_data)
        if json_data['success'] == False:
            self.REGISTER_TRY -= 1
            if self.REGISTER_TRY <= 0 :
                return False
            return self.register(captcha_response)
        return True

    def check_mail(self):
        link = ""
        mailbox = MailBox('imap.zoho.com')
        mailbox.login('admin@keepjpg.com', 'memyself555', initial_folder='ZMNotification')
        mails = [msg for msg in mailbox.fetch(Q(text="Give your account the green light"))]

        for mail in mails:
            mail_to = mail.to[0]
            if mail_to == self.EMAIL:
                content = mail.text
                link = re.search('<(.*)>',content).group(1)                

        if link == "" :
            logger.info("didn't receive mail or mail problem")
            return self.check_mail()

        return link

    def login(self,captcha_response,login_link) :
        self.EMAIL = "jaydeep25@keepjpg.com"
        self.PASSWORD = "Nopassword1305@"
        session = requests.Session()
        session.cookies = LWPCookieJar('cookiejar')

        re_login_link = login_link
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
            # 'Referer' : login_link+"?activate=1&userid="+EMAIL+".done=https://login.yahoosmallbusiness.com/activate?.done=https://dashboard.yahoosmallbusiness.com&sign="+activation_code.strip(),
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
        # logger.debug(response.content)
        response = session.get(re_login_link,cookies=cookies)
        with open('cookie.txt', 'w') as f:
            json.dump(requests.utils.dict_from_cookiejar(session.cookies), f)
        
        session.cookies.save(ignore_discard=True)

        logger.info(response.history)
        for his in response.history:
            logger.info(his.url)
    
        # ## Set Business
        headers2 = {
            'Host': 'smallbusiness.yahoo.com',
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://smallbusiness.yahoo.com',
            'Referer': 'https://smallbusiness.yahoo.com/businessmaker/payitforward',
        }

        json_data = {"_csrf":csrf,"businessCategory":"Business Development","businessCategoryId":"96932152","businessName":"Mine world"}
        response = session.post('https://smallbusiness.yahoo.com/_xhr/_proxy/api/marketing/business/recommendations', headers=headers2, cookies=cookies, json=json_data)
        logger.info(response.content)

        # Create User
        # params = (
        #     ('callback', 'jQuery33108320123340691191_1593029296852'),
        #     ('_csrf', csrf),
        #     ('anyid', '96af01ea-22da-4887-94f2-ec623dd804b1'),
        #     ('optionToken', ''),
        #     ('_', '1593029296853'),
        # )
        # response = session.get('https://smallbusiness.yahoo.com/_xhr/_proxy/api/user/create', headers=headers2, params=params, cookies=cookies)
        # logger.info(response.content)

        # response = session.get('https://smallbusiness.yahoo.com/_xhr/_proxy/api/user?_csrf='+csrf, headers=headers2, cookies=cookies)
        # logger.info(response.content)

        # # Get user info
        # response = session.get('https://smallbusiness.yahoo.com/_xhr/_proxy/api/user/info?_csrf=' + csrf, headers=headers2, cookies=cookies)
        # logger.info(response.content)

        # data = '_csrf='+csrf+'&subscriptions=[{\\"id\\":\\"36f71763-2d9f-40f1-84c7-78d2bf65dc59\\",\\"baseProductId\\":\\"bmaker\\",\\"meta\\":{},\\"addRatePlans\\":[{\\"ratePlanId\\":\\"bmaker_t12m\\",\\"productId\\":\\"bmaker\\",\\"type\\":\\"base\\"},{\\"ratePlanId\\":\\"acctfree_t1m\\",\\"productId\\":\\"acctfree\\",\\"type\\":\\"addon\\"},{\\"ratePlanId\\":\\"wsite_t12m\\",\\"productId\\":\\"wsite\\",\\"type\\":\\"addon\\"},{\\"ratePlanId\\":\\"lwfree_t1m\\",\\"productId\\":\\"lwfree\\",\\"type\\":\\"addon\\"}]}]&promo=PAYITFORWARD&meta={\\"_userData\\":{\\"businessCategory\\":\\"Business+Development\\",\\"businessCategoryId\\":\\"96932152\\",\\"businessName\\":\\"Mine+world\\"},\\"_bundleId\\":\\"custom\\",\\"_bundleName\\":\\"Make+it+your+way\\",\\"_editable\\":false}&domainBundles=[]'
        # response = requests.post('https://smallbusiness.yahoo.com/_xhr/_proxy/api/ordering/cart', headers=headers, cookies=cookies, data=data, verify=False)

        paypal_url = "https://platform-api.yahoosmallbusiness.com/api/user/payment/paypalurl?isBib=true&_csrf="+csrf
        response = session.get(paypal_url,cookies=cookies)
        logger.info(response.content)

