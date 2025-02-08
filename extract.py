from PIL import Image
import pytesseract
import os
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def image_to_string(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    image = Image.open(image_path)
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text
