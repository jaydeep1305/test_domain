from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.paypal.com/cgi-bin/webscr?cmd=_express-checkout&token=EC-0JL36288VA587125S#/checkout/review")