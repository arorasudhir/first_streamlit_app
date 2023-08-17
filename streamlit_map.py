import pandas
import streamlit as st

data = pandas.read_csv('users_location.csv')

st.header('Where our Users come from?')
st.slider('User Count' 0, 10)

st.map(data, zoom=1)
