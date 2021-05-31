from utils.misc import rate_limit
from aiogram import types
from loader import dp
from keyboards import markup_main


# Можно запускать раз в 10 сек
@rate_limit(limit=10)
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.reply("Выберите нужный вам пункт", reply_markup=markup_main)


@rate_limit(limit=10)
@dp.message_handler(commands="help")
async def helps(message: types.Message):
    return await message.answer("Помощь бога")
