import asyncio

from config import bot, dp
from handlers.commands import router_commands

async def main():
    dp.include_router(router_commands)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())