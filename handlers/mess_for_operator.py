from aiogram import types
from aiogram.dispatcher import FSMContext

from data import admins
from keyboards import markup_cancel, markup_main
from loader import dp, bot
from states import Question


@dp.message_handler(text="Связь с оператором")
async def enter_question(message: types.Message):
    await message.answer("Введите ваш вопрос.\nОператор свяжеться с вами в ближайшее время", reply_markup=markup_cancel)
    await Question.Q1.set() # присваивает машине состоянии - ответ


@dp.message_handler(state=Question.Q1) # получает этот  ответ
async def answer_for_question(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == "Отмена":
        await message.answer("Главная", reply_markup=markup_main)    # Возвращает к главному меню
        await state.finish()    # заканчивает состояние
    else:
        await state.update_data(answer1=answer)
        for admin in admins:    # Отправляет всем администраторам вопрос от пользователя
            if message.from_user.username:
                await bot.send_message(chat_id=admin, text=f"Вопрос от: @{message.from_user.username}\n{answer}")
            else:
                await bot.send_message(chat_id=admin, text=f"Вопрос от(id): {message.from_user.id}\n{answer}")
            await message.answer("Ваш вопрос отправлен. Ожидайте сообщения от оператора!")
        await state.finish()
