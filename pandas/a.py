import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('practice.csv')

st.title('My first pro')
st.write('My dataset')
st.write('df')
st.write('web_app.py')
st.write(df.describe())
a= plt.figure(figsize=(4,4))
plt.plot(df['Name'], df['total'])