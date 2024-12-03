from aiogram.types import Message
from aiogram_dialog import DialogManager, StartMode
from aiogram_dialog.widgets.input import MessageInput

from bot.ai import generate_message
from bot.models import UserTemp
from bot.states import NumerologistSG

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
    await message.answer(completion.choices[0].message.content)
    users[message.from_user.id].context = context
    await dialog_manager.start(NumerologistSG.name, mode=StartMode.RESET_STACK)


async def get_name(message: Message, inp: MessageInput, dialog_manager: DialogManager):
    users[message.from_user.id].name = message.text
    users[message.from_user.id].context.append({'role': 'user', 'content': message.text})
    completion = generate_message(users[message.from_user.id].context)
    await message.answer(completion.choices[0].message.content)
    users[message.from_user.id].context.append(completion.choices[0].message)
    await dialog_manager.next()


async def get_date_of_birth(message: Message, inp: MessageInput, dialog_manager: DialogManager):
    pass


async def get_preferences(message: Message, inp: MessageInput, dialog_manager: DialogManager):
    pass


# getters

async def ai_response_getter(**kwargs):
    manager = kwargs['dialog_manager']
    user_id = manager.event.from_user.id
    completion = generate_message(users[user_id].context)
    users[user_id].context.append(completion.choices[0].message)
    return {'ai_response': completion.choices[0].message.content}
