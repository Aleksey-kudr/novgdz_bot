import telebot
from telebot import types

bot = telebot.TeleBot("*")


@bot.message_handler(commands=['start'])
def start_message(message):
    # Создание кнопок
    markup = types.InlineKeyboardMarkup()
    new_hm = types.InlineKeyboardButton('Новое ГДЗ', callback_data='new_hw')
    essay = types.InlineKeyboardButton('Сочинение', callback_data='essay')
    markup.add(new_hm, essay)

    # Отправка сообщения и кнопок
    bot.send_message(message.chat.id, "<b>Привет! 👋 "
                                      "\nЭтот бот поможет тебе с домашкой, контрольной, сочинениями и тд. "
                                      "\nВыбери необходимую функцию⬇️</b>", parse_mode="HTML", reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: callback.data)
def gzd_message(callback):
    if callback.data == "new_hw":
    # Создание кнопок
        markup = types.InlineKeyboardMarkup(row_width=1)
        math_geo = types.InlineKeyboardButton('Математика/Геометрия', callback_data='math')
        phys = types.InlineKeyboardButton('Физика', callback_data='physics')
        chemistry = types.InlineKeyboardButton('Химия', callback_data='chemistry')
        markup.add(math_geo, phys, chemistry)

    # Отправка сообщения и кнопок
        bot.send_message(callback.message.chat.id, "<b>Выбери предмет</b>", parse_mode="HTML", reply_markup=markup)
    elif callback.data == "essay":
        bot.send_message(callback.message.chat.id, "Напишите тему для сочинения⬇️")



bot.polling()