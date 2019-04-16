from PIL import Image, ImageDraw, ImageFont
from pytesseract import image_to_string

from utils import misc, colors, path

import config as conf
from utils.misc import parse_text


class Word:
    text: str = ""
    author: str = ""
    font_size: int = conf.DEFAULT_FONT_SIZE
    font_file: str = conf.DEFAULT_FONT
    language: str = conf.DEFAULT_LANGUAGE
    x = conf.DEFAULT_TEXT_START[0]
    y = conf.DEFAULT_TEXT_START[1]
    text_color = colors.WHITE

    def __init__(self, text):
        self.text, self.author = misc.parse_text(text)

    def print_to_img(self, img_path: str = conf.DEFAULT_BG):
        img = Image.open(path.get_file_path(img_path, data_attr='test', data_type='bg'))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(self.font_file, self.font_size)
        self.justify_text()
        draw.text((self.x, self.y), self.text, self.text_color, font=font)
        return img

    @staticmethod
    def read_from_img(image_path: str):
        img = Image.open(image_path)
        text = image_to_string(img, lang=conf.DEFAULT_LANGUAGE)
        text = misc.prettify(text)
        return Word(text)

    def justify_text(self):
        gap = (self.text.split(".")[0].__len__() * self.font_size / 5) / 2
        self.x = self.x - gap
        print(self.x)

    def __str__(self):
        return "Text: {}\nAuthor: {}\nFont Size: {}\nFont File: {}\nLanguage: {}\nText Position: ({}, {})" \
            .format(self.text, self.author, self.font_size, self.font_file, self.language, self.x, self.y)




