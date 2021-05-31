from aiogram import types

from keyboards import inline_buttons
from keyboards import inline_kb_full, markup_toHome
from loader import dp, bot


@dp.message_handler(text="F.A.Q.")
async def faq(message: types.Message):
    await message.reply("Частые вопросы:", reply_markup=inline_kb_full)
    await message.answer("Выберите нужный вам пункт", reply_markup=markup_toHome)


@dp.callback_query_handler(text_contains='button_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("button_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        for k, v in inline_buttons.items():
            if k == code:
                await bot.send_message(call.from_user.id, text=v)
                # await bot.answer_callback_query(call.id, text=v)
        else:
            await bot.answer_callback_query(call.id)
