from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, StartMode

from app.states import AcquaintanceSG


async def cmd_start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(AcquaintanceSG.greeting, mode=StartMode.RESET_STACK)


async def get_name(message: Message, dialog: Dialog, dialog_manager: DialogManager):
    pass


async def get_date_of_birth(message: Message, dialog: Dialog, dialog_manager: DialogManager):
    pass
