# handlers/monitor.py
from pyrogram import filters, Client
from pyrogram.types import Message

from config import config
from services.keywords import match_keywords


def register_handlers(app: Client):
    @app.on_message(filters.text | filters.photo)
    async def monitor(client: Client, message: Message):
        chat_id = message.chat.id or message.chat.username
        if chat_id in config.monitor_chats:
            text = (message.text or "").lower()
            for kw in config.keywords:
                if kw.lower() in text:
                    await handle_detect(client, message, kw)

async def handle_detect(client: Client, message: Message, keyword: str):
    print(client, message, keyword)