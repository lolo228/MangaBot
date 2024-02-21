from aiogram import Dispatcher
from aiogram.filters.command import CommandStart

from .commands_handlers import start_command_handler


def user_handler_register(dp: Dispatcher):
    dp.message.register(start_command_handler, CommandStart())
