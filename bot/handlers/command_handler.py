from aiogram import types, Dispatcher

async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.first_name}, добро пожаловать! Используйте кнопки для продолжения работы', reply_markup=MAIN_MENU)


def register_general_commands_handlers(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'], state='*')
