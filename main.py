import base64
import html
import random
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

# ---------------------------------------------------------------
# Birthday FX: pure-CSS animation system
#   - @property animated conic-gradient border + gradient title
#   - individual transform properties (translate / rotate / scale)
#     so several animations can drive one element without clashing
#   - 3D confetti, swaying balloons, heartbeat hearts, twinkling stars,
#     aurora blobs, a rainbow wave banner and a cake with flickering
#     candles that blow out and relight
# ---------------------------------------------------------------
FX_CSS = """
<style>
@property --angle { syntax: '<angle>'; initial-value: 0deg; inherits: false; }
@property --hue   { syntax: '<number>'; initial-value: 0;   inherits: true;  }

@keyframes spin-angle { to { --angle: 360deg; } }
@keyframes hue-cycle  { to { --hue: 360; } }

.bd-fx {
    position: fixed; inset: 0; pointer-events: none; overflow: hidden; z-index: 50;
    animation: stage-in 2.5s ease-out both;
}
@keyframes stage-in { from { opacity: 0; } to { opacity: 1; } }

/* ---------- Aurora glow ---------- */
.bd-aurora { z-index: 2; }
.bd-aurora i {
    position: absolute; left: var(--x); top: var(--y);
    width: 55vmax; height: 55vmax; margin: -27vmax 0 0 -27vmax;
    border-radius: 50%;
    background: radial-gradient(circle, hsl(var(--h) 100% 62% / .9), transparent 62%);
    filter: blur(70px);
    mix-blend-mode: screen;
    opacity: .28;
    animation: aurora var(--d) ease-in-out infinite alternate;
}
@keyframes aurora {
    to { translate: var(--dx) var(--dy); scale: 1.35; filter: blur(70px) hue-rotate(90deg); }
}

/* ---------- 3D confetti ---------- */
.bd-confetti b {
    position: absolute; top: -6vh; left: var(--x);
    width: var(--w); height: calc(var(--w) * 1.7);
    background: linear-gradient(135deg, hsl(var(--h) 95% 65%), hsl(calc(var(--h) + 40) 95% 55%));
    animation: fall var(--d) linear var(--delay) infinite,
               tumble var(--s) linear infinite;
}
.bd-confetti b:nth-child(3n) { border-radius: 50%; }
.bd-confetti b:nth-child(5n) { clip-path: polygon(50% 0, 100% 100%, 0 100%); }
@keyframes fall   { from { translate: 0 0; } to { translate: var(--drift) 115vh; } }
@keyframes tumble {
    from { transform: rotate3d(var(--ax), var(--ay), 1, 0deg); }
    to   { transform: rotate3d(var(--ax), var(--ay), 1, 720deg); }
}

/* ---------- Balloons ---------- */
.bd-balloons b {
    position: absolute; left: var(--x); bottom: -35vh;
    width: var(--sz); height: calc(var(--sz) * 1.22);
    border-radius: 50% 50% 48% 48% / 58% 58% 42% 42%;
    background:
        radial-gradient(circle at 32% 26%, rgb(255 255 255 / .8) 0 5%, transparent 20%),
        radial-gradient(circle at 50% 45%, hsl(var(--h) 85% 64%), hsl(var(--h) 80% 44%) 85%);
    box-shadow: inset -10px -12px 20px rgb(0 0 0 / .22),
                0 0 30px hsl(var(--h) 90% 60% / .35);
    transform-origin: 50% calc(100% + var(--sz) * 1.5);
    animation: rise var(--d) linear var(--delay) infinite,
               sway var(--sw) ease-in-out infinite alternate;
}
.bd-balloons b::before {            /* knot */
    content: ''; position: absolute; left: 50%; bottom: -6px;
    width: 10px; height: 9px; margin-left: -5px;
    background: hsl(var(--h) 80% 42%);
    clip-path: polygon(50% 0, 100% 100%, 0 100%);
}
.bd-balloons b::after {             /* string */
    content: ''; position: absolute; left: 50%; top: 100%;
    width: 1.5px; height: calc(var(--sz) * 1.5);
    background: linear-gradient(rgb(255 255 255 / .7), transparent);
    transform-origin: top;
    animation: string-wave 1.2s ease-in-out infinite alternate;
}
@keyframes rise        { from { translate: 0 0; } to { translate: 0 -165vh; } }
@keyframes sway        { from { rotate: -7deg; } to { rotate: 7deg; } }
@keyframes string-wave { from { rotate: -5deg; } to { rotate: 5deg; } }

/* ---------- Hearts ---------- */
.bd-hearts u {
    position: absolute; left: var(--x); bottom: -8vh;
    text-decoration: none; font-size: var(--sz);
    color: hsl(var(--h) 90% 65%);
    filter: drop-shadow(0 0 8px hsl(var(--h) 100% 60% / .9));
    animation: float-heart var(--d) ease-in var(--delay) infinite,
               heartbeat 1s ease-in-out infinite;
}
.bd-hearts u::before { content: '❤'; }
@keyframes float-heart {
    0%   { translate: 0 0; opacity: 0; }
    10%  { opacity: 1; }
    50%  { translate: 3vw -55vh; }
    100% { translate: -3vw -110vh; opacity: 0; }
}
@keyframes heartbeat { 0%, 100% { scale: 1; } 15% { scale: 1.3; } 30% { scale: 1; } 45% { scale: 1.2; } }

/* ---------- Twinkling stars ---------- */
.bd-stars s {
    position: absolute; left: var(--x); top: var(--y);
    width: var(--sz); height: var(--sz); text-decoration: none;
    background: radial-gradient(circle, #fff 0 25%, #fde68a 60%);
    clip-path: polygon(50% 0, 61% 39%, 100% 50%, 61% 61%, 50% 100%, 39% 61%, 0 50%, 39% 39%);
    animation: twinkle var(--d) ease-in-out var(--delay) infinite;
}
@keyframes twinkle {
    0%, 100% { opacity: 0; scale: .2; rotate: 0deg; }
    50%      { opacity: 1; scale: 1;  rotate: 180deg; }
}

/* ---------- Rainbow wave banner ---------- */
.bd-banner {
    position: fixed; top: 6px; left: 0; right: 0; z-index: 52;
    text-align: center; pointer-events: none;
    font: 800 2.1rem 'Segoe UI', system-ui, sans-serif;
    letter-spacing: .12em;
    animation: hue-cycle 8s linear infinite;
}
.bd-banner span {
    display: inline-block;
    color: hsl(calc(var(--hue) + var(--i) * 25) 95% 68%);
    text-shadow: 0 0 12px currentColor, 0 0 30px currentColor;
    animation: wave 1.6s ease-in-out calc(var(--i) * .09s) infinite;
}
@keyframes wave {
    0%, 100% { translate: 0 0;     scale: 1; }
    50%      { translate: 0 -10px; scale: 1.18; }
}

/* ---------- Cake ---------- */
.bd-cake {
    position: fixed; right: 3vw; bottom: 0; width: 190px; height: 190px;
    z-index: 51; pointer-events: none;
    transform-origin: bottom center; scale: .85;
    animation: cake-in 1.4s cubic-bezier(.2, 1.4, .4, 1) both;
}
@keyframes cake-in { from { transform: translateY(120%) rotate(-8deg); } to { transform: none; } }
.bd-cake .plate {
    position: absolute; bottom: 0; left: 0; width: 100%; height: 12px; border-radius: 50%;
    background: linear-gradient(#f5f5f5, #9ca3af); box-shadow: 0 6px 14px rgb(0 0 0 / .4);
}
.bd-cake .l1, .bd-cake .l2 { position: absolute; overflow: hidden; }
.bd-cake .l2 {
    bottom: 8px; left: 15px; width: 160px; height: 68px; border-radius: 10px 10px 6px 6px;
    background: linear-gradient(#7b4a2d, #4b2a17);
}
.bd-cake .l1 {
    bottom: 74px; left: 40px; width: 110px; height: 52px; border-radius: 10px 10px 4px 4px;
    background: linear-gradient(#ff8fb1, #ff5c8a);
}
.bd-cake .l2::before, .bd-cake .l1::before {   /* dripping frosting */
    content: ''; position: absolute; top: 0; left: 0; width: 100%; height: 26px;
    background:
        radial-gradient(circle at 14px 12px, var(--ic) 12px, transparent 13px) 0 0 / 28px 26px repeat-x,
        linear-gradient(var(--ic), var(--ic)) 0 0 / 100% 12px no-repeat;
}
.bd-cake .l2 { --ic: #ffd1e3; }
.bd-cake .l1 { --ic: #fff; }
.bd-cake .l2::after {                           /* sprinkles */
    content: ''; position: absolute; inset: 30px 0 0 0;
    background:
        radial-gradient(circle, #fde047 2px, transparent 3px) 0 0 / 22px 18px,
        radial-gradient(circle, #60a5fa 2px, transparent 3px) 9px 8px / 31px 24px;
}
.bd-cake .candles {
    position: absolute; bottom: 126px; left: 50%; width: 90px; margin-left: -45px; height: 36px;
    display: flex; justify-content: space-between;
}
.bd-cake .candles i {
    position: relative; display: block; align-self: flex-end;
    width: 8px; height: 34px; border-radius: 2px;
    background: repeating-linear-gradient(45deg, #fff 0 5px, #38bdf8 5px 10px);
}
.bd-cake .candles em {
    position: absolute; left: 50%; bottom: 100%; width: 12px; height: 24px;
    margin: 0 0 1px -6px; font-style: normal;
    background: radial-gradient(ellipse at 50% 78%, #fff 0 12%, #ffe066 30%, #ff9f1c 62%, transparent 70%);
    border-radius: 50% 50% 50% 50% / 62% 62% 38% 38%;
    box-shadow: 0 0 18px 6px rgb(255 170 40 / .55);
    transform-origin: 50% 100%;
    animation: flicker .18s ease-in-out infinite alternate,
               relight 12s ease-in-out calc(var(--n) * .25s) infinite;
}
@keyframes flicker { from { transform: skewX(-4deg) scaleY(.92); } to { transform: skewX(4deg) scaleY(1.08); } }
@keyframes relight {
    0%, 78%   { scale: 1;    opacity: 1; }
    82%, 90%  { scale: 0 .1; opacity: 0; }
    96%, 100% { scale: 1;    opacity: 1; }
}

/* ---------- Upgrade the typing box from col1 ---------- */
.typing-box {
    position: relative;
    backdrop-filter: blur(6px);
    animation: glow-pulse 3s ease-in-out infinite alternate;
}
.typing-box::before {                           /* rotating conic-gradient border */
    content: ''; position: absolute; inset: 0; border-radius: inherit; padding: 2px;
    background: conic-gradient(from var(--angle), #f472b6, #fcd34d, #bef264, #60a5fa, #a78bfa, #f472b6);
    -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
    -webkit-mask-composite: xor;
            mask: linear-gradient(#000 0 0) content-box exclude, linear-gradient(#000 0 0);
    pointer-events: none;
    animation: spin-angle 5s linear infinite;
}
.typing-box h1 {                                /* animated gradient title */
    background: linear-gradient(var(--angle), #bef264, #fcd34d, #f472b6, #60a5fa, #bef264);
    -webkit-background-clip: text; background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 10px rgb(244 114 182 / .55));
    animation: spin-angle 4s linear infinite;
}
@keyframes glow-pulse {
    from { box-shadow: 0 0 18px rgb(244 114 182 / .25); }
    to   { box-shadow: 0 0 38px rgb(96 165 250 / .45); }
}
</style>
"""


