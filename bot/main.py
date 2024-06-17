import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage

from bot.loader import dp, bot
from bot.handlers.reg_handlers import reg_handlers

logging.basicConfig(level=logging.INFO)

async def set_default_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/help", description="Get help"),
    ]
    await bot.set_my_commands(commands)

async def on_startup(bot: Bot, dp: Dispatcher):
    reg_handlers(dp)
    await set_default_commands(bot)

async def main():
    
    await on_startup(bot, dp)
    await dp.start_polling(bot, skip_updates=True)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
