from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Next
from aiogram_dialog.widgets.text import Const, Format

import texts
from handlers import get_name, get_date_of_birth
from states import NumerologistSG

numerologist = Dialog(
    Window(Const(texts.greeting),
           Next(Const("Начать знакомство")),
           state=NumerologistSG.greeting),
    Window(Format("{ai_response_name}"),
           MessageInput(get_name),
           state=NumerologistSG.name),
    Window(Format("{ai_response_birth}"),
           MessageInput(get_date_of_birth),
           state=NumerologistSG.date_of_birth),
    Window(Format("{ai_response_preferences}"),
           MessageInput(texts.preferences),
           state=NumerologistSG.preferences),
    Window(Const(texts.fortune),
           MessageInput(),
           state=NumerologistSG.fortune_roll)
)
