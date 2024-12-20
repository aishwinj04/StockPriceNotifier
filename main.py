import yagmail 
import os

my_email = os.getenv('email')
my_password = os.getenv('password')

subject = "Stock Price Notification!"
yag = yagmail.SMTP(user=my_email, password=my_password)



