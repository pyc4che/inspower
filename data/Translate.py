from shared.config import config

from googletrans import Translator


class TranslationHandler:
    def __init__(self) -> None:
        self.translator = Translator()

    def translate(self, text):
        
        try: 
            return self.translator.translate(
                text,
                dest=config.google_translate.language
            ).text
        
        except Exception as _:
            return "🚫 No translation found in the response."
