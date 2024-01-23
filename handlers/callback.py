from aiogram import F
from aiogram.types import CallbackQuery
from loader import dp, fee
from keyboards.inline import keyboard_fee


@dp.callback_query(F.data == "plus")
async def select_fee_plus(call: CallbackQuery):
    fee.type = "plus"
    await call.message.answer(f"Какой налог вы хотите рассчитать?", reply_markup=keyboard_fee.as_markup())


@dp.callback_query(F.data == "minus")
async def select_fee_minus(call: CallbackQuery):
    fee.type = "minus"
    await call.message.answer(f"Какой налог вы хотите рассчитать?", reply_markup=keyboard_fee.as_markup())


@dp.callback_query(F.data == "6")
async def select_fee_(call: CallbackQuery):
    fee.size = 0.94
    await call.message.answer(f"Введите сумму, для которой расчитать налог")


@dp.callback_query(F.data == "7")
async def select_fee_(call: CallbackQuery):
    fee.size = 0.93
    await call.message.answer(f"Введите сумму, для которой расчитать налог")


@dp.callback_query(F.data == "8")
async def select_fee(call: CallbackQuery):
    fee.size = 0.92
    await call.message.answer(f"Введите сумму, для которой расчитать налог")

@dp.callback_query(F.data == "9")
async def select_fee_(call: CallbackQuery):
    fee.size = 0.91
    await call.message.answer(f"Введите сумму, для которой расчитать налог")


@dp.callback_query(F.data == "10")
async def select_fee(call: CallbackQuery):
    fee.size = 0.9
    await call.message.answer(f"Введите сумму, для которой расчитать налог")
