"""Generates meme from a given image."""

from PIL import Image, ImageDraw, ImageFont
import os
import random


class MemeEngine():
    """Generates meme from a given image."""

    def __init__(self, output_dir: str):
        """Instantiate a MemeGenerator object."""
        os.makedirs(output_dir, exist_ok=True)
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500):
        """Create a meme given image, qoute's body and qoute's author."""
        try:
            img = Image.open(img_path)
        except FileNotFoundError:
            print("The file to make meme cant be found")
            exit(1)

        ratio = img.size[1] / img.size[0]
        height = int(width * ratio)
        img = img.resize((width, height))

        drawing_instance = ImageDraw.Draw(img)
        font = ImageFont.truetype('./fonts/arial.ttf', 26)

        drawing_instance.text((2, 2), text, font=font)
        drawing_instance.text((30, 30), author, font=font)

        path = os.path.join(self.output_dir, f'{random.randint(0, 9999)}.jpg')
        img.save(path)
        return path
