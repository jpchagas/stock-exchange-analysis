import numpy as np
import pandas as pd
from pandas_datareader import data as wb
TickerA='ITSA4.SA'
TickerB='FLRY3.SA'
TickerC='LREN3.SA'
prices=pd.DataFrame()
tickers = [TickerA, TickerB, TickerC]
for t in tickers:
    prices[t]=wb.DataReader(t, data_source='yahoo', start='2010-1-1')['Adj Close']