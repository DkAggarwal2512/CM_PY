import streamlit as st 
import pandas as pd
import time
import dateutil
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('mahi.csv')
st.title('My DA project')
if st.checkbox('Display Dataset'):st.write(df)
if st.button('display description'):st.write(df.describe())

#st.radio('Gender',['Female','Male','Other'])
st.multiselect('Gender',['Female','Male','Other']) 
st.date_input('Enter Your Age')
st.balloons()
a = st.slider('select rating',0,10)
b = st.text_input('pick',0,100)

st.progress(10)
with st.spinner('loading....'):time.sleep(5)
st.error('this looks cool...!!')


fig = plt.figure(figsize=(4,4))   #show bar with matplotlib
plt.bar(df['NAME'],df['EMPID'])
st.pyplot(fig)