from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router_fsm = Router()

class Movie(StatesGroup):
    name = State()
    genre = State()
    rating = State()

@router_fsm.message(Command("form"))
async def start_form(message: Message, state: FSMContext):
    await state.set_state(Movie.title)
    await message.answer("Напиши название фильма:")

@router_fsm.message(Movie.title)
async def process_title(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(Movie.genre)
    await message.answer("Теперь напиши жанр:")

@router_fsm.message(Movie.genre)
async def process_genre(message: Message, state: FSMContext):
    await state.update_data(genre=message.text)
    await state.set_state(Movie.rating)
    await message.answer("Поставь оценку фильму (например от 1 до 10):")

@router_fsm.message(Movie.rating)
async def process_rating(message: Message, state: FSMContext):
    await state.update_data(rating=message.text)
    
    data = await state.get_data()
    
    text = (
        "Готово! Вот что ты указал:\n\n"
        f"Название: {data.get('title')}\n"
        f"Жанр: {data.get('genre')}\n"
        f"Оценка: {data.get('rating')}"
    )
    
    await message.answer(text)
    await state.clear()


