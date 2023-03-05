import telebot
from telebot import types
import time

client = telebot.TeleBot("*")


# Создание команды start и ответ на нее с кнопкой "Начать"
@client.message_handler(commands=["start"])
def start(message):
    makrup_inline = types.InlineKeyboardMarkup()
    markup_start = types.InlineKeyboardButton(text="Новое ГДЗ", callback_data="new_hm")
    markup_essay = types.InlineKeyboardButton(text="Сочинение", callback_data="essay")
    makrup_inline.add(markup_start, markup_essay)
    client.send_message(message.chat.id,
                        "<b>Привет!🥰\nВ этом боте собрана самая крупная база контрольных и домашек!</b>",
                        reply_markup=makrup_inline, parse_mode="html"
                        )


# Обработка кнопки "Начать"
@client.callback_query_handler(func=lambda call: True)
def answer_start(call):
    if call.data == "new_hm":
        markup_reply_1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_phys = types.KeyboardButton("Физика")
        markup_him = types.KeyboardButton("Химия")
        markup_geom = types.KeyboardButton("Геометрия")
        markup_geo = types.KeyboardButton("География")
        markup_bio = types.KeyboardButton("Биология")
        markup_ukr_litr = types.KeyboardButton("Укр. - яз./Литература")
        markup_eng = types.KeyboardButton("Английский язык")
        markup_math = types.KeyboardButton("Математика")
        markup_reply_1.add(markup_phys, markup_geom, markup_him, markup_geo, markup_bio, markup_ukr_litr, markup_eng,
                           markup_math
                           )
        client.send_message(call.message.chat.id, "<b>Выбери интересующий предмет ниже👇</b>",
                            reply_markup=markup_reply_1, parse_mode="html")
    elif call.data == "essay":
        markup_essay = types.ReplyKeyboardMarkup(resize_keyboard=True)
        makrup_essay_button = types.KeyboardButton("Отправлено!")
        markup_essay.add(makrup_essay_button)
        client.send_message(call.message.chat.id, "<b>Напишите тему для сочинения⬇️</b>", parse_mode="html", reply_markup=markup_essay)


