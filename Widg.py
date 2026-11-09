
html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Special Greeting</title>
    <!-- Load Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
            display: flex;
            justify-content: center;   /* center the box horizontally */
            align-items: flex-start;   /* don't stretch it vertically */
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
            /* no overflow:hidden, so nothing gets clipped */
        }
 
        #code {
            color: #f3f4f6;
            font-family: 'Consolas', 'Courier New', monospace;
            white-space: pre-wrap;
            line-height: 1.5;
            font-size: 1.125rem;
            margin-top: 0;
        }
 
        .say {
            display: block;
            opacity: 0;
            margin: 0;
        }
 
        .cursor::after {
            content: '|';
            animation: blink 1s step-start infinite;
            color: #fcd34d;
        }
 
        @keyframes blink {
            50% { opacity: 0; }
        }
    </style>
</head>
<body>
 
    <div class="container-box" id="box">
        <h1 class="h1-title text-2xl font-extrabold text-lime-300 mb-3 text-center">Fatma Magdy's Birthday!</h1>
 
        <div id="code">
            <p class="say">This website runs on love, joy, and a little bit of Python🎈
All to celebrate you, my beautiful Arnob🐇💕, Fatma Magdy on your special day ❤
You're not just someone special in my life; you're the reason behind so many of my smiles.
May your day be as beautiful as your heart, filled with endless happiness, sweet moments, and everything that makes you smile. ❤️😘
And remember, no matter what, you'll always have a special place in my heart. ❤️</p>
        </div>
    </div>
 
    <script>
        const TYPING_SPEED = 80;   // delay between characters (ms)
        const LINE_DELAY = 1000;   // delay between lines (ms)
 
        /** Resize the Streamlit iframe to match the content height. */
        function resizeFrame() {
            const box = document.getElementById('box');
            const height = box.offsetHeight + 40; // box + margins
            try {
                if (window.frameElement) {
                    window.frameElement.style.height = height + 'px';
                    window.frameElement.setAttribute('height', height);
                }
            } catch (e) {
                /* ignore if the iframe can't be accessed */
            }
        }
 
        function typeLine(element, fullText) {
            return new Promise(resolve => {
                element.style.opacity = 1;
                element.classList.add('cursor');
                element.textContent = '';
 
                const chars = Array.from(fullText); // keeps emojis intact
                let i = 0;
                const interval = setInterval(() => {
                    if (i < chars.length) {
                        element.textContent += chars[i];
                        i++;
                        resizeFrame(); // grow as the text grows
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
 
        window.onload = () => {
            resizeFrame();
            startTypingAnimation();
        };
        window.addEventListener('resize', resizeFrame);
    </script>
</body>
</html>
"""
 
# Render HTML inside Streamlit.
# `height` is the starting/fallback height; the script inside the HTML
# resizes the iframe automatically as the text is typed.
#components.html(html_code, height=200, scrolling=False)
