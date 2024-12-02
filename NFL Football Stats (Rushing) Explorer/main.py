import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('NFL Football Stats (Rushing) Explorer')

st.markdown("""
This app performs simple web scraping of NFL player rushing stats!
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")

# Sidebar for user inputs
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990, 2024))))

# Function to load data with caching for performance
@st.cache_data
def load_data(year):
    url = f"https://www.pro-football-reference.com/years/{year}/rushing.htm"
    try:
        html = pd.read_html(url, header=1)  # Extract HTML tables
        df = html[0]
        df = df.dropna(how='all')  # Remove empty rows
        return df
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return pd.DataFrame()

# Load player stats for the selected year
playerstats = load_data(selected_year)

if not playerstats.empty:
    # Sidebar filters: Team and Position selection
    team_column = [col for col in playerstats.columns if 'Tm' in col or 'team' in col.lower()][0]
    sorted_unique_team = sorted(playerstats[team_column].dropna().unique())
    selected_team = st.sidebar.multiselect('Team', sorted_unique_team, sorted_unique_team)
    
    unique_pos = ['RB', 'QB', 'WR', 'FB', 'TE']
    selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)
    
    # Filter data based on user selection
    df_selected_team = playerstats[(playerstats[team_column].isin(selected_team)) & 
                                   (playerstats['Pos'].isin(selected_pos))]
    
    # Display filtered data
    st.header('Display Player Stats of Selected Team(s)')
    st.write(f'Data Dimension: {df_selected_team.shape[0]} rows and {df_selected_team.shape[1]} columns.')
    st.dataframe(df_selected_team)
    
    # Function to download filtered data as CSV
    def filedownload(df):
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # Encode to Base64
        href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
        return href
    
    st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)
    
    # Generate and display an intercorrelation heatmap
    if st.button('Intercorrelation Heatmap'):
        st.header('Intercorrelation Matrix Heatmap')
        
        numeric_df = df_selected_team.select_dtypes(include=[np.number])  # Select only numeric columns
        
        if numeric_df.empty:
            st.error("No numeric data available for correlation heatmap.")
        else:
            corr = numeric_df.corr()
            
            mask = np.triu(np.ones_like(corr, dtype=bool))  # Mask the upper triangle
            with sns.axes_style("white"):
                f, ax = plt.subplots(figsize=(7, 5))
                sns.heatmap(corr, mask=mask, vmax=1, square=True, annot=True, ax=ax, cmap='coolwarm')
            
            st.pyplot(f)

else:
    st.warning("No data available for the selected year.")
