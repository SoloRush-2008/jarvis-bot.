import asyncio
import logging
from aiogram import Bot, Dispatcher, F, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Токен вашего бота и ID/юзернейм канала
BOT_TOKEN = "ТВОЙ_ТОКЕН_БОТА"  # Вставь сюда токен от BotFather
CHANNEL_ID = "@Solo_Rush_Anime" # Юзернейм твоего канала
CHANNEL_URL = "https://t.me/Solo_Rush_Anime" # Ссылка для кнопки

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
        "Отправь мне видео, фото или трейлер с подписью — и я опубликую это в канал!",
        parse_mode="Markdown"
    )

# Обработка видео
@dp.message(F.video)
async def handle_video(message: types.Message):
    caption = message.caption or ""
    full_caption = f"{caption}\n\n✨ Подпишись на {CHANNEL_ID} — мир аниме!"
    
    try:
        await bot.send_video(
            chat_id=CHANNEL_ID,
            video=message.video.file_id,
            caption=full_caption,
            reply_markup=channel_keyboard
        )
        await message.answer(f"✅ Успешно опубликовано в {CHANNEL_ID}!")
    except Exception as e:
        await message.answer(f"❌ Ошибка при публикации: {e}")

# Обработка фото
@dp.message(F.photo)
async def handle_photo(message: types.Message):
    caption = message.caption or ""
    full_caption = f"{caption}\n\n✨ Подпишись на {CHANNEL_ID} — мир аниме!"
    
    try:
        await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=message.photo[-1].file_id,
            caption=full_caption,
            reply_markup=channel_keyboard
        )
        await message.answer(f"✅ Успешно опубликовано в {CHANNEL_ID}!")
    except Exception as e:
        await message.answer(f"❌ Ошибка при публикации: {e}")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
