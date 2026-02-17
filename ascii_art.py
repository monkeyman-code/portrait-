from PIL import Image

# A dense character set provides the best gradients for B&W
ASCII_CHARS = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

def main():
    path = "my_image.jpg"
    output_file = "portrait.html"
    
    # SETTINGS FOR HIGH DETAIL
    width = 350  
    font_size = "4px" 

    try:
        img = Image.open(path)
        # Convert to 'L' mode immediately (True Grayscale)
        img = img.convert("L") 
    except Exception as e:
        print(f"Error: Could not find or open {path}. {e}")
        return

    # High-Quality Resize
    w_percent = (width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((width, h_size), Image.Resampling.LANCZOS)
    
    pixels = list(img.getdata())
    
    # HTML with a "Digital Print" aesthetic
    # Added a slight text-shadow to make the characters 'glow' like a monitor
    html_output = f"""
    <html>
    <head>
        <title>B&W Code Portrait</title>
        <style>
            body {{
                background-color: #000;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                overflow: auto;
            }}
            .container {{
                font-family: 'Courier New', monospace;
                font-size: {font_size};
                line-height: 0.75;
                letter-spacing: 1.2px;
                white-space: pre;
                color: #fff;
            }}
            span {{
                display: inline-block;
            }}
        </style>
    </head>
    <body>
        <div class="container">"""

    for i, brightness in enumerate(pixels):
        # Map brightness to character
        char_index = int((brightness / 255) * (len(ASCII_CHARS) - 1))
        char = ASCII_CHARS[char_index]
        
        # We use the brightness value to set the text color (shades of gray)
        # This makes the "white" parts of the photo bright and "gray" parts dim
        html_output += f'<span style="color: rgb({brightness},{brightness},{brightness});">{char}</span>'
        
        if (i + 1) % width == 0:
            html_output += "<br>\n"

    html_output += "</div></body></html>"

    with open(output_file, "w") as f:
        f.write(html_output)
    
    print(f"Successfully generated your B&W portrait in '{output_file}'!")

if __name__ == "__main__":
    main()