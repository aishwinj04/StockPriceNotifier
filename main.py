import time
from scrape_stock import check_stock
from notify_email import send_email

def main():
    while True:
        content = check_stock()

        # function returns value if dropped by 5%
        if content:
            send_email(content)

        time.sleep(3600) # check every hour 


if __name__ == "__main__":
    main()
