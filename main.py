from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties
import asyncio
from config import TOKEN

from aiogram.enums import ParseMode

from app.handlers import router
from app.database.models import async_main


# Основная функция для запуска бота
async def main():
    await async_main()
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
    dp = Dispatcher()
    dp.include_router(router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()



# Запуск
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('ВЫРУБИЛ ТЫ')


