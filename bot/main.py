from aiogram import Dispatcher, Bot

from .handlers import user_handler_register
from .misc import BOT_TOKEN
from .database import create_database


async def register_all_handlers(dp: Dispatcher):
    user_handler_register(dp)


async def start_bot():
    # Создание базы данных
    create_database()

    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    # Регистрация хэндлеров
    await register_all_handlers(dp)

    # Запуск бота
    await dp.start_polling(bot)
