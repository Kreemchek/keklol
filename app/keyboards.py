from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)

from aiogram.utils.keyboard import InlineKeyboardBuilder

process = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Суть процесса 🧘‍♂️')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

process2 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Процесс очищения 🌱", callback_data='process2')]])

faq = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Частые вопросы ❓', callback_data='faq')]])

join_ask = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Начать очищение 🌿', callback_data='join')],
                                                 [InlineKeyboardButton(text='Задать вопрос 💬', url='https://t.me/Liana_gay')]])


money_builder = InlineKeyboardBuilder()


money_builder.button(text="Приобрести доступ 🔑",url='https://t.me/Liana_gay', callback_data="six")

#money_builder.button(text="6000р/месяц 💸",callback_data="sixteen")

# Строим клавиатуру
money = money_builder.as_markup()






#process3 = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Аллоха", callback_data='process3')]])
#mif = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='1 миф', callback_data='one_mif')],
                                           # [InlineKeyboardButton(text='2 миф', callback_data='two_mif')],
                                            #[InlineKeyboardButton(text='3 миф', callback_data='three_mif')],
                                            #[InlineKeyboardButton(text='Меню', callback_data='menu')]])

#back = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='2 миф', callback_data='two_back')],
                                             #[InlineKeyboardButton(text='3 миф', callback_data='three_mif')],
                                             #[InlineKeyboardButton(text='назад в меню')]])

