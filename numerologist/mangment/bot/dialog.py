from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog.widgets.text import Const, Format

import texts
from handlers import messages_handler, ai_response_getter
from states import NumerologistSG

numerologist = Dialog(
    Window(Format('{ai_response}'),
           MessageInput(messages_handler),
           state=NumerologistSG.name,
           getter=ai_response_getter),
    Window(Const(texts.fortune),
           state=NumerologistSG.fortune_roll)
)
