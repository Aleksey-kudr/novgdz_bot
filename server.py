import telebot
from telebot import types

bot = telebot.TeleBot("5867307056:AAFLnmc7y6ktNOpQvqLFFl8FDHzlBCAKmeg")


@bot.message_handler(commands=['start'])
def start_message(message):
    # Создание кнопок
    markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton('Новое ГДЗ', callback_data='new_hw')
    itembtn2 = types.InlineKeyboardButton('Сочинение', callback_data='essay')
    markup.add(itembtn1, itembtn2)

    # Отправка сообщения и кнопок
    bot.send_message(message.chat.id, "Привет", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Новое ГДЗ")
def gzd_message(message):
    # Создание кнопок
    markup = types.InlineKeyboardMarkup()
    itembtn1 = types.InlineKeyboardButton('Математика/Геометрия', callback_data='math')
    itembtn2 = types.InlineKeyboardButton('Физика', callback_data='physics')
    itembtn3 = types.InlineKeyboardButton('Химия', callback_data='chemistry')
    markup.add(itembtn1, itembtn2, itembtn3)

    # Отправка сообщения и кнопок
    bot.send_message(message.chat.id, "Выбери предмет", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "new_hw":
        # Создание кнопок
        markup = types.InlineKeyboardMarkup()
        itembtn1 = types.InlineKeyboardButton('Математика/Геометрия', callback_data='math')
        itembtn2 = types.InlineKeyboardButton('Физика', callback_data='physics')
        itembtn3 = types.InlineKeyboardButton('Химия', callback_data='chemistry')
        markup.add(itembtn1, itembtn2, itembtn3)

        # Отправка сообщения и кнопок
        bot.send_message(call.message.chat.id, "Выбери предмет", reply_markup=markup)
    elif call.data == "essay":
        bot.send_message(call.message.chat.id, "Напишите тему для сочинения")
        bot.register_next_step_handler(call.message, write_essay_topic)
    elif call.data == "math":
        bot.send_message(call.message.chat.id, "Отправьте фото в этот бот. Фото должно быть четкого качества.")
        bot.register_next_step_handler(call.message, send_photo)
    elif call.data == "physics":
        bot.send_message(call.message.chat.id, "Отправьте фото в этот бот. Фото должно быть четкого качества.")
        bot.register_next_step_handler(call.message, send_photo)
    elif call.data == "chemistry":
        bot.send_message(call.message.chat.id, "Отправьте фото в этот бот. Фото должно быть четкого качества.")
        bot.register_next_step_handler(call.message, send_photo)
def send_photo(message):
    try:
        # Проверка, отправил ли пользователь фото
        if message.photo:
            bot.send_message(message.chat.id, "Отлично")
        else:
            bot.send_message(message.chat.id, "Ошибка")
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка")

bot.polling()