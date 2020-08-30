from pandas_datareader import data as wb

class StockDAO():
    def __init__(self):
        self.stockName ={'ITSA4.SA':'Itaúsa',
                         'PETR4.SA':'Petrobras'}

    def getStock(self,s,begin,end):
        print(s)
        return wb.DataReader(s, data_source='yahoo', start=begin,end=end)['Adj Close']

    def getStockName(self, s):
        if self.stockName.get(s):
            return self.stockName.get(s)

