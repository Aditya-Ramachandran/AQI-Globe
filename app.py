import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

final = pd.read_csv('Dataset/AQI and Lat Long of Countries.csv')
final.dropna(inplace=True)




def plot_by_country(dataframe, country, param1, param2):
    temp_df = dataframe[dataframe['Country'] == country]
    fig = px.scatter_mapbox(temp_df, lat='lat', lon='lng', size=param1, color=param2, size_max=20,   mapbox_style='carto-positron', color_continuous_scale= px.colors.sequential.Agsunset_r,
    hover_name=temp_df['City'], height=800, width=900, zoom=4, title='{} vs {} for {}'.format(param1, param2, country))

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



def plot_by_country2(dataframe, country, param1, param2):
    temp_df = dataframe[dataframe['Country'] == country]
    fig = px.scatter_mapbox(temp_df, lat='lat', lon='lng', size=param1, color=param2, size_max=20,   mapbox_style='stamen-toner', color_continuous_scale= px.colors.sequential.Agsunset_r,
    hover_name=temp_df['City'], height=800, width=900, zoom=4, title='{} vs {} for {}'.format(param1, param2, country))

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
    hover_name=temp_df['City'], height=500, width=700, zoom=4)
    
    col1, col2, col3, col4 = st.columns(4)
    st.plotly_chart(fig, use_container_width=True)
    with col1:
        st.metric('Value of {} in {}'.format(param1, city), value=temp_df[param1])
    with col2:
        st.metric('Value of {} in {}'.format(param2, city), value=temp_df[param2])
    with col3:
        st.metric('Latitude of {}'.format(city), value=temp_df['lat'])
    with col4:
        st.metric('Longitude of {}'.format(city), value=temp_df['lng'])


def plot_by_country_city2(dataframe, country,city, param1, param2):
    temp_df = dataframe[(dataframe['Country'] == country) & (dataframe['City'] == city)]
    fig = px.scatter_mapbox(temp_df, lat='lat', lon='lng', size=param1, color=param2, size_max=20, mapbox_style='stamen-toner',
    hover_name=temp_df['City'], height=500, width=700, zoom=4)
    
    col1, col2, col3, col4 = st.columns(4)
    st.plotly_chart(fig, use_container_width=True)
    with col1:
        st.metric('Value of {} in {}'.format(param1, city), value=temp_df[param1])
    with col2:
        st.metric('Value of {} in {}'.format(param2, city), value=temp_df[param2])
    with col3:
        st.metric('Latitude of {}'.format(city), value=temp_df['lat'])
    with col4:
        st.metric('Longitude of {}'.format(city), value=temp_df['lng'])



st.set_page_config(page_title='AQI Index', layout='wide')
st.sidebar.header('AQI Globe')
st.header('AQI Globe')
st.markdown("*Explore air quality index values across different cities worldwide*")
# st.markdown("---")

# if btn == False:


st.markdown("---")





option = st.sidebar.radio('Choose', ['AQI Explorer', 'Learn about AQI Globe'])
if option == 'AQI Explorer':
    country = st.sidebar.selectbox('Select Country', list(sorted(final['Country'].unique())))

    temp_df = final[final['Country'] == country]
    l = list(sorted(temp_df['City'].unique()))
    l.insert(0,'-')
    city = st.sidebar.selectbox('Select a city in {}'.format(country), l)

    primary = st.sidebar.selectbox('Choose primary parameter', final.columns[2:12:2])
    secondary = st.sidebar.selectbox('Choose secondary parameter' ,[cols for cols in final.columns[2:12:2]if cols != primary])
    st.sidebar.markdown('##### *Graph is auto-plotted after parameter selection* ')
    # st.sidebar.markdown('##### *Click View Help for instructions* ')


    btn = st.sidebar.button('View Help',on_click=None)
    if btn == True:
        st.subheader('How to use?')
        st.write('* Select the country from the dropdown.')
        st.write('* For the country overall, select "-" in the city dropdown.')
        st.write('* You can also choose a specific city from the selected country in the city dropdown.')
        st.write('* Select the primary and secondary parameters from their respective dropdowns.')
        st.write('* The primary parameter represents the size of the bubble, and the secondary parameter represents the color of the bubble.')
        st.write('* Scroll below the graph to see more stats of the selected country')

        btn = st.sidebar.button('Hide Help',on_click=None)
        st.markdown("---")

    st.radio('Choose style of graph',['Carto Positron', 'Stamen Toner'], key='graph')
    if st.session_state['graph'] == 'Carto Positron':
        if city == '-':
            plot_by_country(final, country, primary, secondary)
        else:
            plot_by_country_city(final, country,city,primary, secondary)
    else:
        if city == '-':
            plot_by_country2(final, country, primary, secondary)
        else:
            plot_by_country_city2(final, country,city,primary, secondary)


if option == 'Learn about AQI Globe':
    st.subheader('About')
    st.write('AQI Globe is an interactive web application that allows users to explore the air quality index (AQI) values of different cities worldwide. The AQI is a measure of how polluted the air is, and it takes into account several pollutants, such as carbon monoxide, ozone, and particulate matter. The higher the AQI value, the more polluted the air is and the more harmful it can be to human health.')
    st.write('The app uses data from two datasets obtained from Kaggle, which were merged to provide a comprehensive view of AQI values across various countries and cities. The data is presented using Plotly, a Python library for creating interactive data visualizations.')
    st.write('Users can select a country from a dropdown menu and choose between two options: viewing the overall AQI value for the country or selecting a specific city within the country. They can then select primary and secondary parameters from the dropdown menus to customize the graph. The primary parameter is represented by the size of the bubble, while the secondary parameter is represented by the color of the bubble.')
    st.write('The application provides a simple and intuitive way for users to explore AQI values and gain insights into air pollution levels worldwide.')
    st.markdown('---')

    st.subheader('Explanation of common AQI terms')
    st.write('* PM2.5: PM2.5 refers to tiny particles or droplets in the air that are 2.5 micrometers or less in width. They can be harmful to human health when inhaled, especially in high concentrations.')
    st.write('* PM10: PM10 refers to particles or droplets in the air that are 10 micrometers or less in width. They can also be harmful to human health when inhaled, but generally to a lesser extent than PM2.5.')
    st.write('* Ozone: Ozone is a gas that can form in the atmosphere through a chemical reaction between sunlight and other pollutants. High levels of ozone can be harmful to human health, particularly for those with respiratory issues.')
    st.write('* Carbon Monoxide (CO): CO is a colorless, odorless gas that is produced by the incomplete burning of fossil fuels. High levels of CO can be toxic to humans and can cause headaches, dizziness, and nausea')
    st.markdown('---')
    st.subheader('Range of the particulate matter')
    