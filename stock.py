import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

stocks = ['ABEV3.SA','MGLU3.SA','BBAS3.SA','BRKM5.SA','BBDC4.SA','AZUL4.SA','ITUB4.SA','BBDC3.SA','VALE3.SA','PETR4.SA','RENT3.SA','SUZB3.SA','CIEL3.SA','GOLL4.SA','GNDI3.SA','BRAP4.SA','B3SA3.SA','BTOW3.SA','EQTL3.SA']

#TickerA='ITSA4.SA'
#TickerB='FLRY3.SA'
#TickerC='LREN3.SA'
prices=pd.DataFrame()
#tickers = [TickerA, TickerB, TickerC]

for s in stocks:
    prices[s]=wb.DataReader(s, data_source='yahoo', start='2020-3-9')['Adj Close']

(prices/prices.iloc[0]*100).plot(figsize=(15,5))
plt.ylabel('NORMALIZED PRICES')
plt.xlabel('DATE')
plt.show()