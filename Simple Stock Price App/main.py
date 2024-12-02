import yfinance as yf
import streamlit as st
import pandas as pd

# --------------------------
# Page Title and Description
# --------------------------

st.write("""
# Simple Stock Price App

This app displays the **closing price** and **volume** for a selected stock.

***
""")

# --------------------------
# Fetch Stock Data
# --------------------------

# Define the ticker symbol (default: Google)
tickerSymbol = 'GOOGL'  # Change to 'AAPL' for Apple or any other ticker symbol

# Retrieve stock data from Yahoo Finance
tickerData = yf.Ticker(tickerSymbol)

# Fetch historical stock data
tickerDf = tickerData.history(period='1d', start='2010-05-31', end='2020-05-31')

# --------------------------
# Display Data and Charts
# --------------------------

# Display Closing Price Chart
st.write("## Closing Price")
st.line_chart(tickerDf['Close'])

# Display Volume Chart
st.write("## Volume Price")
st.line_chart(tickerDf['Volume'])
