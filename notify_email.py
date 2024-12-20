import yagmail
import os


def send_email(content):

    # email credentials set as environment variables in  open ~/.zshrc in terminal
    my_email = os.getenv('email')
    my_password = os.getenv('password')

    yag = yagmail.SMTP(user=my_email, password=my_password)

    subject = "Stock Price Notification For"

    yag.send(to=my_email, subject=subject, contents=content)
    print("Email Sent!")
