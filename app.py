import streamlit as st
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
import datetime
from dao.news_dao import NewsDAO
from dao.stock_dao import StockDAO


def main():
    #page = st.sidebar.selectbox("Escolha uma opção:",['Todas','ABEV3.SA','MGLU3.SA','BBAS3.SA','BRKM5.SA','BBDC4.SA','AZUL4.SA','ITUB4.SA','BBDC3.SA','VALE3.SA','PETR4.SA','RENT3.SA','SUZB3.SA','CIEL3.SA','GOLL4.SA','GNDI3.SA','BRAP4.SA','B3SA3.SA','BTOW3.SA','EQTL3.SA'])
    stock = st.sidebar.text_input("Enter your stock code","ITSA4.SA")
    start_date = st.sidebar.date_input('Start date')
    end_date = st.sidebar.date_input('End date')
    st.title("Stock Monitor")
    
    stock_name = StockDAO().getStockName(stock)
    news_source = NewsDAO().getNews(stock_name,start_date,end_date)
    print(news_source)
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