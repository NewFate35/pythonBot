from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import TOKEN


# инициализируем бота
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
# инициализация кучи
storage = MemoryStorage()
# инициализация Dispatcher, который будет обрабатывать хэндлеры
dp = Dispatcher(bot, storage=storage)