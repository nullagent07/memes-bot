import cv2
import numpy as np
from PIL import Image
import pytesseract
from text_translator import translate_text

def main():
    # Uploading an image
    image_path = './images/image.png'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Application of median filter for noise removal
    image = cv2.medianBlur(image, 3)

    # Image binarisation
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Saving a pre-processed image for inspection
    preprocessed_image_path = 'preprocessed_image.png'
    cv2.imwrite(preprocessed_image_path, binary_image)

    # Performing OCR for text extraction
    image_pil = Image.fromarray(binary_image)
    text = pytesseract.image_to_string(image_pil, lang='eng')

    print("Recognised text:")
    print(text)

    ranslated_text = translate_text(text, "ru")
    print("Ranslated text:")
    print(ranslated_text)


if __name__ == "__main__":
    main()