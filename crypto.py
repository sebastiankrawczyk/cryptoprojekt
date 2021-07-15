print('crypto')
import requests
import pandas as pd
from datetime import datetime, timedelta

response = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/history?date=30-5-2019")

#response = requests.get("https://api.coingecko.com/api/v3/coins/bitcoin/history?date=zmienna")

# funkcja(data)
# for
print(response.json())
print(response.json()['market_data']['current_price']['usd'])
print('hello')
# columny ktore chcemy miec
# laduje do dataframema
# csv