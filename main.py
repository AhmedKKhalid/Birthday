# This is a sample Python script.
import os



# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import streamlit.components.v1 as components
import Widg as wd
import time
import base64
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
time.sleep(2)

with col1:
    components.html(wd.html_code, height=550)

with col2:
    time.sleep(21)
    components.html(
   """
       <body>

    <div class="container-box">
        <!-- Content Container -->

        <div id="code">
            <!-- Each line is wrapped in a paragraph for sequential animation -->
            <p class="say">Level 25: New Skills, New Wins, Same Awesome You ❤\nTime to Shine, Laugh, and Make Everyone Jealous of Your Awesomeness😉️</p>
        </div>
    </div>

    <style>
        /* Make all text white */
        #code .say {
        text-align: center;
            color: white;  /* text will be white */
            font-family: 'Consolas', 'Courier New', monospace;;
            font-size: 18px;
            opacity: 0; /* initially invisible for animation */
        }

        /* Blinking cursor effect */
        .cursor::after {
            content: '|';
            animation: blink 1s infinite;
        }

        @keyframes blink {
            0%, 50%, 100% { opacity: 1; }
            25%, 75% { opacity: 0; }
        }
    </style>

    <script>
        const TYPING_SPEED = 80; // Delay between characters
        const LINE_DELAY = 1000; // Delay between lines

        function typeLine(element, fullText) {
            return new Promise(resolve => {
                element.style.opacity = 1; // Make the line visible
                element.classList.add('cursor');
                element.textContent = ''; // Clear content for typing effect
                
                let i = 0;
                const interval = setInterval(() => {
                    if (i < fullText.length) {
                        element.textContent += fullText.charAt(i);
                        i++;
                    } else {
                        clearInterval(interval);
                        element.classList.remove('cursor');
                        resolve();
                    }
                }, TYPING_SPEED);
            });
        }

        async function startTypingAnimation() {
            const lines = document.querySelectorAll('#code .say');
            
            for (let lineElement of lines) {
                const fullText = lineElement.textContent;
                await typeLine(lineElement, fullText);
                await new Promise(resolve => setTimeout(resolve, LINE_DELAY));
            }
        }

        window.onload = startTypingAnimation;
    </script>
</body>
 
    """
    , )

with col3:

    time.sleep(15)
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
            width: 60%;
            max-width: 500px; /* Limit max width on large screens */
            min-height: 50px; /* Set a minimum height instead of fixed 500px */
            background: rgba(59, 60, 54, 0.6); /* Semi-transparent dark green/gray */
            border-radius: 15px;
            overflow: hidden;
            padding: 30px; /* Increased padding slightly for better look */
            justify-content: flex-center; /* Ensure content starts from the top, removing vertical centering */
            margin: 16px; /* Added margin for mobile safety */
        }

    .box-image {
        width: 92%;
        max-height: 460px;
       margin: 16px;
        object-fit: cover;
        border-radius: 15px;
 justify-content: flex-center;

    }
    </style>
    """, unsafe_allow_html=True)
st.balloons()