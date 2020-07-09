import streamlit as st
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt

stocks = ['ABEV3.SA','MGLU3.SA','BBAS3.SA','BRKM5.SA','BBDC4.SA','AZUL4.SA','ITUB4.SA','BBDC3.SA','VALE3.SA','PETR4.SA','RENT3.SA','SUZB3.SA','CIEL3.SA','GOLL4.SA','GNDI3.SA','BRAP4.SA','B3SA3.SA','BTOW3.SA','EQTL3.SA']

prices=pd.DataFrame()


for s in stocks:
    prices[s]=wb.DataReader(s, data_source='yahoo', start='2020-3-9')['Adj Close']


def main():
    page = st.sidebar.selectbox("Escolha uma opção:",['Todas','ABEV3.SA','MGLU3.SA','BBAS3.SA','BRKM5.SA','BBDC4.SA','AZUL4.SA','ITUB4.SA','BBDC3.SA','VALE3.SA','PETR4.SA','RENT3.SA','SUZB3.SA','CIEL3.SA','GOLL4.SA','GNDI3.SA','BRAP4.SA','B3SA3.SA','BTOW3.SA','EQTL3.SA'])
    st.title("MBA CONTROLADORIA E FINANÇAS - Mercado de Capitais")
    st.header('Carteira IBOVESPA Selecionada')
    #st.write('Esta é uma página de teste.')
    if page == 'Todas':
        st.dataframe(prices)
        st.line_chart(prices)
    else:
        st.dataframe(prices[page])
        st.line_chart(prices[page])

if __name__ == '__main__':
    main()