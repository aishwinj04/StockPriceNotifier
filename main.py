import yagmail 
import os

def sendEmail():
    my_email = os.getenv('email')
    my_password = os.getenv('password')