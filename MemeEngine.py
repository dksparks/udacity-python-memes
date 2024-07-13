from PIL import Image, ImageDraw, ImageFont
from os import makedirs
import os.path
import random
import string


class MemeEngine:
    """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""

    def __init__(self, output_dir):
        """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""
        try:
            makedirs(output_dir)
        except FileExistsError:
            pass
        self.output_dir = output_dir

    def make_meme(
        self, img_path: str, text: str, author: str, width=500,
    ) -> str:
        """XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"""
        try:
            img = Image.open(img_path)
        except FileNotFoundError:
            print(f'The image {img_path} could not be found.')
            return
        input_width, input_height = img.size
        if input_width > width:
            height = int(input_height * width / input_width)
            img.resize((width, height))
        full_text = f'"{text}" — {author}'
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(
            './fonts/NotoSans_ExtraCondensed-Black.ttf', size=36
        )
        x, y = map(random.randrange, img.size)
        draw.text((x, y), full_text, font=font, fill='white', anchor='mm')
        out_chars = \
                string.digits + string.ascii_lowercase + string.ascii_uppercase
        out_len = 8
        # Randomly generate output filenames, repeating until we generate one
        # that does not already exist.
        while True:
            out_file = ''.join(random.choices(out_chars, k=out_len)) + '.png'
            out_path = os.path.join(self.output_dir, out_file)
            if not os.path.exists(out_path):
                break
        img.save(out_path)
        return out_path
