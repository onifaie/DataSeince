from msilib.schema import Icon
import streamlit as st



im = Image.open("Data\pic.jpg")
st.set_page_config(
    page_title="Table Activity ",
    page_icon=im,
    Icon=''
    layout="wide",
)

st.title('this application about images Chooes picture by camera ')

col1,col2=st.columns(2)

col1.camera_input('take this picture')
import time


col1 = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    col1.progress(percent_complete + 1)