from aiogram.types import Message
from loader import dp, fee
from num2words import num2words


def get_money_text(money_num: float):
    splited_num: list[str] = str(money_num).split('.')
    rub = num2words(splited_num[0], lang= 'ru')
    kop = str(splited_num[1])
    kop += " коп."
    last_word: str = (rub.split())[-1]
    if last_word == 'один':
        text =  rub + " рубль, " + kop
    elif last_word in {'два', 'три', 'четыре'}:
        text = rub + ' рубля, ' + kop
    else:
        text = rub + ' рублей, ' + kop
    return text


@dp.message()
async def calc_handler(message: Message) -> None:
    msg = ''.join(message.md_text.split('\\'))
    msg = msg.replace(",", ".")
    try:
        msg_clean = float(msg)
    except Exception:
        await message.answer(f"Некорректный ввод, используйте только числа и точку!")
    try:
        if fee.type == 'plus':
            result = round(msg_clean / fee.size, 2)
            await message.answer(f"Расчетная сумма + налог {int(100 - fee.size * 100)}%:\n\n"
                                 f"{result}")
        elif fee.type == 'minus':
            result = round(msg_clean * fee.size, 2)
            await message.answer(f"Твой расчет сумма - налог! Размер налога {int(100 - fee.size * 100)}%:\n"
                                 f"Расчетная сумма: {result}")
        await message.answer(f"{get_money_text(result)}")
    except Exception:
        if msg_clean:
            await message.answer("Nice try! Please start this bot...")


