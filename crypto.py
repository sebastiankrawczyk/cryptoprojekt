print('crypto')
import requests
import pandas as pd
from datetime import datetime, timedelta

current_date = datetime(2020,10,2).strftime('%d-%m-%Y')
# response = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/history?date=30-5-2019")

response = requests.get(f"https://api.coingecko.com/api/v3/coins/bitcoin/history?date={current_date}")

# funkcja(data)
# for
print(response.json())
topics = ['current_price', 'market_cap', 'total_volume']
currencies = ['usd', 'xrp', 'link', 'xlm']

data = {}
for topic in topics:
    for currency in currencies:
        data[f"{topic}_{currency}"] = []
data['date'] = []
for topic in topics:
    for currency in currencies:
        data[f"{topic}_{currency}"].append(response.json()['market_data'][topic][currency])
data['date'].append(current_date)

print(data)

print(response.json()['market_data']['current_price']['usd'])
print('hello')
# columny ktore chcemy miec
# laduje do dataframema
# csv