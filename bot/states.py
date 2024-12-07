from aiogram.fsm.state import StatesGroup, State


class NumerologistSG(StatesGroup):
    name = State()
    fortune_roll = State()