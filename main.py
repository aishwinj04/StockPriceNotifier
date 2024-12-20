import yagmail 
import os

from selenium import webdriver

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    options.add_experimental_option('excludeSwtiches',['enable-automation'])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.marketwatch.com/investing/index/spx?mod=home-page")

def send_email():
    my_email = os.getenv('email')
    my_password = os.getenv('password')

    yag = yagmail.SMTP(user=my_email, password=my_password)

    subject = "Stock Price Notification for Aishwin"

    content = " "

    yag.send(to=my_email, subject=subject, contents=content)










