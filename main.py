import yagmail 
import os

my_email = os.getenv('email')
my_password = os.getenv('password')

yag = yagmail.SMTP(user=my_email, password=my_password)

subject = "Stock Price Notification for Aishwin"

content = " "

yag.send(to=my_email, subject=subject, contents=content)

def getContents():
    







