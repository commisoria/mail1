import yfinance as yf
import streamlit as st
from time import sleep

def gold():
    gold = yf.download(tickers="GC=F", period="1d", interval="15m")
    latest_price = gold['Close'].iloc[-1]
    return latest_price

while True:
    gold=gold()
    st.write(gold)
    sleep(120)
