from bot.bot import bot
from bot.handlers.utils import user_allowed

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton


def get_menu_reply_markup() -> ReplyKeyboardMarkup:
    buttons = [
        "🖋️ Get Quote 🖋️"
    ]

    builder = ReplyKeyboardBuilder()

    for button in buttons:
        builder.add(KeyboardButton(text=button))

    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)


router = Router()

@router.message(CommandStart())
@user_allowed
async def start_handler(message: Message, *args, **kwargs):
    me = await bot.me()

    menu_markup = get_menu_reply_markup()

    greeting_name = f'@{me.username}' if me.username is not None else me.first_name
    user_name = f'@{message.from_user.username}' if message.from_user.username is not None else message.from_user.first_name
    
    await message.answer(
        f'Hello and welcome, {user_name}! I am {greeting_name}.\nStart your journey of inspiration and power 🐺!',
        reply_markup=menu_markup
    )
