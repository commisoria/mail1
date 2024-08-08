import yfinance as yf
import streamlit as st
from time import sleep
options = ['GC=F', 'BTC-USD', 'PAXG-USD', 'BNB-USD', 'TRY=X']

# Create the select box
selected_option = st.selectbox('Select an option', options)
button=st.button('Calculate')

def asset(selected_option):
    gold = yf.download(tickers=selected_option, period="1d", interval="15m")
    latest_price = gold['Close'].iloc[-1]
    return latest_price

asset=asset(selected_option)
while True:
    if button:
        st.write(asset)
       

    
    


