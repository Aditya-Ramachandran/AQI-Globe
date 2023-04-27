import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.set_page_config(page_title='AQI Index', layout='wide')
st.sidebar.header('AQI Globe')
option = st.sidebar.radio('Choose', ['Check AQI', 'About the project'])
