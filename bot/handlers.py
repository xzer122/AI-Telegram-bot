from aiogram_dialog import DialogManager, StartMode
from aiogram.types import Message
from aiogram_dialog.widgets.input import MessageInput

from ai import generate_message
from models import UserTemp
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
    users[message.from_user.id].context = context
    await dialog_manager.start(NumerologistSG.name, mode=StartMode.RESET_STACK)


async def messages_handler(message: Message, inp: MessageInput, dialog_manager: DialogManager):
    user_id = message.from_user.id
    users[user_id].context.append({'role': 'user', 'content': message.text})
    completion = generate_message(users[user_id].context)
    users[user_id].context.append(completion.choices[0].message)


# async def get_date_of_birth(message: Message, inp: MessageInput, dialog_manager: DialogManager):
#     if message.text.lower() == 'вперёд' or message.text.lower() == 'вперед':
#         await dialog_manager.next()
#
#     user_id = message.from_user.id
#     users[user_id].context.append({'role': 'user', 'content': message.text})
#
#     if users[user_id].name == '':
#         age_context = users[user_id].context
#         age_context.append({'role': 'system', 'content': 'Пользователь указал полную дату рождения? Отвечай "Да." '
#                                                          'или "Нет."'})
#         completion = generate_message(age_context)
#         if completion.choices[0].message.content == 'Да.':
#             users[user_id].name = completion.choices[0].message.content
#
#     completion = generate_message(users[user_id].context)
#     users[user_id].context.append(completion.choices[0].message)


# getters

async def ai_response_getter(**kwargs):
    manager = kwargs['dialog_manager']
    user_id = manager.event.from_user.id
    completion = generate_message(users[user_id].context)
    users[user_id].context.append(completion.choices[0].message)
    return {'ai_response': completion.choices[0].message.content}
