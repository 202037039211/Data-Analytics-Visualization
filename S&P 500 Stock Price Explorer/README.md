# S&P 500 Stock Price Explorer

This Streamlit application retrieves the list of S&P 500 companies from Wikipedia and visualizes their year-to-date stock closing prices using data from Yahoo Finance.

## Features:
- **Company Data Retrieval**: Fetches the latest S&P 500 company list directly from Wikipedia.
- **Sector Filtering**: Allows users to filter and view companies based on GICS sectors.
- **Stock Price Visualization**:
  - Displays stock closing prices for selected companies.
  - Interactive line charts with historical data for each stock.
- **Download Data**: Export filtered company lists as a CSV file.

## Libraries Used:
- **Python**: Streamlit, pandas, matplotlib, yfinance
- **Data Source**:
  - Company List: [Wikipedia - S&P 500 Companies](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
  - Stock Data: Yahoo Finance (via `yfinance` library)
