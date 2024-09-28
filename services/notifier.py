# services/notifier.py
from pyrogram import Client
from pyrogram.types import Message
from datetime import datetime
from config import config

async def send_notification(client: Client, message: Message, keyword: str):
    user = message.from_user
    user_info = (
        f"ID: {user.id}\n"
        f"Имя: {user.first_name or ''}\n"
        + (f"Username: @{user.username}\n" if user.username else "")
    )
    text = (
        f"Обнаружено ключевое слово: '{keyword}'\n"
        f"Время: {datetime.now().isoformat()}\n\n"
        f"Информация о пользователе:\n{user_info}\n"
        f"Сообщение: {message.text or '<без текста>'}"
    )
    await client.send_message(chat_id=config.notify_chat, text=text)

    if message.photo:
        await client.forward_messages(
            chat_id=config.notify_chat,
            from_chat_id=message.chat.id,
            message_ids=message.message_id
        )