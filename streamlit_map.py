import pandas
import streamlit

data = pandas.read_csv('users_location.csv')

streamlit.header('Where our Users come from?')
streamlit.map(data, zoom=3)
