from translate import Translator

# Настройка клиента переводчика
translator = Translator(to_lang="ru")

def translate_text(text, target_lang="ru"):
    """
    Translates the given text to the target language.
    
    :param text: The text to be translated.
    :param target_lang: The language to translate the text into (default is Russian).
    :return: The translated text.
    """
    translator = Translator(to_lang=target_lang)
    translated = translator.translate(text)
    return translated