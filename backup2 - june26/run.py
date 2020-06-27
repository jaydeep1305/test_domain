import time
import json
import threading
from init import *
from bounded_pool_executor import BoundedProcessPoolExecutor

def thread(anyid):
    try:
        logger.info(anyid)
        registe_obj = Register(CAPTCHA_API,SITE_KEY_RECAPTCHA,DOMAIN_NAME)
        captcha_response = registe_obj.captcha_request()
        registe_obj.register(captcha_response,anyid)

    except Exception as ex:
        logger.error(ex)

threads = []
anyids = ["efcd3e66-e8d8-4d52-9039-99d413b17af3","0fa4d02f-47c6-47ab-b71c-4e85dcfa02d4","d59640b4-a99a-4404-be53-54d9021bd33e","2b841c3e-8086-4dfd-ac47-0ea2c38c013e","64fcbb02-41bf-45cd-baa2-da3c2512ebb0","fc935ff4-97d6-445c-80e6-475b7961f7ac","6a1124b0-20e5-42b6-aa7c-e3e5d7fd69a2","5d2e617d-f54f-4ba7-8052-18ce68a9c5e5","6f95555a-c5b5-434b-960a-b2e52ad612f9","98dc2d55-d657-4cba-9c04-54607aec0794","7b24b2d4-950c-4b63-8c96-8fd11778047e","901b50f6-697e-478d-ac6a-fdd0f475e2b8","c088ff6d-67d5-4fa2-9d39-778ee92e4968","d089710c-c8c4-49f9-a849-0c44bb898b49","ccd1380e-03d9-4faa-a3ab-feb8489768d5","73434873-79c7-4a9f-90d7-c8c26ce9fa59","0790f223-c9c2-4c82-a3ad-1050d7619e59","351c03aa-af0a-4061-9df5-1afcfb38bc15","705407b9-2e46-446b-9456-e42f7039ed65","20c17287-53ca-4512-afc3-a3e6ce50ebc1","13943b22-f059-4639-a957-d07d58f5f0d0","0faa65db-2335-4218-9691-72397c100b96","81b32e7a-6645-48ac-bc82-3d77f993c054","83703ed2-0ba1-4ba2-9906-ef7248997c49","2c8d4cb2-075f-45e2-80d6-1008428e7f63","0fa04457-ea73-4994-b08a-3c359f532ec9","c520e3e4-9e16-4747-a5a6-363d547eb3ec","e78caecc-02eb-48fd-b148-22ddffe60f68","b6d5a58c-201d-445b-83c4-6d991368898b","59849584-ea3a-434a-9161-e18e17b68195","8e80571d-36f9-402d-8694-96ccd9e26a2a","26cad3e5-587c-4d00-8acd-a508a8390c55","8b72cb58-60de-48b8-a84b-1b9c60a74678","4f49f330-80d8-4595-bb9e-d6407b916066","422aea52-561b-4738-9dc8-71f5c3b27aa2","884c0dd6-ba6c-4008-8ff4-1ea9be1889d2","2dfc070f-d507-478e-bb31-1807e33273bd","d64ad56b-dd1e-4ebb-a72e-f85fc7c3321c","eb9a97c2-5b1c-42b9-9475-ac8da9ac1743","eccdb099-8618-4521-b046-f0bb37a193fe"]
worker = BoundedProcessPoolExecutor(max_workers=15)
j = 100
i = 0
while True:
    anyid = anyids[i]
    if i == (len(anyids)-2):
        i = 0
    else :
        i += 1

    t1 = worker.submit(thread,anyid)
    j -= 1
    if j <= 0 : 
        break

# for i in range(len(anyids)):
#     anyid = anyids[i]
#     t1 = threading.Thread(target=thread,args=(anyid,))
#     t1.start()
#     threads.append(t1)

# for t in threads:
#     t.join()


# time.sleep(20)
# login_link = registe_obj.check_mail()
# logger.info(login_link)
# captcha_response = registe_obj.captcha_request(SITE_KEY_RECAPTCHA_LOGIN)
# registe_obj.login(captcha_response,login_link)
