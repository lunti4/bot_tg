import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


bot = Bot(token=os.getenv("API_TOKEN"))
dp = Dispatcher(storage=MemoryStorage())
