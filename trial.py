import yfinance as yf
import streamlit as st
from time import sleep
st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder="Choose an option", disabled=False, label_visibility="visible")

def gold():
    gold = yf.download(tickers="GC=F", period="1d", interval="15m")
    latest_price = gold['Close'].iloc[-1]
    return latest_price

while True:
    gold=gold()
    st.write(gold)
    sleep(120)
