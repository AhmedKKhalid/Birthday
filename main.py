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


image_path = r"Gemini_Generated_Image_lyf48xlyf48xlyf4.jpg"

with open(image_path, "rb") as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode()

page_element = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("data:image/jpeg;base64,{encoded_image}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background-color: rgba(0,0,0,0);
}}

[data-testid="stAppViewContainer"] > .main {{
    background-color: transparent;
}}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)
st.balloons()




col1, col2,col3 = st.columns(3)
time.sleep(2)

with col1:
    #components.html(wd.html_code, height=550)
    import html
    import time
    import streamlit as st
    
    st.set_page_config(page_title="Special Greeting", layout="centered")
    
    # ---------------------------------------------------------------
    # Message (edit the text here)
    # ---------------------------------------------------------------
    lines = [
        "This website runs on love, joy, and a little bit of Python🎈",
        "All to celebrate you, my beautiful Arnob🐇💕, Fatma Magdy on your special day ❤",
        "You're not just someone special in my life; you're the reason behind so many of my smiles.",
        "May your day be as beautiful as your heart, filled with endless happiness, sweet moments, and everything that makes you smile. ❤️😘",
        "And remember, no matter what, you'll always have a special place in my heart. ❤️",
    ]
    message = "\n".join(lines)
    
    TYPING_DELAY = 0.1   # seconds between updates
    CHARS_PER_STEP = 1    # characters added per update
    
    # ---------------------------------------------------------------
    # Styles (rendered directly in the page, NOT in an iframe,
    # so the box grows naturally with its content)
    # ---------------------------------------------------------------
    st.markdown(
        """
        <style>
            .container-box {
                width: 100%;
                max-width: 600px;
                margin: 16px auto;
                padding: 30px;
                box-sizing: border-box;
                background: rgba(59, 60, 54, 0.6);
                border-radius: 15px;
                height: auto;            /* grows with the text */
                min-height: 50px;
            }
            .container-box h1 {
                color: #bef264;          /* lime */
                font-size: 1.5rem;
                font-weight: 800;
                text-align: center;
                margin: 0 0 12px 0;
                padding: 0;
            }
            .typed-text {
                color: #f3f4f6;
                font-family: 'Consolas', 'Courier New', monospace;
                font-size: 1.125rem;
                line-height: 1.5;
                white-space: pre-wrap;
                word-break: break-word;
            }
            .cursor::after {
                content: '|';
                color: #fcd34d;
                animation: blink 1s step-start infinite;
            }
            @keyframes blink { 50% { opacity: 0; } }
        </style>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------
# Typing animation: re-render the box with a bit more text each step
# ---------------------------------------------------------------
    def render_box(text: str, typing: bool) -> str:
        safe = html.escape(text).replace("\n", "<br>")
        cursor_class = " cursor" if typing else ""
        return (
            '<div class="container-box">'
            "<h1>Fatma Magdy's Birthday!</h1>"
            f'<div class="typed-text{cursor_class}">{safe}</div>'
            "</div>"
        )
    
    placeholder = st.empty()
    chars = list(message)  # keeps emojis intact
    
    for i in range(CHARS_PER_STEP, len(chars) + CHARS_PER_STEP, CHARS_PER_STEP):
        placeholder.markdown(render_box("".join(chars[:i]), typing=True), unsafe_allow_html=True)
        time.sleep(TYPING_DELAY)
    
    # Final render without the blinking cursor
    placeholder.markdown(render_box(message, typing=False), unsafe_allow_html=True)
with col2:
   # time.sleep(38)
    components.html(
   """
       <body>

    <div class="container-box">
        <!-- Content Container -->

        <div id="code">
            <!-- Each line is wrapped in a paragraph for sequential animation -->
            <p class="say">Level 26: New Skills, New Wins, Same Awesome You ❤\nTime to Shine, Laugh, and Make Everyone Jealous of Your Awesomeness😉️</p>
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

    time.sleep(11)
    def img_to_base64(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()


    img_base64 = img_to_base64(r"aa.jpg" )
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

time.sleep(1)
components.html(
    """
        <body>

     <div class="container-box">
         <!-- Content Container -->

         <div id="code">
             <!-- Each line is wrapped in a paragraph for sequential animation -->
             <p class="say"> Software engineer powered by algorithms, coffee, and questionable programming skills 😝</p>
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
time.sleep(4)
st.balloons()
