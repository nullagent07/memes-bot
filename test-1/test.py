import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import pytesseract
from translate import Translator
import os

def translate_text(text, src='en', dest='ru'):
    translator = Translator(from_lang=src, to_lang=dest)
    return translator.translate(text)

def get_text_contours(image_path):
    # Загрузка изображения с помощью OpenCV
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Нахождение контуров текста
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours, image

def add_text_to_image(image_path, text, output_path, contours):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # Путь к шрифту Arial
    font_path = "/Library/Fonts/Arial.ttf"
    font = ImageFont.truetype(font_path, size=20)

    # Закрашиваем области с оригинальным текстом белым цветом
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        draw.rectangle([x, y, x+w, y+h], fill=(255, 255, 255))

    # Разделяем переведенный текст на строки и добавляем их последовательно
    lines = text.split('\n')
    y_text = 10
    for line in lines:
        draw.text((10, y_text), line, font=font, fill=(0, 0, 0))
        y_text += 30  # Смещение по вертикали для новой строки

    image.save(output_path, format="PNG")

def process_meme(image_path, output_path):
    full_image_path = os.path.join(image_path)
    image = Image.open(full_image_path)
    text = pytesseract.image_to_string(image, lang='eng')
    translated_text = translate_text(text)

    # Получаем контуры текста
    contours, _ = get_text_contours(full_image_path)
    
    add_text_to_image(full_image_path, translated_text, output_path, contours)
    print(f"Processed meme saved to {output_path}")

# Usage
process_meme('./images/image.png', 'output_meme.png')
