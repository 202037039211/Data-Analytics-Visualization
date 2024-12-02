# NBA Player Stats Explorer

This Streamlit app performs web scraping of NBA player statistics from [Basketball-reference.com](https://www.basketball-reference.com/). It provides an interactive interface to explore and analyze player data from any NBA season since 1950.

## Features:
- **Data Selection**: Choose a season and filter players by team and position.
- **Data Visualization**: Display player statistics in a table format.
- **Download Option**: Export filtered data as a CSV file.
- **Heatmap Analysis**: Visualize intercorrelations between numeric stats.

## Libraries Used:
- **Python**: Streamlit, pandas, matplotlib, seaborn, numpy
- **Data Source**: Basketball-reference.com

## How to Run:
1. Clone this repository.
2. Install dependencies:
```bash
pip install streamlit pandas matplotlib seaborn numpy
```
3. Run the Streamlit app:
```bash
streamlit run main.py
```
