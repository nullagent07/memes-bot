from translate import Translator

translator = Translator(to_lang="ru")

def translate_text(text, target_lang='ru'): 
    translator = Translator(to_lang=target_lang)   
    translated = translator.translate(text)
    return translated