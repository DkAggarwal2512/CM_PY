import streamlit as st
import pandas as pd

a = pd.read_csv('marks.csv')
st.write(a)  
st.title("Student Details") 
st.write(a.describe())




status = st.radio("Select Gender: ", ('Male', 'Female'))
if (status == 'Male'):
	st.success("Male")
else:
	st.success("Female")



    
