import asyncio

from config import bot, dp
from handlers.commands import router
from db.main_db import create_table


async def on_startup():
    create_table()


async def main():
    await on_startup()

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())