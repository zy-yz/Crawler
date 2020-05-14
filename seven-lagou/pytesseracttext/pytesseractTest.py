# encoding: utf-8

import pytesseract
from PIL import Image

from PIL import Image
import pytesseract

if __name__ == '__main__':
    text = pytesseract.image_to_string(Image.open('9.png'))
    print(text)

