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
    from PIL import Image, ImageEnhance
    time.sleep(12)
    # Load the image
    img = Image.open(r"aa.jpg").convert("RGBA")  # Ensure it has an alpha channel
    import base64
    from io import BytesIO

    # Load the image

    # Reduce opacity to 50%
    r, g, b, a = img.split()
    a = a.point(lambda i: i * 0.5)
    img_transparent = Image.merge("RGBA", (r, g, b, a))

    # Resize image to height 300px while keeping aspect ratio
    width = int((400 / img_transparent.height) * img_transparent.width)
    img_resized = img_transparent.resize((width, 600))

    # Convert image to base64 for HTML embedding
    buffered = BytesIO()
    img_resized.save(buffered, format="PNG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    # Display image inside a rounded container
    st.markdown(
        f"""
        <div style="
            border-radius: 15px;
            overflow: hidden;
            width: 100%;
            max-width: 600px; /* Limit max width on large screens */
            min-height: 50px;
            height: 300px;
            padding: 30px; /* Increased padding slightly for better look */
            justify-content: flex-start; /* Ensure content starts from the top, removing vertical centering */

            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
            margin: 16px; /* Added margin for mobile safety */
        ">
            <img src="data:image/png;base64,{img_base64}" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        """,
        unsafe_allow_html=True
    )
st.balloons()