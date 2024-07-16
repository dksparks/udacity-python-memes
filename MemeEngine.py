from PIL import Image, ImageDraw, ImageFont
from os import makedirs
import os.path
import random
import string


class MemeEngine:
    """A class to add text to images and save the result."""

    def __init__(self, output_dir):
        """Create a new MemeEngine with the provided output directory.

        The directory will be created if it does not exist.

        :param output_dir:
            The output directory in which to save generated images.
        """
        try:
            makedirs(output_dir)
        except FileExistsError:
            pass
        self.output_dir = output_dir

    def make_meme(
        self, img_path: str, text: str, author: str, width=500,
    ) -> str:
        """Generate a new meme image and save it to a randomized name.

        If the provided image is wider than the specified width, it will
        be reduced to that size with the aspect ratio preserved.

        The provided text and author will be added to the image.

        The result will be saved to a randomized name in the output_dir
        of the MemeEngine object.

        :param img_path: The path to the input image.
        :param text: The body to text to add to the image.
        :param author: The author to be added to the image.
        :param width: The maximum width of the result.
        :return: The path where the result was saved.
        """
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
        out_path = self.random_file_path(self.output_dir, 'png')
        img.save(out_path)
        return out_path

    @staticmethod
    def random_file_path(
        directory: str, extension: str,
        length = 8, characters = string.digits + string.ascii_letters,
    ) -> str:
        """Generate a random file name, ensuring that it does not exist.

        A string of the length provided will be generated at random by
        drawing (with replacement) from the characters provided, and the
        extension provided will be appended to it. If extension is the
        empty string, no extension will be appended.

        If a file with this name exists in the provided directory, the
        process will instead be repeated until a file name is generated
        that does not exist.

        :param directory:
            The directory for the randomly generated file name.
        :param extension: The file extension to append (after a dot).
        :param length: The length of the string to generate.
        :param characters: The string of characters from which to draw.
        :return: The path of the randomly generated file name.
        """
        while True:
            file_name = ''.join(random.choices(characters, k=length))
            if extension:
                file_name += '.' + extension
            file_path = os.path.join(directory, file_name)
            if not os.path.exists(file_path):
                break
        return file_path
