from optparse import Values
from tkinter.font import names
from tkinter.tix import COLUMN
import matplotlib.pyplot as px
import streamlit as st

import pandas as pd
# import plotly.express as px

df=pd.read_csv('Data/udemy_courses.csv')
# st.dataframe(df)

st.title('this Data analysis for Courses Udemy website ')
subject=df[['subject']]
with st.sidebar:
    myvalue=st.slider('chooes my Slider' ,1,1000)
    # list_subject=st.selectbox('chooes the Subject ',subject).unique()
# myfileds=['price','course_title','num_reviews','course_id','is_paid']
    filter = st.selectbox('filter data', df['subject'].unique())
    
df2=(df[df['subject'] == filter])
st.write(df2[['course_title','price']])
total=(df2.tail(5)['price'].sum(axis=0))
st.text(df2[['subject','price']].sum())
pp=(df2[['price']].value_counts())
st.text( f'this count of how many Times repate this fileds {pp} ')
              
             
if myvalue:
    st.write('this depands of Slider Moving ')
    df2[:myvalue]
             


# mindf2.df2.min()
meandf2=df2.mean()

st.markdown(f'### this my total price for this subject =   { total}' )    
           
# st.text(maxdf2)
st.line_chart(df2[['price']][:7])



# this how disply char pie 
# fig = px.bar(df[['price']])

# plots
# plot1, plot2, plot3 = st.columns((20,1,1))
st.line_chart(df2[['price']][:7])    
# plot3.line_chart(fig)


import numpy as np 
data=np.random.randint(0,20,(3,3))
d=pd.DataFrame(data,index=['A','B','C'],columns=['X','Y','Z'])
st.write(d)
st.subheader('this whats kind of Data in side Datafame' )
st.text(df2.dtypes)
