import pandas
import streamlit as st

data = pandas.read_csv('users_location.csv')

user_count = st.slider('User Count', 0, 1000)

data = data[data['USERS'] > user_count]

st.header('Where our Users come from?')
st.map(data, zoom=1)
