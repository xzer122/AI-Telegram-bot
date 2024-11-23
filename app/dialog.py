from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Next
from aiogram_dialog.widgets.text import Const, Format

from app import texts
from app.texts import preferences
from states import NumerologistSG
from handlers import get_name, get_date_of_birth

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
           MessageInput(preferences),
           state=NumerologistSG.preferences),
    Window(Const(texts.fortune))
)
