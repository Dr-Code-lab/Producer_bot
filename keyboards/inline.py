from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


keyboard = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Сумма + налог",
                         callback_data='plus'),
    InlineKeyboardButton(text="Сумма - налог",
                         callback_data='minus'),
]])

keyboard_fee = InlineKeyboardBuilder()
keyboard_fee.button(text=f'Самозанятость 6%', callback_data='6')
for i in [7, 8, 9, 10]:
    keyboard_fee.button(text=f'ИП {i}%', callback_data=f'{i}')
    keyboard_fee.adjust(1,2)
