from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Next
from aiogram_dialog.widgets.text import Const, Format

from app import texts
from states import AcquaintanceSG
from handlers import get_name, get_date_of_birth

acquaintance = Dialog(
    Window(Const(texts.greeting),
           Next(Const("Начать знакомство")),
           state=AcquaintanceSG.greeting),
    Window(Format("{ai_response_name}"),
           MessageInput(get_name),
           state=AcquaintanceSG.name),
    Window(Format("{ai_response_name}"),
           MessageInput(get_date_of_birth),
           state=AcquaintanceSG.date_of_birth)
)

numerologist = Dialog(
)
