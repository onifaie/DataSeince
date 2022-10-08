import streamlit as st


st.title('Scarp_Markting Jomula ....')

with st.sidebar:
    option=st.selectbox('chooes Brand' ,['Watch','Cloth','Helth'])
    st.button('Save to CSV File ')