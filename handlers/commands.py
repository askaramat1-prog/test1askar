from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from db.main_db import get_db, add_product_db, add_drink_info_db

router = Router()


@router.message(Command("add"))
async def add_drink(message: Message):
    drink_id = add_product_db("Cola", 100)
    add_drink_info_db(drink_id, 500)

    await message.answer("Напиток добавлен!")


@router.message(Command("list"))
async def list_drinks(message: Message):
    drinks = get_db()

    if not drinks:
        await message.answer("Список напитков пуст.")
        return

    text = "Список напитков:\n\n"

    for drink in drinks:
        name, price, volume = drink

        text += (
            f"Название: {name}\n"
            f"Цена: {price}\n"
            f"Объём: {volume} мл\n\n"
        )

    await message.answer(text)