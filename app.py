import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

final = pd.read_csv('Dataset/AQI and Lat Long of Countries.csv')
final.dropna(inplace=True)
l = list(sorted(final['City'].unique()))
l.insert(0,'-')



def plot_by_country(dataframe, country, param1, param2):
    temp_df = dataframe[dataframe['Country'] == country]
    fig = px.scatter_mapbox(temp_df, lat='lat', lon='lng', size=param1, color=param2, size_max=20,   mapbox_style='carto-positron', color_continuous_scale= px.colors.sequential.Agsunset_r,
    hover_name=temp_df['City'], height=800, width=900, zoom=4)

    st.plotly_chart(fig, use_container_width=True)

st.set_page_config(page_title='AQI Index', layout='wide')
st.sidebar.header('AQI Globe')
option = st.sidebar.radio('Choose', ['Check AQI', 'About the project'])
if option == 'Check AQI':
    country = st.sidebar.selectbox('Select Country', list(sorted(final['Country'].unique())))
    temp_df = final[final['Country'] == country]
    city = st.sidebar.selectbox('Select a city in {}'.format(country), l)
    primary = st.sidebar.selectbox('Choose primary parameter', final.columns[2:12:2])
    secondary = st.sidebar.selectbox('Choose secondary parameter' ,[cols for cols in final.columns[2:12:2]if cols != primary])
    if city == '-':
        plot_by_country(final, country, primary, secondary)
    else:
        st.write('pass')