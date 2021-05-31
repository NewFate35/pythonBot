from aiogram.types import Message

from keyboards import markup_main
from loader import dp


@dp.message_handler(text=["На главную", "Отмена"])
async def button_to_main(message: Message):
    await message.answer("Выберите нужный вам пункт", reply_markup=markup_main)
