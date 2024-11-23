from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.kbd import Next
from aiogram_dialog.widgets.text import Const

from app import texts
from states import AcquaintanceSG

acquaintance = Dialog(
    Window(Const(texts.greeting),
           Next(Const("Начать знакомство")),
           state=AcquaintanceSG.greeting),
    Window(Const(texts.name),
           MessageInput(get_name),
           state=AcquaintanceSG.name),
    Window(Const(texts.age),
           MessageInput(get_date_of_birth),
           state=AcquaintanceSG.date_of_birth)
)

numerologist = Dialog(
)
