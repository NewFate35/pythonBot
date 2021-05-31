from keyboards import markup_toServices, markup_services, inline_kb_pay
from aiogram.types import Message
from loader import dp


@dp.message_handler(text=["Услуги", "Назад"])
async def services(message: Message):
    await message.answer("Выберите нужный вам пункт", reply_markup=markup_services)


@dp.message_handler(text="Консультация выбора ПК/Ноутбука")
async def building_pc(message: Message):
    await message.answer("К оплате 700 рублей", reply_markup=markup_toServices)
    await message.answer("👇", reply_markup=inline_kb_pay)


@dp.message_handler(text="Сборка ПК")
async def building_pc(message: Message):
    await message.answer("К оплате 1500 руб", reply_markup=markup_toServices)
    await message.answer("👇", reply_markup=inline_kb_pay)


@dp.message_handler(text="Ремонт")
async def building_pc(message: Message):
    await message.answer("Ремонт вашей техники!!!", reply_markup=markup_toServices)
    await message.answer("👇", reply_markup=inline_kb_pay)
