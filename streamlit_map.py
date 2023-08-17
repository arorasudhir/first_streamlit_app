import pandas
import streamlit as st

data = pandas.read_csv('users_location.csv')

st.header('Where our Users come from?')
user_count = st.slider('User Count' 0, 1000)

st.map(data, zoom=1)
