import streamlit as st
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import datetime
from dao.news_dao import NewsDAO
from dao.stock_dao import StockDAO


def main():
    stock = st.sidebar.text_input("Enter your stock code","ITSA4.SA")
    start_date = st.sidebar.date_input('Start date',datetime.date.today()-datetime.timedelta(days=30))
    end_date = st.sidebar.date_input('End date',datetime.date.today())
    st.title("Stock Monitor")
    
    stock_name = StockDAO().getStockName(stock)
    news_source = NewsDAO().getNews(stock_name,start_date,end_date)
    news_list = NewsDAO().create_news(news_source)
    news_df = pd.DataFrame(NewsDAO().getJsonList(news_list))

    price = StockDAO().getStock(stock,start_date,end_date)
    st.dataframe(price)
    st.line_chart(price)
    ac1 = price
    size = len(ac1)-1
    xn = ac1[size]
    x1 = ac1[0]
    st.header('Valor Inicial: %s' % round(x1,2))
    st.header('Valor Atual: %s' % round(xn,2))
    rentabilidade = round(((xn/x1)-1)*100,2) 
    st.header('Rentabilidade: %s' % rentabilidade)
    #st.text(rentabilidade)
    st.dataframe(news_df)

if __name__ == '__main__':
    main()