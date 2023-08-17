import pandas
import streamlit as st

data = pandas.read_csv('users_location.csv')

st.header('Where our USers come from?')
st.map(data, zoom=1)
