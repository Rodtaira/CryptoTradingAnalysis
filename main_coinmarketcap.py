from coinmarketcap import Market
import matplotlib.pyplot as plt
import pandas as pd
import time

def receive_btc (list_btc):
    market = Market()
    ticker = market.ticker()
    data = ticker['data']['1']['quotes']['USD']['price']
    btc = data
    list_btc.append(btc)
    return list_btc

def receive_xrp (list_xrp):
    market = Market()
    ticker = market.ticker()
    data = ticker['data']['52']['quotes']['USD']['price']
    xrp = data
    list_xrp.append(xrp)
    return list_xrp

list_btc = []
list_xrp = []

fig = plt.figure(figsize=(10,10))
fig2 = plt.figure(figsize=(10,10))

ax = fig.gca()
ax2 = fig2.gca()

while True:
    ax.clear()
    ax2.clear()
    ax.plot(receive_btc(list_btc))
    ax2.plot(receive_xrp(list_xrp))
    plt.pause(1)
