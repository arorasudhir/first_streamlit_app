import pandas
import folium
import streamlit as st
from streamlit_folium import st_folium

streamlit.set_page_config(layout="wide")

def init_connection():
    return snowflake.connector.connect(**streamlit.secrets["snowflake"])

conn = init_connection()
cur = conn.cursor()

def get_data():
    with conn.cursor() as cur:
        query = "SELECT * from USERS_LOCATION;"
        cur.execute(query)
        return cur.fetchall()   

st.header('Where our users come from?')
data = get_data()
st.map(data, zoom=7.5)
