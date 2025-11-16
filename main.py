# This is a sample Python script.
import os



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import streamlit.components.v1 as components
import Widg as wd
import time
st.set_page_config(layout="wide")

page_element="""
<style>
[data-testid="stAppViewContainer"]{
  background-image: url("https://images.pexels.com/photos/696271/pexels-photo-696271.jpeg");
  background-size: cover;
}
[data-testid="stHeader"]{
  background-color: rgba(0,0,0,0);
}
</style>
"""



st.markdown(page_element, unsafe_allow_html=True)
st.balloons()

col1, col2,col3 = st.columns(3)

with col1:
    components.html(wd.html_code, height=550)
with col2:
    pass
with col3:
    import base64


    def img_to_base64(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()


    img_base64 = img_to_base64(r"aa.jpg")
#C:\Users\Levi\PycharmProjects\pythonProject1\aa.jpg
    st.markdown(f"""
    <img src="data:image/jpeg;base64,{img_base64}" class="box-image">
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    .container-box {
        width: 100%;
        max-width: 600px;
        min-height: 50px;
        max-height: 400px;
        background: rgba(59, 60, 54, 0.6);
        border-radius: 15px;
        overflow: hidden;
        padding: 30px;
        margin: 16px;
    }

    .box-image {
        width: 100%;
        max-height: 460px;
       margin: 16px;
        object-fit: cover;
        border-radius: 15px;
         padding-left: 30px;
         padding-right: 30px;

    }
    </style>
    """, unsafe_allow_html=True)
st.balloons()