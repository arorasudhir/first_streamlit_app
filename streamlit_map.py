import pandas
import folium
import streamlit
from streamlit_folium import st_folium
import snowflake.connector

streamlit.set_page_config(layout="wide")

data = pandas.read_csv('users_location.csv')
user_count = streamlit.slider('User Count', 0, 10000000)
data = data[int(data['USERS']) == user_count]

streamlit.header('Where our Customers come from?')
streamlit.map(data, zoom=7.5)
