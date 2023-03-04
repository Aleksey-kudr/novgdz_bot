import telebot

# Вставьте ваш токен бота, который вы получили от BotFather
TOKEN = '*'

# Вставьте ссылку на ваш канал, которую вы хотите, чтобы пользователь подписался
CHANNEL_LINK = 'https://t.me/estetts'

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_handler(message):
    # Создаем объект клавиатуры и добавляем в нее кнопку
    keyboard = telebot.types.InlineKeyboardMarkup()
    subscribe_button = telebot.types.InlineKeyboardButton('Подписаться на канал', url=CHANNEL_LINK)
    check_button = telebot.types.InlineKeyboardButton('Проверить подписку', callback_data='check_subscription')
    keyboard.add(subscribe_button, check_button)

    # Отправляем сообщение пользователю с клавиатурой
    bot.send_message(message.chat.id, 'Привет! Подпишитесь на наш канал:', reply_markup=keyboard)

# Обработчик нажатия на кнопку "Проверить подписку"
@bot.callback_query_handler(func=lambda call: call.data == 'check_subscription')
def check_subscription_handler(call):
    user_id = call.from_user.id

    # Проверяем, подписан ли пользователь на канал
    is_subscribed = bot.get_chat_member(CHANNEL_LINK, user_id).status == 'member'

    if is_subscribed:
        bot.answer_callback_query(call.id, 'Вы подписаны на канал!')
    else:
        bot.answer_callback_query(call.id, 'Пожалуйста, подпишитесь на канал!')

# Запускаем бота
bot.polling()