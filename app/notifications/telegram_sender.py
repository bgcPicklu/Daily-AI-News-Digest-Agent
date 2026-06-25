from telegram import Bot

from app.config import TELEGRAM_TOKEN
from app.config import TELEGRAM_CHAT_ID


async def send_telegram(msg):

    try:

        bot = Bot(
            token=TELEGRAM_TOKEN
        )

        await bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=msg[:4000]
        )

        print("Telegram Delivered")

    except Exception as e:

        print("Telegram Error:", str(e))