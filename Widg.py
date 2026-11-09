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

TYPING_DELAY = 0.04   # seconds between updates
CHARS_PER_STEP = 2    # characters added per update

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
