from aiogram.fsm.state import StatesGroup


class NumerologistSG(StatesGroup):
    greeting = State()
    name = State()
    date_of_birth = State()
    preferences = State()
    fortune_roll = State()