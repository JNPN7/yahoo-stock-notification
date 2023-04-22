import yfinance as yf
from time import sleep
import asyncio

hourly_subscribers = [
    {
        'email': "ids.major.project@gmail.com",
        'stocks': "META",
        'interval': 3,
        'current': 0
    },
    {
        'email': "ids.major.project@gmail.com",
        'stocks': "ALPHA",
        'interval': 5,
        'current': 0
    }
]

daily_subscirbers = [
    {
        'email': "ids.major.project@gmail.com",
        'stocks': "META",
        'interval': 3,
        'current': 0
    },
    {
        'email': "ids.major.project@gmail.com",
        'stocks': "ALPHA",
        'interval': 5,
        'current': 0
    }
]
msft = yf.Ticker("META")

# get all stock info
print(f'{msft.info}')
# class YahooNotifier:

#     def __init__(self, ticker):
#         self.ticker = ticker
#         self.time_interval = 5
#         self.msft = yf.Ticker(self.ticker)

#     def notify(self):
#         data = self.msft.info
#         print(data['currentPrice'])
    
#     async def test(self, t):
#         while True:
#             print(self.ticker)
#             await asyncio.sleep(t)

# async def notify_hourly_subscriber():
#     while True:
#         print(stock)
#         await asyncio.sleep(t)

# async def notify_daily_subscriber():
#     while True:
#         pass

# async def main():
#     notifier = YahooNotifier("META")
#     new = YahooNotifier("Google")
#     newtask = asyncio.create_task(notifier.test(2))
#     newtask2 = asyncio.create_task(new.test(7))
#     while True:
#         await asyncio.sleep(2)
#         notifier.ticker = "X CORP"
#         await asyncio.sleep(3)
#         notifier.ticker = "STEAM"
#         pass

# asyncio.run(main())