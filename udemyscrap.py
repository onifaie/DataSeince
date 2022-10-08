from html.parser import HTMLParser
import streamlit as st
import  pandas as pd 
import requests
# import plotly.figure_factory as ff
# import plotly.express as px             
#
from bs4 import BeautifulSoup  
import numpy as np
import random
# import matplotlib.pyplot as plt
import time



st.title('obeid web scraping the NONNNNNNN  website ..... ')






st.subheader('This web Scraping for Watch Markting  ....')
with st.sidebar:
    st.sidebar.image("https://avatars.githubusercontent.com/u/31520330?v=4", use_column_width=True,width=3)
    st.write('## this my Data Secince Projects ')
    option = st.selectbox('chooes',['guess', 'casio','coach','fossil','titan',''])


    
    
    
    CourseType = st.selectbox(
    'chooes the  type Of Courses  ',
    ('Select Of Course ', 'python', 'JavaScript','ASP.net','Oracle'))

    st.write('You selected:', CourseType)


df = pd.DataFrame([])

data=[]




    
    # url="https://www.udemy.com/courses/search/?price=price-free&q=python+&sort=relevance&src=ukw"
url=(f"https://www.noon.com/saudi-en/fashion/women-31229/womens-watches/wrist-watches-20504/{option}/watches-store/?f%5Bfashion_department%5D=women&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc&gclid=CjwKCAjw7eSZBhB8EiwA60kCW4Yuxdvxd5mDvyOgQCUelmsgdzaKjv4uT7t5IT2A-_LYfwulED_8FBoC63UQAvD_BwE&utm_campaign=C1000035432N_sa_ar_web_on_go_s_ex_cb_nbr_c1000088l_&utm_medium=cpc&utm_source=c1000088L")
    # url="https://www.futurelearn.com/courses" 
res=requests.get(url)

# st.write(res)
content=BeautifulSoup(res.content,'html.parser')
    # st.code(content)
    # all_courses=content.find_all('div',class_='Content-wrapper_1O_KH')
watches=content.find_all('div',class_='sc-f8165ac8-15 bkbUJe')
count=0
count_price=0

    # st.code(all_courses)
    # st.write(all_courses)
for watch in watches:
        watch_name=watch.find('div',class_='WwCBf').text
        watch_price=watch.find('strong').text
        # watch_rate=watch.find('span',class_='ratingValue') 
        
        count+=1

        dict = {'id':count,'watch_name' : watch_name,
            'price' : watch_price,
                    #   'Rate' : watch_rate
                            }
        df = df.append(dict,ignore_index=True)
st.write(df)    

# data['total'] = pd.to_numeric(df['price']).sum()


# st.write(data)      

        
        
        
        
        # st.write("====================================")
        # st.write(course_name)
        # course_atuore=course.find('span',class_='udlite-sr-only')
        # course_rate=course.find('span',class_='star-rating--medium--17tJo')


st.write(' # You selected:', option)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.video('https://www.youtube.com/watch?v=uuOqshuLmaU&t=74s') 

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

st.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})

# this start charting 
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

 
#this python and free 
#https://www.udemy.com/courses/search/?price=price-free&q=python+&sort=relevance&src=ukw



