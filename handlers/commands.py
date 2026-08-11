from aiogram.filters import Command
from aiogram import Router, F
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import bot
from handlers.buttons import main_buttons, main_builder, menu_inline

#from db import main_db

router_commands = Router()


@router_commands.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        "Добро пожаловать в кафе!",
        reply_markup=menu_inline
    )

@router_commands.message(Command("menu"))
async def menu_command(message: Message):
    await message.answer(
        "/start - запуск бота\n"
        "/menu - список команд"
    )


@router_commands.message(F.text == "пока")
async def bye_command(message: Message):
    await message.answer("До встречи!")

@router_commands.callback_query(F.data == 'menu')
async def about_callback(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        '/start - запуск бота\n'
        '/menu - список команд'
    )
@router_commands.callback_query(F.data == 'about')
async def about_callback(call: CallbackQuery):
    await call.answer()
    await call.message.answer(
        'Наше кафе предлагает вкусные напитки и уютную атмосферу!'
    )

@router_commands.message(F.text)
async def echo(message: Message):
    await message.answer(f'Такой команды нет - {message.text}')
    