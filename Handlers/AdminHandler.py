from config import ADMIN_CHAT_ID
from loader import bot


async def admin_message():
    await bot.send_message(ADMIN_CHAT_ID, "Бот запущен")
