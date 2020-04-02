#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import json

def get_orders(max = 10):
  data = json.loads(requests.get('https://bitbay.net/API/Public/BTCUSD/orderbook.json').text)
  print('bid:')
  for el in data['bids'][:max]:
    print('%f USD za 1 BTC; max %f BTC'%(el[0], el[1]))
  print('ask:')
  for el in data['asks'][:max]:
    print('%f USD za 1 BTC; max %f BTC'%(el[0], el[1]))

  return


gielda1 = json.loads(requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').text)
print('BitBay: bid: %f ask %f'%(gielda1['bid'], gielda1['ask']))
gielda2 = json.loads(requests.get('https://blockchain.info/ticker').text)
print('blockchain.info: bid: %f ask %f'%(gielda2['USD']['buy'], gielda2['USD']['sell']))

if gielda1['bid'] > gielda2['USD']['buy']:
  lepiej_sprzedac = "bitbay.net"
else:
  lepiej_sprzedac = "blockchain.info"

if gielda1['ask'] < gielda2['USD']['sell']:
  lepiej_kupic = "bitbay.net"
else:
  lepiej_kupic = "blockchain.info"

print("Lepiej kupować BTC na %s\nLepiej sprzedawać BTC na %s"%(lepiej_kupic, lepiej_sprzedac))


# In[2]:


get_orders(5)


# In[ ]:




