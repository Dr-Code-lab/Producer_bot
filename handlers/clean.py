from aiogram.filters import Command
from aiogram.types import Message
from loader import dp, fee


@dp.message(Command('clean'))
async def to_command_clean(message: Message):
    fee.type = None
    fee.size = None
    await message.answer(f"Бот обнулился.")
