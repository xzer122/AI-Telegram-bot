from aiogram.fsm.state import StatesGroup


class AcquaintanceSG(StatesGroup):
    greeting = State()
    name = State()
    date_of_birth = State()
    preferences = State()
