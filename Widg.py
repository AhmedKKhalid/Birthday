html_code = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Special Greeting</title>
    <!-- Load Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        /* Define the custom font and basic body styles */
        body {
            font-family: 'Inter', sans-serif;
            display: flex;
        }
        
        /* Custom styles for the transparent container */
        .container-box {
            width: 100%;
            max-width: 600px; /* Limit max width on large screens */
            min-height: 50px; /* Set a minimum height instead of fixed 500px */
            background: rgba(59, 60, 54, 0.6); /* Semi-transparent dark green/gray */
            border-radius: 15px;
            overflow: hidden;
            padding: 30px; /* Increased padding slightly for better look */
            justify-content: flex-start; /* Ensure content starts from the top, removing vertical centering */
            margin: 16px; /* Added margin for mobile safety */
        }

        /* Styling for the content area */
        #code {
            color: #f3f4f6; /* Light gray text */
            font-family: 'Consolas', 'Courier New', monospace; /* Monospace font for "typing" look */
            white-space: pre-wrap; /* Allows line breaks */
            line-height: 1.5; /* ADJUSTED: Reduced from 1.8 to 1.5 for tighter line spacing */
            font-size: 1.125rem; /* text-lg */
            margin-tio: 0px;
        }
        
        /* Hidden initially, revealed by JS */
        .say {
            display: block;
            opacity: 0;
        }

        /* The cursor effect */
        .cursor::after {
            content: '|';
            animation: blink 1s step-start infinite;
            color: #fcd34d; /* Yellow cursor */
        }

        @keyframes blink {
            50% { opacity: 0; }
        }
    </style>
</head>
<body>

    <div class="container-box">
        <!-- Content Container -->
        <h1 class="h1-title text-2xl font-extrabold text-lime-300 mb-3 text-center">Fatma Magdy's Birthday!</h1>

        <div id="code">
            <!-- Each line is wrapped in a paragraph for sequential animation -->
            <p class="say">This website runs on love, joy, and a little bit of JavaScript🎈\nAll to celebrate you, "Fatma Magdy" on your special day ❤\nWhile we are always friends ❤  \nHope your day is filled with smiles, good vibes, and everything that makes you happiest ❤️😘</p>
        </div>
    </div>

    <script>
        // Use a standard async function for the typing effect, replacing the old Jscex/typewriter logic.
        
        // Define the typing speed in milliseconds
        const TYPING_SPEED = 50; // Delay between characters
        const LINE_DELAY = 1000; // Delay between lines

        /**
         * Simulates the typing of a single line.
         * @param {HTMLElement} element The paragraph element to type into.
         * @param {string} fullText The complete text content.
         * @returns {Promise<void>} A promise that resolves when the line is fully typed.
         */
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

        /**
         * Initiates the sequence of typing all lines.
         */
        async function startTypingAnimation() {
            const lines = document.querySelectorAll('#code .say');
            
            for (let lineElement of lines) {
                // Get the original content before it's cleared
                const fullText = lineElement.textContent;
                
                // Wait for the current line to finish typing
                await typeLine(lineElement, fullText);
                
                // Wait for a short delay before starting the next line
                await new Promise(resolve => setTimeout(resolve, LINE_DELAY));
            }
        }

        // Start the animation when the window loads
        window.onload = startTypingAnimation;

    </script>
</body>
</html>
"""

# Render HTML inside Streamlit


