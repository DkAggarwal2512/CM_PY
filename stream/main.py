import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt






a ={
    'name':['abc' , 'xyz'],
    'marks': [98,90]
} 




# Mining your data
df = pd.read_csv('marks1.csv')
st.title('This is  Data Mining')

col1, col2, col3 = st.columns(3)
col1.metric("Name", 'Seema')
col2.metric("Marks", 90)

# if st.sidebar.button('Waiting'):df


# df1 = df.drop(['English', 'Social Science'], axis= 'columns')
# st.write(df1)
# st.map(df1)

# if st.button('Load DataSet'):
# if st.sidebar.button('Ok')


if st.sidebar.button('load Description'):
    st.write(df.describe())




# a1 = pd.DataFrame(df['Name'], df['Hindi'])
# st.line_chart(df['Name'], df['Social Science'])


if st.sidebar.button('Load Bar Chart'):
    df2=df.head(20)
    fig= plt.figure(figsize=(10,8))
    plt.bar(df2['Hindi'], df2['Maths'])
    st.pyplot(fig)



# st.dataframe(df)
# st.dataframe(df,height=300, width=500)
st.table(df)# we cant take height width in table
# st.write(a)


# if st.button('Waiting'):df

st.table(a)


#  plots



fig = plt.figure(figsize=(5,3))
# plt.plot(df['Name'], df['Hindi'])
if st.button('Loand BarChart'):df

plt.bar(df['Name'], df['Hindi'])
# plt.show()
st.pyplot(fig)

if st.sidebar.button('hello'): df
