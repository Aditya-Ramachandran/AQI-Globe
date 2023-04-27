import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

final = pd.read_csv('Dataset/AQI and Lat Long of Countries.csv')
final.dropna(inplace=True)




def plot_by_country(dataframe, country, param1, param2):
    temp_df = dataframe[dataframe['Country'] == country]
    fig = px.scatter_mapbox(temp_df, lat='lat', lon='lng', size=param1, color=param2, size_max=20,   mapbox_style='carto-positron', color_continuous_scale= px.colors.sequential.Agsunset_r,
    hover_name=temp_df['City'], height=800, width=900, zoom=4)

    st.plotly_chart(fig, use_container_width=True)

    st.subheader('Line chart of {} vs {} for top cities in {}'.format(param1, param2, country))

    col1, col2 =st.columns(2)
    top1 = dataframe[dataframe['Country'] == country][['City',param1]].sort_values(by = param1, ascending=False).head(25)
    top2 = dataframe[dataframe['Country'] == country][['City',param2]].sort_values(by = param2, ascending=False).head(25)

    with col1:
        st.write('Top cities in {} for {}'.format(country, param1))
        st.dataframe(top1)
        # fig1 = px.bar(top1, 'City', param1)
        # st.plotly_chart(fig1)
        
    with col2:
        st.write('Top cities in {} for {}'.format(country, param2))
        st.dataframe(top2)
        
    
    fig1 = px.bar(top1, 'City', param1, title='{} in top cities in {}'.format(param1, country))
    st.plotly_chart(fig1)
    fig2 = px.bar(top2, 'City', param2, title='{} in top cities in {}'.format(param2, country))
    st.plotly_chart(fig2)




def plot_by_country_city(dataframe, country,city, param1, param2):
    temp_df = dataframe[(dataframe['Country'] == country) & (dataframe['City'] == city)]
    fig = px.scatter_mapbox(temp_df, lat='lat', lon='lng', size=param1, color=param2, size_max=20, mapbox_style='carto-positron',
    hover_name=temp_df['City'], height=900, width=1200, zoom=4)
    
    st.plotly_chart(fig, use_container_width=True)
    




st.set_page_config(page_title='AQI Index', layout='wide')
st.sidebar.header('AQI Globe')
option = st.sidebar.radio('Choose', ['Check AQI', 'About the project'])
if option == 'Check AQI':
    country = st.sidebar.selectbox('Select Country', list(sorted(final['Country'].unique())))

    temp_df = final[final['Country'] == country]
    l = list(sorted(temp_df['City'].unique()))
    l.insert(0,'-')
    city = st.sidebar.selectbox('Select a city in {}'.format(country), l)

    primary = st.sidebar.selectbox('Choose primary parameter', final.columns[2:12:2])
    secondary = st.sidebar.selectbox('Choose secondary parameter' ,[cols for cols in final.columns[2:12:2]if cols != primary])
    if city == '-':
        plot_by_country(final, country, primary, secondary)
    else:
        plot_by_country_city(final, country,city,primary, secondary)