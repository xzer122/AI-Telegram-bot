import asyncio
import logging
import os

from aiogram import Dispatcher, Bot
from aiogram.filters import CommandStart
from aiogram_dialog import setup_dialogs

from dialog import numerologist
from handlers import cmd_start

BOT_TOKEN = os.getenv('AI_NUMEROLOGIST')
dp = Dispatcher()
bot = Bot(token=BOT_TOKEN)


async def main():
    logging.basicConfig(level=logging.INFO)
    dp.message.register(cmd_start, CommandStart())
    dp.include_router(numerologist)
    setup_dialogs(dp)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
