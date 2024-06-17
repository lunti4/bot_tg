from aiogram import Dispatcher
from aiogram.dispatcher.router import Router

from bot.handlers.start import register_general_commands_handlers
from bot.handlers.gen_handler import sdxl_button_handler

def reg_handlers(dp: Dispatcher):
    router = Router()
    register_general_commands_handlers(router)
    dp.include_router(router)
