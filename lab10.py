import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')


st.title('California Housing Data(1990) by Yuxuan Tian')
df = pd.read_csv('housing.csv')

Price_filter = st.slider('Maximal Median Housing Price:', 0, 500001, 200000) 

proximity_filter = st.sidebar.multiselect(
     'Choose the location type:',
     df.ocean_proximity.unique(), 
     df.ocean_proximity.unique())  

income_filter = st.sidebar.radio('Choose income level:',('Low','Median','High'))

df = df[df.median_house_value <= Price_filter]

df = df[df.ocean_proximity.isin(proximity_filter)]

if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'Median':
    df = df[df.median_income >= 2.5]
    df = df[df.median_income <= 4.5]
elif income_filter == 'High':
    df = df[df.median_income >= 4.5]

st.subheader('See more filters in the sidebar:')
st.map(df)

st.subheader('Histogram of the median house value')
fig, ax = plt.subplots(figsize=(20, 5))
df['median_house_value'].plot.hist(bins=30)
st.pyplot(fig)