# Cryptocurrency Price Explorer

This Streamlit application retrieves and visualizes cryptocurrency prices for the top 100 coins from CoinMarketCap.

## Features:
- **Real-time Data**: Scrapes the latest cryptocurrency prices from CoinMarketCap.
- **User Filters**: 
  - Select currency unit (USD, BTC, ETH).
  - Choose specific cryptocurrencies to display.
  - Sort and analyze price changes over different time frames (1h, 24h, 7d).
- **Visualizations**:
  - Display price data in table format.
  - Download filtered data as a CSV file.
  - Bar chart to visualize percentage changes in price.

## Libraries Used:
- **Python**: Streamlit, pandas, matplotlib, BeautifulSoup, requests, json
- **Data Source**: [CoinMarketCap](http://coinmarketcap.com)

## How to Run:
1. Clone this repository.
2. Install dependencies:
```bash
pip install streamlit pandas matplotlib beautifulsoup4 requests
```
3. Run the Streamlit app:
```bash
streamlit run main.py
```
