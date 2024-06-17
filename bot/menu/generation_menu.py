from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

SDXL_BUTTON = InlineKeyboardButton(text='SDXL 🤩', callback_data='SDXL')
MANGA_BUTTON = InlineKeyboardButton(text='MANGA ⛩️', callback_data='MANGA')


GENERATION_MENU = InlineKeyboardMarkup(inline_keyboard=[[SDXL_BUTTON, MANGA_BUTTON]])
