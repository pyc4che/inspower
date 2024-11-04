from shared.config import config
from aiogram.types import Message, CallbackQuery


def user_allowed(func):
    async def wrapper(entity, *args, **kwargs):
        user_id = getattr(entity.from_user, 'id', None) if isinstance(entity, (Message, CallbackQuery)) else None

        if user_id not in config.telegram.allowed_users:
            if isinstance(entity, Message):
                await entity.reply("🚫 Access denied.")
            
            elif isinstance(entity, CallbackQuery):
                await entity.answer("🚫 Access denied.", show_alert=True)
            
            return

        return await func(entity, *args, **kwargs)

    return wrapper
