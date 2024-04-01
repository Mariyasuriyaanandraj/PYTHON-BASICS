# %%
pip install googletrans==4.0.0-rc1

# %%
from googletrans import Translator

def translate_text(text, target_language='ta'):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

# Example usage:
text_to_translate = ""  # English text to translate
target_language = 'en'  # Translate to Tamil

translated_text = translate_text(text_to_translate, target_language)
print("Translated text:", translated_text)

# %%



