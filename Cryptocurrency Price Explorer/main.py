import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json

#---------------------------------#
# Page layout
st.set_page_config(layout="wide")

#---------------------------------#
# Title and Logo
st.title('Crypto Price App')
st.markdown("""
This app retrieves cryptocurrency prices for the top 100 cryptocurrencies from **CoinMarketCap**!
""")

# Logo placeholder (optional - ensure the image file is available)
# image = Image.open('logo.jpg')
# st.image(image, width=500)

#---------------------------------#
# About Section
with st.expander("About"):
    st.markdown("""
    * **Python libraries:** base64, pandas, streamlit, matplotlib, BeautifulSoup, requests, json
    * **Data source:** [CoinMarketCap](http://coinmarketcap.com).
    * **Credits:** Web scraper inspired by [Bryan Feng](https://medium.com/@bryanf)'s article on web scraping crypto prices.
    """)

#---------------------------------#
# Sidebar layout
st.sidebar.header('User Input Options')

# Sidebar - Currency price unit
currency_price_unit = st.sidebar.selectbox('Select currency for price', ('USD', 'BTC', 'ETH'))

#---------------------------------#
# Web scraping function with caching for performance
@st.cache_data
def load_data():
    cmc = requests.get('https://coinmarketcap.com')
    soup = BeautifulSoup(cmc.content, 'html.parser')

    # Extract JSON data from CoinMarketCap's embedded script
    data = soup.find('script', id='__NEXT_DATA__', type='application/json')
    listings = json.loads(data.contents[0])['props']['initialState']['cryptocurrency']['listingLatest']['data']

    # Extract relevant data fields
    data_list = []
    for item in listings:
        data_list.append({
            'symbol': item['symbol'],
            'name': item['name'],
            'price': item['quote'][currency_price_unit]['price'],
            'percent_change_1h': item['quote'][currency_price_unit]['percentChange1h'],
            'percent_change_24h': item['quote'][currency_price_unit]['percentChange24h'],
            'percent_change_7d': item['quote'][currency_price_unit]['percentChange7d'],
        })

    df = pd.DataFrame(data_list)
    return df

# Load data
df = load_data()

#---------------------------------#
# Sidebar - Cryptocurrency selection
sorted_coin = sorted(df['symbol'])
selected_coin = st.sidebar.multiselect('Cryptocurrency', sorted_coin, sorted_coin)

# Filter data based on selection
df_selected_coin = df[df['symbol'].isin(selected_coin)]

# Number of coins to display
num_coin = st.sidebar.slider('Display Top N Coins', 1, 100, 100)
df_coins = df_selected_coin.head(num_coin)

#---------------------------------#
# Display data
st.subheader('Price Data of Selected Cryptocurrencies')
st.write(f'Data Dimension: {df_selected_coin.shape[0]} rows and {df_selected_coin.shape[1]} columns.')
st.dataframe(df_coins)

# Download data as CSV
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Encode to Base64
    href = f'<a href="data:file/csv;base64,{b64}" download="crypto.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_coin), unsafe_allow_html=True)

#---------------------------------#
# Percent change analysis
st.subheader('Table of % Price Change')
df_change = df_coins[['symbol', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d']].set_index('symbol')
df_change['positive'] = df_change['percent_change_7d'] > 0
st.dataframe(df_change)

# Bar plot of % price change
st.subheader('Bar plot of % Price Change')
df_change = df_change.sort_values(by=['percent_change_7d'])

plt.figure(figsize=(10, 5))
df_change['percent_change_7d'].plot(
    kind='barh',
    color=df_change['positive'].map({True: 'g', False: 'r'})
)
st.pyplot(plt)

