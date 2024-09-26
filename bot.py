# bot.py
from pyrogram import Client
from config import config
from handlers.monitor import register_handlers


def main():
    app = Client(
        config.session_name,
        api_id=config.api_id,
        api_hash=config.api_hash,
    )

    register_handlers(app)
    app.run()


if __name__ == "__main__":
    main()