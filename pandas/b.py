import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('details.csv')
st.title('My Interactive DA Project')
df1= df.head(5)

fig = plt.figure(figsize=(5,5))
plt.scatter(df1['Name'], df1['Maths'])
st.pyplot(fig)



if st.checkbox('display dataset'):st.write(df)
if st.button('display description'):st.table(df.describe())
st.date_input('date of birth')


d = st.text_input('Enter your name')
st.write(d)
st.number_input('pick', 0,100)




st.multiselect('Proficiency', ['HTML', 'CSS', 'JS', 'Java', 'python'])

a = st.slider('select rating', 0,10)
st.write(a)

#'''st.title('My Data Analytics Dashboard')

#if st.button('click to read dataset'):st.write(df)

#if st.checkbox('acknowledge'):st.write('Welcome')'''

