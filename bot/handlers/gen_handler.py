from aiogram import types
from aiogram.types import CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from bot.loader import bot, dp
from bot.utils.generator import generate_pic

from bot.states.states import GeneratePicState

from bot.menu.generation_menu import GENERATION_MENU

@dp.callback_query(GeneratePicState.idle)
async def sdxl_button_handler(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Введите промпт для генерации:")

    await state.update_data(model=callback_query.data)

    await state.set_state(GeneratePicState.waiting_for_prompt)


@dp.message(GeneratePicState.waiting_for_prompt)
async def prompt_handler(message: types.Message, state: FSMContext):
    prompt = message.text

    data = await state.get_data()

    ret = await message.answer(text="Ожидаем генерацию...")

    try:
        result = generate_pic(prompt, data['model'])
    except Exception as e:
        await bot.delete_message(chat_id=message.chat.id, message_id=ret.message_id)
        await bot.send_message(message.from_user.id, text="Для продолжения генерации выберете модель", reply_markup=GENERATION_MENU)
        await state.set_state(GeneratePicState.idle)

    print(result)

    if isinstance(result, list):
        result = result[0]

    await bot.delete_message(chat_id=message.chat.id, message_id=ret.message_id)
    await bot.send_photo(message.chat.id, photo=result)
    await bot.send_message(message.from_user.id, text="Для продолжения генерации выберете модель", reply_markup=GENERATION_MENU)
    await state.set_state(GeneratePicState.idle)
