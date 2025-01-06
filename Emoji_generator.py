# Python Code for Custom Emoji Generator
from PIL import Image, ImageDraw, ImageFont # type: ignore
import os

def create_custom_emoji(base_image_path, text, output_path):
    try:
        # Load the base image
        base_image = Image.open(base_image_path).convert("RGBA")

        # Create a drawing context
        draw = ImageDraw.Draw(base_image)

        # Load a font (you may need to provide the path to a .ttf file on your system)
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Adjust for your system
        font = ImageFont.truetype(font_path, 40)

        # Add text to the image
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (base_image.width - text_width) // 2
        text_y = base_image.height - text_height - 10
        draw.text((text_x, text_y), text, font=font, fill="white")

        # Save the modified image
        base_image.save(output_path, "PNG")
        print(f"Custom emoji saved at: {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Input base image and text
    base_image_path = input("Enter the path to the base emoji image (e.g., smiley.png): ")
    text = input("Enter the text for the emoji: ")

    # Output file name
    output_path = "custom_emoji.png"

    # Generate the custom emoji
    create_custom_emoji(base_image_path, text, output_path)
