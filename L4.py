#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests
import pandas as pd

def get_market_data():
  name1 = 'Bitbay'
  data_gielda1 = requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()
  gielda1 = {'buy': data_gielda1['ask'],
            'sell': data_gielda1['bid']}

  name2 = 'Blokchain'
  data_gielda2 = requests.get('https://blockchain.info/ticker').json()
  gielda2 = {'buy': data_gielda2['USD']['buy'],
            'sell': data_gielda2['USD']['sell']}

  name3 = 'Coinbase'
  gielda3 = {'buy': requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy.json').json()['data']['amount'],
            'sell': requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell.json').json()['data']['amount']}

  name4 = 'bitstamp'
  data_gielda4 = requests.get('https://www.bitstamp.net/api/ticker/').json()
  gielda4 = {'buy': data_gielda4['high'],
            'sell': data_gielda4['low']}
  return {name1: gielda1, name2: gielda2, name3: gielda3, name4: gielda4}

# print(get_market_data())

def transform(data):
  transformed_data = []
  index = []
  for el in data.items():
    # print(el)
    index.append(el[0])
    transformed_data.append([el[1]['buy'], el[1]['sell']])
  # print(index)
  transformed_data = pd.DataFrame(transformed_data, columns = ['Buy', 'Sell'], index = index, dtype = 'float')
  
  return transformed_data

def buy_and_sell(df):
  buy = df.loc[df['Buy'] == min(df['Buy'])]
  sell = df.loc[df['Sell'] == max(df['Sell'])]
  a = buy['Buy'].to_numpy()
  b = sell['Sell'].to_numpy()
  if a < b:
    print('Jest możliwość arbitrażu: kup na %s i sprzedaj na %s' %(buy.index[0], sell.index[0]))
  else:
    print('Brak możliwości arbitrażu')
  return

buy_and_sell(transform(a))


# In[ ]:





# In[ ]:




