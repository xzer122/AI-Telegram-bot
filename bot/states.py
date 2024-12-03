from aiogram.fsm.state import StatesGroup, State


class NumerologistSG(StatesGroup):
    name = State()
    date_of_birth = State()
    preferences = State()
    fortune_roll = State()