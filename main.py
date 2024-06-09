import easyocr
import cv2

def detect_and_replace_text(image_path, new_text, output_path):
    # Загрузка изображения
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Проверка, что изображение загружено корректно
    if image is None:
        raise FileNotFoundError(f"Не удается открыть/прочитать файл: {image_path}. Проверьте путь к файлу или его целостность.")

    # Инициализация easyocr Reader
    reader = easyocr.Reader(['en'])
    
    # Обнаружение текста
    results = reader.readtext(image_path)  # передаем путь к изображению напрямую
    
    for (bbox, text, prob) in results:
        # Получение координат
        (top_left, top_right, bottom_right, bottom_left) = bbox
        top_left = tuple(map(int, top_left))
        bottom_right = tuple(map(int, bottom_right))
        
        # Замена текстового блока белым прямоугольником
        cv2.rectangle(image, top_left, bottom_right, (255, 255, 255), -1)
        
        # Добавление нового текста поверх прямоугольника
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.7
        font_thickness = 2
        text_size, _ = cv2.getTextSize(new_text, font, font_scale, font_thickness)
        text_x = top_left[0] + (bottom_right[0] - top_left[0] - text_size[0]) // 2
        text_y = top_left[1] + (bottom_right[1] - top_left[1] + text_size[1]) // 2

        cv2.putText(image, new_text, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)
    
    # Сохранение результата
    cv2.imwrite(output_path, image)

# Пример использования
image_path = '../images/image.png'
new_text = 'New Text'
output_path = '../images/output_image.png'

detect_and_replace_text('./images/image.png', new_text, './images/output_image.png')
