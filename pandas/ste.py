import streamlit as st
import pandas as pd
import time
import dateutil

import matplotlib.pyplot as plt
import numpy as np


st.progress(10)
with st.spinner('loanding....'):time.sleep(2)

# st.balloons()
st.error('This Looks Like')
df=pd.read_csv('marks1.csv')

df= pd.read_csv('details.csv')
st.title(' Welcome My Event')
df1 =df.head(5)
fig=plt.figure(figsize=(7,4))
plt.bar(df['Name'], df['Maths'])
st.pyplot(fig)






st.title('My DashBoard')
if st.checkbox('display dataset'):st.write(df)
if st.button('display'):st.write(df.describe())
st.radio('Gender',['Female', 'MAle', 'Other'])
st.date_input('Enter your Age')
a = st.slider('select rating', 0,10)
d = st.text_input('Enter your name')
st.write(d)
st.number_input('pick', 0,100)
st.multiselect('Proficiency', ['Html', 'Java','Css'])
st.header('dataset')
st.subheader('first')
st.write('Iris')
