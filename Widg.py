import math
import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------
# 1) The message (edit the text here)
# ---------------------------------------------------------------
lines = [
    "This website runs on love, joy, and a little bit of Python🎈",
    "All to celebrate you, my beautiful Arnob🐇💕, Fatma Magdy on your special day ❤",
    "You're not just someone special in my life; you're the reason behind so many of my smiles.",
    "May your day be as beautiful as your heart, filled with endless happiness, sweet moments, and everything that makes you smile. ❤️😘",
    "And remember, no matter what, you'll always have a special place in my heart. ❤️",
]
message = "\n".join(lines)

# ---------------------------------------------------------------
# 2) The HTML page (the box grows with the text via height:auto)
# ---------------------------------------------------------------
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Special Greeting</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        html, body {
            margin: 0;
            padding: 0;
            background: transparent;   /* the iframe itself stays invisible */
        }

        body {
            font-family: 'Inter', sans-serif;
            display: flex;
            justify-content: center;
            align-items: flex-start;   /* box keeps its own height, never stretched */
        }

        .container-box {
            width: 100%;
            max-width: 600px;
            height: auto;              /* grows with the text */
            min-height: 50px;
            background: rgba(59, 60, 54, 0.6);
            border-radius: 15px;
            padding: 30px;
            margin: 16px;
            box-sizing: border-box;
        }

        #code {
            color: #f3f4f6;
            font-family: 'Consolas', 'Courier New', monospace;
            white-space: pre-wrap;
            word-break: break-word;
            line-height: 1.5;
            font-size: 1.125rem;
            margin-top: 0;
        }

        .cursor::after {
            content: '|';
            animation: blink 1s step-start infinite;
            color: #fcd34d;
        }

        @keyframes blink { 50% { opacity: 0; } }
    </style>
</head>
<body>
    <div class="container-box">
        <h1 class="text-2xl font-extrabold text-lime-300 mb-3 text-center">Fatma Magdy's Birthday!</h1>
        <div id="code" class="cursor"></div>
    </div>

    <script>
        const TYPING_SPEED = 80;
        const FULL_TEXT = __MESSAGE__;   // injected from Python

        const el = document.getElementById('code');
        const chars = Array.from(FULL_TEXT);   // keeps emojis intact
        let i = 0;

        const timer = setInterval(() => {
            if (i < chars.length) {
                el.textContent += chars[i++];   // the box grows as text is added
            } else {
                clearInterval(timer);
                el.classList.remove('cursor');
            }
        }, TYPING_SPEED);
    </script>
</body>
</html>
"""

import json
html_code = html_template.replace("__MESSAGE__", json.dumps(message))

# ---------------------------------------------------------------
# 3) Iframe height: tall enough for the FULL text.
#    The iframe is transparent, so the visible box still grows
#    smoothly while typing; this just stops it being clipped.
# ---------------------------------------------------------------
CHARS_PER_LINE = 38      # conservative (narrow screens wrap more)
LINE_HEIGHT_PX = 27      # 1.125rem * 1.5
wrapped_lines = sum(max(1, math.ceil(len(l) / CHARS_PER_LINE)) for l in lines)
frame_height = 60 + 60 + 32 + 40 + wrapped_lines * LINE_HEIGHT_PX  # title + padding + margins + spare

#components.html(html_code, height=frame_height, scrolling=False)
