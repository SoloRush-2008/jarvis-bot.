import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# Настройки бота
TOKEN = "8849903659:AAGRcdcolV50kCbTke9i9O2sOySs_EG8U6M"
ADMIN_ID = 6357555378

# Включаем логирование
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Проверка на администратора
def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if not is_admin(message.from_user.id):
        await message.answer("❌ У вас нет доступа к этому боту.")
        return
    await message.answer("🚀 Привет! Бот для @Solo_Rush_Anime успешно запущен и работает 24/7!")

@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    if not is_admin(message.from_user.id):
        await message.answer("❌ У вас нет доступа к этому боту.")
        return
    await message.answer("📌 Доступные команды:\n/start - Запуск бота\n/help - Помощь")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
  
