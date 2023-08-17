import pandas
import folium
import streamlit
from streamlit_folium import st_folium
import snowflake.connector

streamlit.set_page_config(layout="wide")

data = pandas.read_csv('users_location.csv')

streamlit.header('Where our Users come from?')
streamlit.map(data, zoom=7.5)
