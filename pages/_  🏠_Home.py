import datetime
import streamlit as st 
import numpy as np 
import pandas as pd 


d=datetime.date(2014,1,1)


st.write('I started Data Analysis:', d)

st.markdown('# Welcome to my Profile Data Science ')
st.text("------------------------------------------------------------------------------------")
col1,col2=st.columns(2)

col1.image('Data\pic.jpg',width=150)

with col2 :
    st.markdown('* working on Data Science ')
    st.markdown('* Developer web application by Django & Python  ') 
    st.markdown('* working on ML For Data Science ')  
    st.markdown('* So tell us whats you Need to Do ..... ')
    
Project1,project2,project3,project4=st.columns(4)

Project1.metric("Temperature", "70 °F", "1.2 °F")
project2.metric("Wind", "9 mph", "-8%")
project3.metric("Humidity", "86%", "4%")
project4.metric("Humidity", "86%", "4%")




with st.expander('# please click here to see More information '):
    Project1,project2=st.columns(2)

    with Project1:
        st.success(' Evertthink id Done when you Ready ')
        st.markdown('*## Everything about how its learn Data Sciences ')
    with project2:
        st.info(' Evertthink id Done when you Ready ')
        st.markdown('* Everything about how its learn Data Sciences ')
    # st.markdown('* Everything about how its learn Data Sciences ') 
    # st.markdown('* Everything about how its learn Data Sciences ')  
    # st.markdown('* Everything about how its learn Data Sciences ')
    
    st.subheader('----------------------------------------------------------------------------')
    mycol1,mycol2,mycol3,mycol4=st.columns(4)
    
    
    mycol1.image('https://www.researchgate.net/publication/342215873/figure/fig1/AS:903149141389313@1592338943641/Figure-1C-Advantages-of-Pie-Chart-Graph-can-be-created-proportionally-to-the.png',"88%")
    mycol2.image('https://www.amcharts.com/wp-content/uploads/2019/02/demo_13290_none-1-1024x690.png',"70%")
    mycol3.image('https://media.istockphoto.com/vectors/business-abstract-infographics-with-3d-pie-info-char-and-graph-bar-vector-id935728880?k=20&m=935728880&s=170667a&w=0&h=iieIsnKVbf2kYoehAz5TAWZbcvALs0cuLWdBTwMxfeg=',"98%")
    mycol4.image('https://images.squarespace-cdn.com/content/v1/55b6a6dce4b089e11621d3ed/1630434647811-2ZYDSKS7D0VH8YI3HX1T/parallel-coordinates-as-an-alternative-to-spider-charts.png',"56%")

    
    st.subheader('this maping about where the almost my works Done ')
    df = pd.DataFrame(
    np.random.randn(200, 2) / [50, 50] + [37.76, -122.4],
    
    columns=['lat', 'lon'])
    #24.819876816608232, 46.72903244104631
    st.map(df)
    
    

    
        