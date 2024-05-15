from aiogram import types
from aiogram.filters import CommandStart

from Keyboards.Reply.MainKeyboard import main_keyboard
from loader import dp


@dp.message(CommandStart())
async def process_start_command(message: types.Message):
    await message.answer("Привіт\nЩоб анонімно подивитися сторіс користувача написни кнопку нижче та надішли його "
                         "юзернейм!", parse_mode='HTML', reply_markup=main_keyboard())
