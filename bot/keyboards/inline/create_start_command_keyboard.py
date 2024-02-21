from aiogram import types


def create_start_keyboard():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Поиск🔎",
                callback_data="search_manga"
            ),
            types.InlineKeyboardButton(
                text="Новые главы📬",
                callback_data="new_chapters"
            )
        ]
    ]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)

    return keyboard
