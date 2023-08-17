import pandas
import streamlit

streamlit.set_page_config(layout="wide")

data = pandas.read_csv('users_location.csv')

streamlit.header('Where our Users come from?')
streamlit.map(data, zoom=7.5)