@client.message_handler(content_types=["text"])
def get_photo(message):
    if message.text == "Физика":
        markup_send = types.ReplyKeyboardMarkup(resize_keyboard=True)
        makrup_send_button = types.KeyboardButton("Отправлено!")
        markup_send.add(makrup_send_button)
        client.send_message(message.chat.id, "<b>Прикрепи фото (чтобы было четко видно задание) и нажми Отправлено!</b>"
                            , reply_markup=markup_send, parse_mode="html")
    elif message.text == "Химия":
        markup_send_him = types.ReplyKeyboardMarkup(resize_keyboard=True)
        makrup_send_button_him = types.KeyboardButton("Отправлено!")
        markup_send_him.add(makrup_send_button_him)
        client.send_message(message.chat.id,
                            "<b>Прикрепи фото (чтобы было четко видно задание) и нажми Отправлено!</b>",
                            reply_markup=markup_send_him, parse_mode="html")
    elif message.text == "Геометрия":
        markup_send_geom = types.ReplyKeyboardMarkup(resize_keyboard=True)
        makrup_send_button_geom = types.KeyboardButton("Отправлено!")
        markup_send_geom.add(makrup_send_button_geom)
        client.send_message(message.chat.id,
                            "<b>Прикрепи фото (чтобы было четко видно задание) и нажми Отправлено!</b>",
                            reply_markup=markup_send_geom, parse_mode="html")
    elif message.text == "География":
        markup_send_geo = types.ReplyKeyboardMarkup(resize_keyboard=True)
        makrup_send_button_geo = types.KeyboardButton("Отправлено!")
        markup_send_geo.add(makrup_send_button_geo)
        client.send_message(message.chat.id,
                            "<b>Прикрепи фото (чтобы было четко видно задание) и нажми Отправлено!</b>",
                            reply_markup=markup_send_geo, parse_mode="html")
    elif message.text == "Биология":
        markup_send_bio = types.ReplyKeyboardMarkup(resize_keyboard=True)
        makrup_send_button_bio = types.KeyboardButton("Отправлено!")
        markup_send_bio.add(makrup_send_button_bio)
        client.send_message(message.chat.id,
                            "<b>Прикрепи фото (чтобы было четко видно задание) и нажми Отправлено!</b>",
                            reply_markup=markup_send_bio, parse_mode="html")
    elif message.text == "Укр. - яз./Литература":
        markup_send_ukr = types.ReplyKeyboardMarkup(resize_keyboard=True)
        makrup_send_button_ukr = types.KeyboardButton("Отправлено!")
        markup_send_ukr.add(makrup_send_button_ukr)
        client.send_message(message.chat.id,
                            "<b>Прикрепи фото (чтобы было четко видно задание) и нажми Отправлено!</b>",
                            reply_markup=markup_send_ukr, parse_mode="html")
    elif message.text == "Английский язык":
        markup_send_eng = types.ReplyKeyboardMarkup(resize_keyboard=True)
        makrup_send_button_eng = types.KeyboardButton("Отправлено!")
        markup_send_eng.add(makrup_send_button_eng)
        client.send_message(message.chat.id,
                            "<b>Прикрепи фото (чтобы было четко видно задание) и нажми Отправлено!</b>",
                            reply_markup=markup_send_eng, parse_mode="html")
    elif message.text == "Математика":
        markup_send_math = types.ReplyKeyboardMarkup(resize_keyboard=True)
        makrup_send_button_math = types.KeyboardButton("Отправлено!")
        markup_send_math.add(makrup_send_button_math)
        client.send_message(message.chat.id,
                            "<b>Прикрепи фото (чтобы было четко видно задание) и нажми Отправлено!</b>",
                            reply_markup=markup_send_math, parse_mode="html")
    elif message.text == "Отправлено!":
        client.send_message(message.chat.id, "Отлично! Фото распознано!✅")
        time.sleep(3)
        client.send_message(message.chat.id, "Обработка запроса...")
        time.sleep(3)
        client.send_message(message.chat.id, "Загрузка...")
        time.sleep(3)
        client.send_message(message.chat.id, "Приступаем к решению...")
        time.sleep(3)
        client.send_message(message.chat.id, "Выгрузка данных с серверов...")
        time.sleep(3)
        client.send_message(message.chat.id, "Загрузка...")
        markup_ready = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_ready_button = types.KeyboardButton("Продолжить")
        markup_ready.add(markup_ready_button)
        client.send_message(message.chat.id, "<b>Готово!✅ Жми на кнопку ниже</b>", reply_markup=markup_ready,
                            parse_mode="html")
    elif message.text == "Продолжить":
        markup_ready_2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_ready2_button = types.KeyboardButton("Получить решение")
        markup_ready_2.add(markup_ready2_button)
        client.send_message(message.chat.id, "<b>Решение найдено! Нажми на кнопку ниже</b>",
                            reply_markup=markup_ready_2, parse_mode="html")
    elif message.text == "Получить решение":
        markup_check_sub = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_check_button = types.KeyboardButton("Проверить подписку")
        markup_check_sub.add(markup_check_button)
        client.send_message(message.chat.id,
                            "<b>Отлично!\n⛔Для того, чтобы бот выслал решение, тебе остался последний шаг, "
                            "тебе необходимо подписаться на каналы спонсоры, благодаря которым наш "
                            "бот работает бесплатно</b> "
                            "\n1) <a href='https://t.me/+txD03dWrovI0NTdi'>Чат Аниме</a>"
                            "\n2) <a href='https://t.me/+7JyMfqQQaKZjMDBi'>СМИ</a>"
                            "\n3) <a href='https://t.me/+H8dDrnVBs_9hM2Zi'>COOL</a>"
                            "\n4) <a href='https://t.me/+eu1CdshiLNs2MTdi'>Книга Рекордов</a>"
                            "\n4) <a href='https://t.me/+afVr3w_RzqQzNTEy'>Жесть дня</a>"
                            "\n5) <a href='https://t.me/+XOMvOib_mi1lNDAy'>Наука и факты</a>"
                            "\n5) <a href='https://t.me/+Qp_bXfUgoZdmNDI6'>Новостник</a>"
                            "\n6) <a href='https://t.me/+pPv3cdNhACgzMDgy'>Темки и языки</a>"
                            "\n7) <a href='https://t.me/+S361H4x9RtE4OTY6'>Картинки Пинтерест</a>"

                            "\n<b>ПОСЛЕ ПОДПИСКИ, НАЖМИ ПРОВЕРИТЬ ПОДПИСКУ</b>", parse_mode="html",
                            reply_markup=markup_check_sub)
    elif message.text == "Проверить подписку":
        markup_sub = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup_sub_button = types.KeyboardButton("Я ПОДПИСАН(-А)")
        markup_sub.add(markup_sub_button)
        client.send_message(message.chat.id, "<b>⚠Доступ ограничен!⚠</b>\n<b>Проверьте подписку на всех спонсоров"
                                             " и нажмите кнопку ниже!</b>", parse_mode="html", reply_markup=markup_sub)
    elif message.text == "Я ПОДПИСАН(-А)":
        client.send_message(message.chat.id, "<b>Успешно!✅</b>\nК сожалению сейчас большая нагрузка на бот. В течение"
                                             " 24 часов придет ответ, ожидайте!<b> Следующие запросы будут обрабатываться мгновенно!</b>🤗\nВо время ожидания <b>нельзя отписываться"
                                             " от каналов спонсоров иначе бот остановит свою работу.</b>",
                            parse_mode="html")


client.polling(none_stop=True, interval=0)

Напиши телеграмм бота
1. /start выводит пользователю сообщение с ссылками на канал
2. По кнопке "Проверить подписку", бот должен проверять подписался ли пользователь на канал указаный в кнопке start