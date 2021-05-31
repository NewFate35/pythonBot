from aiogram import types


# Главная
markup_main = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
markup_main.add("Услуги")
markup_main.add("F.A.Q.", "Связь с оператором")

# Услуги
markup_services = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
markup_services.add("Консультация выбора ПК/Ноутбука")
markup_services.add("Сборка ПК")
markup_services.add("Ремонт")
markup_services.add("На главную")

# 1 кнопка - на главную
markup_toHome = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
markup_toHome.add("На главную")

# Назад к услугам + на главную
markup_toServices = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
markup_toServices.add("Назад")
markup_toServices.add("На главную")


# Отмена вопроса к оператору
markup_cancel = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
markup_cancel.add("Отмена")
