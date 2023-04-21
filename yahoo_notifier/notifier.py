import schedule
import time
import yfinance as yf
from yahoo_notifier.mailer import Mailer

# hourly_subscribers = {
#     "ids.major.project@gmail.com": {
#         'email': "ids.major.project@gmail.com",
#         'stock_sym': "META",
#         'interval': 1,
#         'current': 1,
#         'threshold': 500,
#     },
# }

# daily_subscribers = {
#     "ids.major.project@gmail.com": {
#         'email': "ids.major.project@gmail.com",
#         'stock_sym': "META",
#         'interval': 3,
#         'current': 1,
#         'threshold': 439,
#     },
# }

hourly_subscribers: dict = {}
daily_subscribers: dict = {}

def check_if_stock_symbol_exists(stock_symbol: str):
    try: 
        msft = yf.Ticker(stock_symbol)
        data = msft.info
        _ = data['currentPrice']
        return True
    except:
        return False


def notify_daily_subscriber():
    stock = {}
    for _, subscriber in daily_subscribers.items():
        if subscriber["current"] != subscriber["interval"]:
            subscriber["current"] += 1
            continue
        subscriber["current"] = 1

        if subscriber["stock_sym"] not in stock:
            msft = yf.Ticker(subscriber["stock_sym"])
            data = msft.info
            stock[subscriber["stock_sym"]] = data['currentPrice']

        if stock[subscriber["stock_sym"]] > subscriber["threshold"]:
            print(f'{subscriber["stock_sym"]}: {stock[subscriber["stock_sym"]]}')
            message = f'The threshold has been passed.\nStock Symbol: {subscriber["stock_sym"]}\nCurrent Price: {stock[subscriber["stock_sym"]]}'
            Mailer().mail(message, subscriber["email"])
        

def notify_hourly_subscriber():
    stock = {}
    for _, subscriber in hourly_subscribers.items():
        if subscriber["current"] != subscriber["interval"]:
            subscriber["current"] += 1
            continue
        subscriber["current"] = 1

        if subscriber["stock_sym"] not in stock:
            msft = yf.Ticker(subscriber["stock_sym"])
            data = msft.info
            stock[subscriber["stock_sym"]] = data['currentPrice']

        if stock[subscriber["stock_sym"]] > subscriber["threshold"]:
            print(f'{subscriber["stock_sym"]}: {stock[subscriber["stock_sym"]]} : {subscriber["email"]}')
            message = f'The threshold has been passed.\nStock Symbol: {subscriber["stock_sym"]}\nCurrent Price: {stock[subscriber["stock_sym"]]}'
            Mailer().mail(message, subscriber["email"])


def notify():
    schedule.every(30).seconds.do(notify_hourly_subscriber)
    schedule.every().day.at("16:00").do(notify_daily_subscriber)
    while True:
        schedule.run_pending()
        time.sleep(1)