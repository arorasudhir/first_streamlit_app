import pandas
import folium
import streamlit
from streamlit_folium import st_folium

streamlit.set_page_config(layout="wide")

def init_connection():
    return snowflake.connector.connect(**streamlit.secrets["snowflake"])

conn = init_connection()
cur = conn.cursor()

def get_data():
    with conn.cursor() as cur:
        query = "SELECT * from USERS_LOCATION limit 1000;"
        cur.execute(query)
        return cur.fetchall()   

streamlit.header('Where our users come from?')
data = get_data()
streamlit.map(data, zoom=7.5)
