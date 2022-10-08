from click import option
import pandas as pd 
import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('Data/amazon_reviews.csv')






st.write(df.head(5))

#creating a sample array

a = np.random.normal(1, 1, size=50)



#specifying the figure to plot 

fig, x = plt.subplots()

x.hist(a, bins=10)



#plotting the figure

st.pyplot(fig)

# loadData(df)