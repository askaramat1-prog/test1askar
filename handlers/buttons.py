from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/menu')
        ],
    ],
    resize_keyboard=True
)

# ------------------------------------------------------------------------------------------

main_buttons_builder = ReplyKeyboardBuilder()
main_buttons_builder.button(text='/start')
main_buttons_builder.button(text='/menu')
main_buttons_builder.button(text='/about')
main_buttons_builder.adjust(3)

main_builder = main_buttons_builder.as_markup(resize_keyboard=True)

# ------------------------------------------------------------------------------------------

menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Меню', callback_data='menu')],
        [InlineKeyboardButton(text='О нас', callback_data='about')]
    ]
)
