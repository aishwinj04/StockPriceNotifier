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

    driver.get("https://www.marketwatch.com/investing/stock/tsla")

    return driver


def clean_text(text):
    # extract value before the percent symbol
    percent = text.split("%")
    percent = float(percent[0])
    return percent



def send_email(content):
    my_email = os.getenv('email')
    my_password = os.getenv('password')

    yag = yagmail.SMTP(user=my_email, password=my_password)

    subject = "Stock Price Notification!!"

    content = " "

    yag.send(to=my_email, subject=subject, contents=content)


def main():
    driver = get_driver()
    percent = driver.find_element(
        by="xpath", value= '//*[@id = "maincontent"]/div[2]/div[3]/div/div[2]/bg-quote/span[2]')
    price = driver.find_element(by="xpath", value='//*[@id="maincontent"]/div[2]/div[3]/div/div[2]/h2/bg-quote')
    print(price)
    value = clean_text(percent.text)

    
    # if value < -10: 
    #     content = f"""
    #     We would like to inform you that Tesla's stock has experienced a significant decrease of 10% or more in value as of today. This represents a notable shift in the market, and we wanted to keep you updated on this development.
    #     As always, we recommend reviewing your portfolio and considering any necessary adjustments in light of this change. If you have any questions or would like further details, feel free to reach out to us.
    #     Thank you for your attention to this important update. We will continue to monitor the stock and provide you with timely notifications of any further changes.

    #     The current price of the stock is: {}
    #     Best regards,
    #     StockNotifier Team
    #     """
    #     send_email(content)

    
    


if __name__ == "__main__":
    main()








