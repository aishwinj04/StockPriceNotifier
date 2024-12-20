import yagmail 
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# initialize webdriver to access site
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)

    driver.get("https://www.marketwatch.com/investing/index/spx?mod=home-page")

    return driver


def clean_text(text):
    # extract value before the percent symbol
    percent = text.split("%")
    percent = float(percent[0])
    return percent



def send_email():
    my_email = os.getenv('email')
    my_password = os.getenv('password')

    yag = yagmail.SMTP(user=my_email, password=my_password)

    subject = "Stock Price Notification!!"

    content = " "

    yag.send(to=my_email, subject=subject, contents=content)


def main():
    driver = get_driver()
    element = driver.find_element(
        by="xpath", value= '//*[@id = "maincontent"]/div[2]/div[3]/div/div[2]/bg-quote/span[2]')
    
    cleaned = clean_text(element.text)
    print(cleaned)


if __name__ == "__main__":
    main()








