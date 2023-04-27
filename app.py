import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

final = pd.read_csv('Dataset/AQI and Lat Long of Countries.csv')
final.dropna(inplace=True)

st.set_page_config(page_title='AQI Index', layout='wide')
st.sidebar.header('AQI Globe')
option = st.sidebar.radio('Choose', ['Check AQI', 'About the project'])
if option == 'Check AQI':
    country = st.sidebar.selectbox('Select Country', list(sorted(final['Country'].unique())))
    temp_df = final[final['Country'] == country]
    city = st.sidebar.selectbox('Select a city in {}'.format(country), list(sorted(temp_df['City'].unique())))