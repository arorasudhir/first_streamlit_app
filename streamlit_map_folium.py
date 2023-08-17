import pandas
import folium
import streamlit
from streamlit_folium import st_folium

streamlit.set_page_config(layout="wide")

data = pandas.read_csv('users_location_sample.csv')

streamlit.header('Where our Customers come from?')
map = folium.Map(location=[47.116386, -101.299591], zoom_start=1)

for index, row in data.iterrows():
    folium.Marker(location=[row["LATITUDE"], row["LONGITUDE"]],
                    popup=row['USERS'],
                    tooltip=f"Users: {(row['USERS'])}",
                    icon=folium.Icon(color='green')
                ).add_to(map)

st_folium(map, width=1200, height=400)
