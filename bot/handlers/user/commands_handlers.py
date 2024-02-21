from aiogram import types, Bot

from bot.keyboards import create_start_keyboard


async def start_command_handler(message: types.Message):
    bot: Bot = message.bot

    keyboard = create_start_keyboard()

    await bot.send_message(
        message.chat.id,
        f"{message.from_user.full_name}, приветствую тебя в боте для чтения манги.\n\n"
        f"Это не официальный бот LR Manga!!!",
        reply_markup=keyboard
    )
