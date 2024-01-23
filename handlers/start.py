from aiogram.filters import CommandStart
from aiogram.types import Message
from keyboards.inline import keyboard
from loader import dp


@dp.message(CommandStart())
async def to_command_start(message: Message):
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Выберите тип расчета:", reply_markup=keyboard)
