import yfinance as yf
import streamlit as st

def gold():
    gold = yf.download(tickers="GC=F", period="1d", interval="15m")
    latest_price = gold['Close'].iloc[-1]
    return latest_price


gold=gold()

st.write(gold)
