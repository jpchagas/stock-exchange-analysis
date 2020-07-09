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
    if page == 'Todas':
        st.dataframe(prices)
        st.line_chart(prices)
        xn = 0
        x1 = 0
        for s in stocks:
            size = len(prices[s])-1
            xn += prices[s][size]
            x1 += prices[s][0]
        st.header('Valor Inicial: %s' % round(x1,2))
        st.header('Valor Atual: %s' % round(xn,2))
        rentabilidade = round(((xn/x1)-1)*100,2) 
        st.header('Rentabilidade: %s' % rentabilidade)

    else:
        st.dataframe(prices[page])
        st.line_chart(prices[page])
        ac1 = prices[page]
        size = len(ac1)-1
        xn = ac1[size]
        x1 = ac1[0]
        st.header('Valor Inicial: %s' % round(x1,2))
        st.header('Valor Atual: %s' % round(xn,2))
        rentabilidade = round(((xn/x1)-1)*100,2) 
        st.header('Rentabilidade: %s' % rentabilidade)
        #st.text(rentabilidade)

if __name__ == '__main__':
    main()