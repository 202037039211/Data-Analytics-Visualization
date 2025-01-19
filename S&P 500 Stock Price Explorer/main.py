import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import yfinance as yf

#---------------------------------#
# Title and Description
st.title('S&P 500 Stock App')
st.markdown("""
This app retrieves the list of **S&P 500 companies** from Wikipedia and their corresponding **year-to-date stock closing prices**.
* **Python libraries:** pandas, streamlit, matplotlib, yfinance
* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
""")

#---------------------------------#
# Sidebar Layout
st.sidebar.header('User Input Features')

# Load and cache S&P 500 data
@st.cache_data
def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    df = pd.read_html(url, header=0)[0]
    return df

# Load data and group by sector
df = load_data()

# Sidebar - Sector selection
sorted_sector_unique = sorted(df['GICS Sector'].unique())
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# Filter data based on user selection
df_selected_sector = df[df['GICS Sector'].isin(selected_sector)]

# Display data
st.header('Companies in Selected Sector(s)')
st.write(f'Data Dimension: {df_selected_sector.shape[0]} rows and {df_selected_sector.shape[1]} columns.')
st.dataframe(df_selected_sector)

# CSV Download Function
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_sector), unsafe_allow_html=True)

#---------------------------------#
# Retrieve and plot stock data
def price_plot(symbol):
    stock_data = yf.download(symbol, period="ytd")
    
    # Create plot
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(stock_data.index, stock_data['Close'], label='Close Price', color='skyblue')
    ax.fill_between(stock_data.index, stock_data['Close'], color='skyblue', alpha=0.3)
    ax.set_title(symbol, fontsize=14)
    ax.set_xlabel('Date')
    ax.set_ylabel('Closing Price')
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Sidebar - Number of companies to display
num_company = st.sidebar.slider('Number of Companies to Display', 1, 5)

# Show plots for selected companies
if st.button('Show Plots'):
    st.header('Stock Closing Prices')
    for i in df_selected_sector['Symbol'][:num_company]:
        price_plot(i)
