from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import MessageInput

from app.states import NumerologistSG


async def cmd_start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(NumerologistSG.greeting, mode=StartMode.RESET_STACK)


async def get_name(message: Message, inp: MessageInput, dialog_manager: DialogManager):
    pass


async def get_date_of_birth(message: Message, inp: MessageInput, dialog_manager: DialogManager):
    pass


async def preferences(message: Message, inp: MessageInput, dialog_manager: DialogManager):
    pass