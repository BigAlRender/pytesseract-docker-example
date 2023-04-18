from flask import Flask
from PIL import Image
import pytesseract

app = Flask(__name__)

@app.route('/')
def ocr():
    # test.png from the pytesseract project: https://github.com/madmaze/pytesseract/tree/master/tests/data
    return pytesseract.image_to_string(Image.open('test.png'))