import asyncio
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = "8268408644:AAHmkyBmdBb8XXXMXoXO_-OqOkXhR_P4mH4"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer("✅ Бот работает на хостинге!")

async def main():
    print("🚀 Бот запущен на Render.com")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())