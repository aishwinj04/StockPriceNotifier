import yagmail
import os


def send_email(content):

    # hidden email credentials set as environment variables
    my_email = os.getenv('email')
    my_password = os.getenv('password') # app password 

    yag = yagmail.SMTP(user=my_email, password=my_password)

    subject = "Stock Price Alert!"

    yag.send(to=my_email, subject=subject, contents=content)
    print("Email Sent!")
