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


with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
st.balloons()


st.title('this System about Scrap Data and  analysis  Data ')







st.subheader('this project about how you scrap website depand Fillter by Gatogery ')
with st.sidebar:
    st.image("https://www.arabnews.com/sites/default/files/styles/n_670_395/public/2017/12/13/1052876-894326392.jpg?itok=gtrggN0M", use_column_width=True,width=3)
    st.write('## this my Data Secince Projects ')
    option = st.selectbox('Gatogery ',['electronics-and-mobiles', 'kitchen-and-dining','home-decor','patio-lawn-and-garden','furniture-10180',''])


    
    
    
   

df = pd.DataFrame([])

data=[]




    
    # url="https://www.udemy.com/courses/search/?price=price-free&q=python+&sort=relevance&src=ukw"
# url=(f"https://www.noon.com/saudi-en/all-products/")
url=f"https://www.noon.com/saudi-en/{option}/all-products/?limit=50&sort%5Bby%5D=popularity&sort%5Bdir%5D=desc" 
res=requests.get(url)
# st.write(res)
content=BeautifulSoup(res.content,'html.parser')
    # st.code(content)
    # all_courses=content.find_all('div',class_='Content-wrapper_1O_KH')
watches=content.find_all('div',class_='bkbUJe')
# st.write(watches)
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



# chart_data = pd.DataFrame(df(columns=['a', 'b', 'c']))
st.markdown('''
            ## this chart about how mutch Selling Product every month 
            * this chart about markting years
            * just you can select any Gatogery to show this Data 
            * use the scrap Data on run Time 
            ''')
st._legacy_line_chart(df)

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

st._legacy_line_chart(chart_data)

df = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])

cola1,cola2,cola3=st.columns(3)
cola1.vega_lite_chart(df, {
    'mark': {'type': 'circle', 'tooltip': True},
    'encoding': {
        'x': {'field': 'a', 'type': 'quantitative'},
        'y': {'field': 'b', 'type': 'quantitative'},
        'size': {'field': 'c', 'type': 'quantitative'},
        'color': {'field': 'c', 'type': 'quantitative'},
    },
})
cola2.title('              ')
cola3.markdown('''
            ### this chart about how mutch Selling Product every month 
            * this chart about markting years
            * just you can select any Gatogery to show this Data 
            * use the scrap Data on run Time 
            ''')

# this start charting 
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

 
#this python and free 
#https://www.udemy.com/courses/search/?price=price-free&q=python+&sort=relevance&src=ukw



