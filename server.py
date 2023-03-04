import telebot
from telebot import types

bot = telebot.TeleBot("5867307056:AAFLnmc7y6ktNOpQvqLFFl8FDHzlBCAKmeg")


@bot.message_handler(commands=['start'])
def start_message(message):
    # Создание кнопок
    markup = types.InlineKeyboardMarkup()
    new_hm = types.InlineKeyboardButton('Новое ГДЗ', callback_data='new_hw')
    essay = types.InlineKeyboardButton('Сочинение', callback_data='essay')
    markup.add(new_hm, essay)

    # Отправка сообщения и кнопок
    bot.send_message(message.chat.id, "Привет", reply_markup=markup)


@bot.callback_query_handlers(func=lambda callback: callback.data)
def gzd_message(callback):
    # Создание кнопок
    markup = types.InlineKeyboardMarkup()
    math_geo = types.InlineKeyboardButton('Математика/Геометрия', callback_data='math')
    phys = types.InlineKeyboardButton('Физика', callback_data='physics')
    chemistry = types.InlineKeyboardButton('Химия', callback_data='chemistry')
    markup.add(math_geo, phys, chemistry)

    # Отправка сообщения и кнопок
    bot.send_message(message.chat.id, "Выбери предмет", reply_markup=markup)

@bot.callback_query_handlers(func=lambda message: message.text == "Сочинение")
def essay_message(message):
    bot.send_message(message.chat.id, "Напишите тему для сочинения⬇️")



bot.polling()