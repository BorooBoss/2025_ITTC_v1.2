from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def image_to_string():
    image = Image.open('images/test.png')
    extracted_text = pytesseract.image_to_string(image)

    return extracted_text