from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_kb_pay = InlineKeyboardMarkup(row_width=1)
inline_btn = InlineKeyboardButton('Оплатить', callback_data='button_pay')
inline_kb_pay.add(inline_btn)
# F.A.Q.
inline_kb_full = InlineKeyboardMarkup(row_width=1)
inline_btn_1 = InlineKeyboardButton('Как происходит оплата?', callback_data='button_1')
inline_btn_2 = InlineKeyboardButton('Как происходит консультуцаия по выбору ПК/Ноутбука?', callback_data='button_2')
inline_btn_3 = InlineKeyboardButton('Доставка', callback_data='button_3')
inline_btn_4 = InlineKeyboardButton('Гарантии', callback_data='button_4')
inline_btn_5 = InlineKeyboardButton('Нет нужного вопроса?', callback_data='button_5')

inline_kb_full.add(
    inline_btn_1,
    inline_btn_2,
    inline_btn_3,
    inline_btn_4,
    inline_btn_5)

inline_buttons = {
    1: 'Выбираете нужную вам услугу, переходете по выданной ссылке(нажав на кнопку) и оплачиваете, после чего с вами '
       'свяжется наш оператор',
    2: 'После оплаты, с вами связывается наш оператор для выяснения целей покупки/сборки ПК и ваш '
       'бюджет.\nПроанализовав рынок и нужные потребности, составляется список из выгодных для вас предложений',
    3: 'По Екатеринбургу - 200 рублей, остальные регионы - 500 рублей. Либо самовывоз',
    4: 'Предоставляем гарантию - 3 месяца (относится только к сборке ПК)',
    5: 'Напишите вопрос оператору(на главной)',
}
