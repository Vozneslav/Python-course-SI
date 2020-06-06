#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests as rq


def cena_danych():
        ETH = rq.get("https://bitbay.net/API/Public/ETH/ticker.json")
        BTC = rq.get("https://bitbay.net/API/Public/BTC/ticker.json")
        LTC = rq.get("https://bitbay.net/API/Public/LTC/ticker.json")
        BCC = rq.get("https://bitbay.net/API/Public/BCC/ticker.json")
        GAME = rq.get("https://bitbay.net/API/Public/GAME/ticker.json")
        return ETH.json(), BTC.json(), LTC.json(), BCC.json(), GAME.json()

def max_zysk(ilosc):
    while True:
        ETH_ticker, BTC_ticker, LTC_ticker, BCC_ticker, GAME_ticker = cena_danych()

        roznice_cen = {
            'ETH': (ETH_ticker['max']) / float(ETH_ticker['min']) - 1,
            'BTC': float(BTC_ticker['max']) / float(BTC_ticker['min']) - 1,
            'LTC': float(LTC_ticker['max']) / float(LTC_ticker['min']) - 1,
            'BCC': float(BCC_ticker['max']) / float(BCC_ticker['min']) - 1,
            'GAME': float(GAME_ticker['max']) / float(GAME_ticker['min']) - 1}

        volumes = { 'ETH': float(ETH_ticker['volume']),
            'BTC': float(BTC_ticker['volume']),
            'LTC': float(LTC_ticker['volume']),
            'BCC': float(BCC_ticker['volume']),
            'GAME': float(GAME_ticker['volume'])}

        najnizsza_cena = {'ETH': float(ETH_ticker['min']),
            'BTC': float(BTC_ticker['min']),
            'LTC': float(LTC_ticker['min']),
            'BCC': float(BCC_ticker['min']),
            'GAME': float(GAME_ticker['min'])}

        sorted_kryptowaluta = sorted(roznice_cen, key= roznice_cen.get, reverse=True)

        for kryptowaluta in sorted_kryptowaluta:
            print(kryptowaluta ,  roznice_cen[kryptowaluta] * 100)

        for kryptowaluta in sorted_kryptowaluta:
            if ilosc > 0:
                if volumes[kryptowaluta ] * najnizsza_cena[kryptowaluta ] < ilosc:
                    ilosc = ilosc -                              volumes[kryptowaluta ] * najnizsza_cena[kryptowaluta ]
                    print('Mozesz kupic:', volumes[kryptowaluta ] * najnizsza_cena[kryptowaluta ], kryptowaluta )
                    print('Zostalowiles:', ilosc, 'USD')
                else:
                    print('Mozesz kupic:', ilosc / najnizsza_cena[kryptowaluta], kryptowaluta )
                    ilosc = 0
                    print('Nie masz pieniedzy:','USD')

max_zysk(100000)


# In[ ]:





# In[ ]:




