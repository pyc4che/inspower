from shared.config import config
from bot.handlers.utils import user_allowed
from data import quote_provider, translator

from aiogram import Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import (CallbackQuery, InlineKeyboardButton, 
    InlineKeyboardMarkup, Message)

router = Router()


@router.message(Text("🖋️ Get Quote 🖋️"))
@user_allowed
async def generate_quote(message: Message, state: FSMContext, 
                        *args, **kwargs):
    quote = quote_provider.generate()

    await state.update_data(
        current_quote=quote, 
        language="en"
    )
    await send_quote(
        message, 
        "en", quote
    )


@router.callback_query(Text(startswith="switch_language"))
async def toggle_language(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    new_language = "other" if data.get("language") == "en" else "en"
    
    await state.update_data(
        language=new_language
    )
    
    await send_quote(
        callback, new_language,
        data["current_quote"]
        )


async def send_quote(entity, language, quote):
    text = (f"English 🇺🇸:\n\n{quote}" if language == "en" else
            f"{config.google_translate.message}:\n\n{translator.translate(quote)}")
    
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text="English 🇺🇸" if language != "en" else f"{config.google_translate.message}",
                callback_data="switch_language"
            )]
        ]
    )

    if isinstance(entity, CallbackQuery):
        await entity.message.edit_text(
            text=text, 
            reply_markup=markup
        )
        await entity.answer()
    else:
        await entity.answer(
            text=text,
            reply_markup=markup
        )
