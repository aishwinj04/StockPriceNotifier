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

    subject = "Stock Price Notification For"

    yag.send(to=my_email, subject=subject, contents=content)
    print("Email Sent!")


def check_stock():
    driver = get_driver()
    percent = driver.find_element(
        by="xpath", value= '//*[@id = "maincontent"]/div[2]/div[3]/div/div[2]/bg-quote/span[2]')
    price = driver.find_element(by="xpath", value= '//*[@id="maincontent"]/div[2]/div[3]/div/div[2]/h2/bg-quote')
    price = price.text
    stock = driver.find_element(by="xpath", value= '//*[@id="maincontent"]/div[2]/div[2]/div/div[1]/div[2]/span[1]')
    stock = stock.text
    value = clean_text(percent.text)

    
    if value < -1: 
        content = f"""
        
         <p style = "font-size: 16px;"> Hello User! </p>
        <p style = "font-size: 16px;"> We would like to inform you that Tesla's stock has experienced a significant decrease of 10 % or more in value as of today. This represents a notable shift in the market, and we wanted to keep you updated on this development. </p>
        <p style = "font-size: 16px;"> As always, we recommend reviewing your portfolio and considering any necessary adjustments in light of this change. If you have any questions or would like further details, feel free to reach out to us. </p>
        <p style = "font-size: 16px;"> Thank you for your attention to this important update. We will continue to monitor the stock and provide you with timely notifications of any further changes. </p>

        <p style = "font-size: 18px; font-weight: bold;"> The current price of {stock} is {price}</p>

        <p style = "font-size: 14px;"> Best regards, 
        <p style = "font-size: 18px;"> StockNotifier Team </p>
        """
        send_email(content)

def main():
    while True:
        check_stock()
        time.sleep(2)
if __name__ == "__main__":
    main()








