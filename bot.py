import asyncio
import logging
import os
from aiohttp import web
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Токен бота и данные канала
BOT_TOKEN = "ТВОЙ_ТОКЕН_БОТА"  # Обязательно вставь свой токен!
CHANNEL_ID = "@Solo_Rush_Anime"
CHANNEL_URL = "https://t.me/Solo_Rush_Anime"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Кнопка под постом
channel_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔥 Смотреть аниме-канал", url=CHANNEL_URL)]
    ]
)

@dp.message(F.text == "/start")
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 **Привет, босс!**\n\n"
        "Я твой аниме-помощник Джарвис.\n"
        "Отправь мне видео, фото или трейлер с подписью — и я опубликую это в канал!"
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    
    # 1. Сначала поднимаем веб-сервер, чтобы Render сразу увидел открытый порт
    app = web.Application()
    app.router.add_get("/", lambda r: web.Response(text="Bot is alive!"))
    runner = web.AppRunner(app)
    await runner.setup()
    
    port = int(os.environ.get("PORT", 10000))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    logging.info(f"Web server started on port {port}")

    # 2. Запускаем бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
