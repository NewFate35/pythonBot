import logging

from aiogram.utils import executor

from handlers import dp
from utils.set_bot_commands import set_default_commands

# задаем уровень логов
logging.basicConfig(level=logging.DEBUG)


async def on_startup(dp):
    import middlewares  # импорт пакета, содержащий "анти-спам"
    from utils.notify_admins import on_startup_notify   # импорт функции, которая активируется при запуске бота

    middlewares.setup(dp)           # получает обработанный Dispatcher
    await on_startup_notify(dp)     # вызов асинхронной функции (сообщение админу)
    await set_default_commands(dp)  # вызов асинхронной функции (устанавливает команды бота)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)   # активация поллинга
