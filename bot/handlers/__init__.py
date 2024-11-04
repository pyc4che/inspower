from aiogram import Router

from bot.handlers.start import router as start_router
from bot.handlers.quote import router as quote_router

router = Router()

router.include_routers(
    start_router,
    quote_router
)
