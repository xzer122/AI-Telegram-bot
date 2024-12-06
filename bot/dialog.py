from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Const, Format

import texts
from handlers import get_name, get_date_of_birth, get_preferences, ai_response_getter
from states import NumerologistSG

numerologist = Dialog(
    Window(Format('{ai_response}'),
           MessageInput(get_name),
           state=NumerologistSG.name,
           getter=ai_response_getter),
    Window(Format('{ai_response}'),
           MessageInput(get_date_of_birth),
           state=NumerologistSG.date_of_birth,
           getter=ai_response_getter),
    Window(MessageInput(get_preferences),
           state=NumerologistSG.preferences,
           getter=ai_response_getter),
    Window(Const(texts.fortune),
           state=NumerologistSG.fortune_roll)
)
