from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.main_db import get_db

router = Router()

@router.message(Command("drinks"))
async def drinks_command(message: Message):
    drinks = await get_db()

    if not drinks:
        await message.answer("В базе данных пока нет записей.")
        return

    text = "Список напитков:\n\n"

    for drink in drinks:
        id_drink, name_drink, price = drink
        text += f"{id_drink}. {name_drink} — {price}\n"

    await message.answer(text)
