import locale
locale.setlocale(locale.LC_ALL, 'C')
import tesserocr
from PIL import Image

class ocr:
    def __init__(self, filename):
        self.filename = filename



    def getPrediction(self):
        image = Image.open(self.filename)
        lines = tesserocr.image_to_text(image)  # print ocr text from image
        #for line in lines.split("\r"):
         #   print(line)
        return lines