def build_fx_html(seed: int = 26) -> str:
    rnd = random.Random(seed)
    u = rnd.uniform

    aurora = "".join(
        f'<i style="--h:{h};--x:{x}vw;--y:{y}vh;--dx:{dx}vw;--dy:{dy}vh;--d:{d}s"></i>'
        for h, x, y, dx, dy, d in [
            (320, 15, 20, 30, -20, 26),
            (200, 85, 25, -30, 25, 30),
            (280, 50, 90, 20, -30, 34),
            (50, 10, 85, 25, -15, 28),
        ]
    )

    confetti = "".join(
        f'<b style="--x:{u(0, 100):.1f}vw;--w:{rnd.randint(6, 12)}px;--h:{rnd.randint(0, 360)};'
        f'--d:{u(6, 12):.1f}s;--delay:-{u(0, 12):.1f}s;--s:{u(2, 5):.1f}s;'
        f'--drift:{rnd.randint(-15, 15)}vw;--ax:{u(-1, 1):.2f};--ay:{u(-1, 1):.2f}"></b>'
        for _ in range(70)
    )

    balloons = ""
    for k in range(12):
        d = u(14, 24)
        balloons += (
            f'<b style="--x:{3 + k * 8 + u(-2, 2):.1f}vw;--sz:{rnd.randint(50, 90)}px;'
            f'--h:{rnd.randint(0, 360)};--d:{d:.1f}s;--delay:-{u(0, d):.1f}s;--sw:{u(3, 5):.1f}s"></b>'
        )

    hearts = "".join(
        f'<u style="--x:{u(2, 96):.1f}vw;--sz:{rnd.randint(18, 40)}px;--h:{rnd.choice([340, 350, 320, 0])};'
        f'--d:{u(9, 16):.1f}s;--delay:-{u(0, 14):.1f}s"></u>'
        for _ in range(14)
    )

    stars = "".join(
        f'<s style="--x:{u(0, 98):.1f}vw;--y:{u(0, 95):.1f}vh;--sz:{rnd.randint(8, 18)}px;'
        f'--d:{u(2, 5):.1f}s;--delay:-{u(0, 5):.1f}s"></s>'
        for _ in range(30)
    )

    banner = "".join(
        f'<span style="--i:{i}">{"&nbsp;" if ch == " " else ch}</span>'
        for i, ch in enumerate("HAPPY BIRTHDAY")
    )

    candles = "".join(f'<i style="--n:{n}"><em style="--n:{n}"></em></i>' for n in range(5))
    cake = (
        '<div class="bd-cake"><div class="candles">' + candles + "</div>"
        '<div class="l1"></div><div class="l2"></div><div class="plate"></div></div>'
    )

    return (
        f'<div class="bd-fx bd-aurora">{aurora}</div>'
        f'<div class="bd-fx bd-confetti">{confetti}</div>'
        f'<div class="bd-fx bd-balloons">{balloons}</div>'
        f'<div class="bd-fx bd-hearts">{hearts}</div>'
        f'<div class="bd-fx bd-stars">{stars}</div>'
        f'<div class="bd-banner">{banner}</div>'
        f"{cake}"
    )


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

# ---------------------------------------------------------------
# Launch the birthday FX only now, after every widget has appeared.
# The caption above types for ~7s, so wait for it to finish first.
# ---------------------------------------------------------------
time.sleep(7)
st.markdown(FX_CSS, unsafe_allow_html=True)
st.markdown(build_fx_html(), unsafe_allow_html=True)
st.balloons()
