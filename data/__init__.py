from shared.config import config
from data.Quote import QuotesHandler
from data.Translate import TranslationHandler

quote_provider = QuotesHandler(
    config.api_ninjas.api_ninjas_token,
    config.api_ninjas.api_ninjas_categories
)

translator = TranslationHandler()