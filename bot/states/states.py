from aiogram.fsm.state import State, StatesGroup

class GeneratePicState(StatesGroup):
    waiting_for_prompt = State()
    idle = State()