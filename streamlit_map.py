import pandas
import folium
import streamlit as at
from streamlit_folium import st_folium
import snowflake.connector

st.set_page_config(layout="wide")

data = pandas.read_csv('users_location.csv')

st.header('Where our Customers come from?')
st.map(data, zoom=7.5)
