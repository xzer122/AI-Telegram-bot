from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import MessageInput

from backend.api.models import UserTemp
from bot.ai import generate_message
from states import NumerologistSG

users = {}


async def cmd_start(message: Message, dialog_manager: DialogManager):
    from bot import texts
    context = [
        {"role": "system", "content": texts.prompt},
        {"role": "user", "content": "/start"}
    ]
    user = UserTemp()
    users[message.from_user.id] = user
    completion = generate_message(context)
    context.append(completion.choices[0].message)
    await message.reply(completion.choices[0].message.content)
    users[message.from_user.id].context = context
    await dialog_manager.start(NumerologistSG.greeting, mode=StartMode.RESET_STACK)


async def get_name(message: Message, inp: MessageInput, dialog_manager: DialogManager):
    pass


async def get_date_of_birth(message: Message, inp: MessageInput, dialog_manager: DialogManager):
    pass


async def preferences(message: Message, inp: MessageInput, dialog_manager: DialogManager):
    pass