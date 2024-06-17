from aiogram import types
from aiogram.filters import Command
from aiogram.dispatcher.router import Router
from aiogram.fsm.context import FSMContext

from bot.menu.generation_menu import GENERATION_MENU

from bot.states.states import GeneratePicState


async def command_start(message: types.Message, state: FSMContext):
    await message.answer(
        f'Привет {message.from_user.first_name}, добро пожаловать! Используйте кнопки для продолжения работы',
        reply_markup=GENERATION_MENU
    )
    await state.set_state(GeneratePicState.idle)

def register_general_commands_handlers(router: Router):
    router.message.register(command_start, Command(commands=['start']))
