# StockPriceNotifier

## Overview
The Stock Price Notifier is a Python program that checks the price of Tesla's stock on the MarketWatch website. If the stock price decreases by 5% or more, an email notification is sent to the user. The program runs indefinitely, checking the stock price every hour and sending notifications when necessary.

## How the Program Works

1. **Web Scraping**: The program uses the `Selenium` library to access the MarketWatch website and scrape Tesla's stock price and percentage change.
   
2. **Checking Stock**: The program compares the percentage change in the stock price to a threshold (5% decrease). If the stock drops by 5% or more, it triggers an email notification.
   
3. **Sending Email**: The program sends an email using `Yagmail`. The email includes the stock price and a message notifying the user about the price change.

4. **Looping**: The program continuously checks the stock price every hour (`time.sleep(3600)`).

## Features

- Stock price checks every hour.
- Email notifications sent when the stock decreases by 5% or more.
- Automated process, runs indefinitely until terminated.

## Requirements

- Python 3.6+
- Required Libraries: 
  - `yagmail`
  - `selenium`
  - `os`
  - `time`
  - `datetime`
 
## Potential Delays
Page Loading and Scraping: The program scrapes data from the MarketWatch website using Selenium, which involves opening the web page and waiting for elements to load. This can take some time depending on the website's speed and the complexity of the page. The program will wait for the necessary data to be fully loaded before extracting the stock price and percentage change. This process may take a few seconds to a minute.

Email Sending: Sending emails using Yagmail may also take a few seconds depending on network conditions. Please be patient if the email does not arrive immediately.

Program Delay: Since the program is designed to check the stock every hour, there will be a delay of up to 1 hour between each check, as it sleeps for 3600 seconds (time.sleep(3600)).
