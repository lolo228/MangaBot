from telethon import TelegramClient
from telethon import types, functions
import asyncio

api_id = 23036385
api_hash = '55ed62679d06c14d02ccdf997e9f4b79'

client = TelegramClient("session", api_id, api_hash,
                        device_model="iPhone 13 Pro Max",
                        system_version="14.8.1",
                        app_version = "8.4",
                        lang_code = "en",
                        system_lang_code = "en-US")


async def check_new_manga(client):
    await client.start()

    async for dialog in client.iter_dialogs(limit=500):
        if dialog.is_channel:
            if dialog.title == "Слив платных глав | LR Manga":
                async for message in client.iter_messages(dialog.id, limit=100):
                    print(message.reply_markup.rows[0].buttons[0].url)


if __name__ == "__main__":
    asyncio.run(check_new_manga(client))