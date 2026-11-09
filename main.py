import base64
import html
import time

import streamlit as st
import streamlit.components.v1 as components

# Must be the first Streamlit call, and only called once
st.set_page_config(page_title="Special Greeting", layout="wide")

# ---------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------
def img_to_base64(path: str) -> str:
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


# Each components.html call renders in its own iframe, so the page CSS
# can't reach it. This template carries its own styles.
TYPING_IFRAME_TEMPLATE = """
<head>
    <meta name="color-scheme" content="light">
</head>
<body>
    <div class="typing-box">
        <div id="code">
            <p class="say">__TEXT__</p>
        </div>
    </div>

    <style>
        html, body { margin: 0; background: transparent !important; }
        .typing-box {
            width: 100%;
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            background: none;
        }
        #code .say {
            text-align: center;
            color: white;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 18px;
            margin: 0;
            opacity: 0;
            white-space: pre-wrap;
        }
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
        const TYPING_SPEED = 80;
        const LINE_DELAY = 1000;

        function typeLine(element, fullText) {
            return new Promise(resolve => {
                element.style.opacity = 1;
                element.classList.add('cursor');
                element.textContent = '';

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


def typing_iframe(text: str, height: int = 160):
    components.html(
        TYPING_IFRAME_TEMPLATE.replace("__TEXT__", html.escape(text)),
        height=height,
    )


# ---------------------------------------------------------------
# Page background
# ---------------------------------------------------------------
image_path = r"Gemini_Generated_Image_lyf48xlyf48xlyf4.jpg"
encoded_image = img_to_base64(image_path)

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

/* Make the components.html iframes fully transparent (no backdrop behind the text) */
iframe {{
    background: transparent !important;
    color-scheme: light;
}}
</style>
"""

st.markdown(page_element, unsafe_allow_html=True)
st.balloons()

col1, col2, col3 = st.columns(3)
time.sleep(2)

# ---------------------------------------------------------------
# col1: typing message (own class name: .typing-box)
# ---------------------------------------------------------------
with col1:
    lines = [
        "This website runs on love, joy, and a little bit of Python🎈",
        "All to celebrate you, my beautiful Arnob🐇💕, Fatma Magdy on your special day ❤",
        "You're not just someone special in my life; you're the reason behind so many of my smiles.",
        "May your day be as beautiful as your heart, filled with endless happiness, sweet moments, and everything that makes you smile. ❤️😘",
        "And remember, no matter what, you'll always have a special place in my heart. ❤️",
    ]
    message = "\n".join(lines)

    TYPING_DELAY = 0.1   # seconds between updates
    CHARS_PER_STEP = 1   # characters added per update

    st.markdown(
        """
        <style>
            .typing-box {
                width: 100%;
                max-width: 600px;
                margin: 16px auto;
                padding: 30px;
                box-sizing: border-box;
                background: rgba(59, 60, 54, 0.6);
                border-radius: 15px;
                height: auto;
                min-height: 50px;
            }
            .typing-box h1 {
                color: #bef264;
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

    def render_box(text: str, typing: bool) -> str:
        safe = html.escape(text).replace("\n", "<br>")
        cursor_class = " cursor" if typing else ""
        return (
            '<div class="typing-box">'
            "<h1>Fatma Magdy's Birthday!</h1>"
            f'<div class="typed-text{cursor_class}">{safe}</div>'
            "</div>"
        )

    placeholder = st.empty()
    chars = list(message)  # keeps emojis intact

    for i in range(CHARS_PER_STEP, len(chars) + CHARS_PER_STEP, CHARS_PER_STEP):
        placeholder.markdown(
            render_box("".join(chars[:i]), typing=True), unsafe_allow_html=True
        )
        time.sleep(TYPING_DELAY)

    # Final render without the blinking cursor
    placeholder.markdown(render_box(message, typing=False), unsafe_allow_html=True)

# ---------------------------------------------------------------
# col2: iframe typing text
# ---------------------------------------------------------------
with col2:
    time.sleep(2)
    typing_iframe(
        "Level 26: New Skills, New Wins, Same Awesome You ❤\n"
        "Time to Shine, Laugh, and Make Everyone Jealous of Your Awesomeness😉️",
        height=200,
    )

# ---------------------------------------------------------------
# col3: image
# ---------------------------------------------------------------
with col3:
    time.sleep(11)
    img_base64 = img_to_base64(r"aa.jpg")

    st.markdown(
        f"""
        <style>
        .box-image {{
            width: 92%;
            max-height: 460px;
            margin: 16px;
            object-fit: cover;
            border-radius: 15px;
        }}
        </style>
        <img src="data:image/jpeg;base64,{img_base64}" class="box-image">
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------------
# Bottom caption
# ---------------------------------------------------------------
time.sleep(1)
typing_iframe(
    "Software engineer powered by algorithms, coffee, and questionable programming skills 😝",
    height=140,
)

time.sleep(4)
st.balloons()
