import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import config as cfg
import time
from aiogram.dispatcher import filters
from db import Database

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)
db = Database('database.db')

#Создание кнопки start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if not db.user_exists(message.from_user.id):
        db.add_user(message.from_user.id)
    await bot.send_message(message.from_user.id, "<b>Привет! 👋 \n"
                                                 "Этот бот поможет тебе с домашкой, контрольной, сочинениями и тд. \n"
                                                 "Выбери необходимую функцию⬇️</b>", reply_markup=nav.keyboard_menu,
                           parse_mode="html")
#Создание кнопки рассылки
@dp.message_handler(commands=["sendall"])
async def sendall(message: types.Message):
    if message.from_user.id == 5832872782:
        users = db.get_users()
        for row in users:
            try:
                await bot.send_message(row[0], "<b>Наконец-то очередь дошла до тебя! Просим прощения за долгое ожидание</b> ❤️ К сожалению, была <b>большая нагрузка</b> на бот.\n\n"
                                               "Мы уже выслали материал <b>более 23к пользователям</b> и бот готов выслать тебе, но не заметил подписку на эти каналы:"
                                               "\n\n1) <a href='https://t.me/+tFvYNeH4oUA4ZDFi'>Женский дневник</a>"
                                               "\n2) <a href='https://t.me/+TGiQC4xTYopkMjQy'>Мечтай</a>"
                                               "\n\nПосле проверки подписки бот продолжит работу и Вам <b>придет материал. Ожидайте❤️</b>", parse_mode = "html")
        users = db.get_users()
        for row in users:
            try:
                await bot.send_message(row[0], text)
                if int(row[1]) != 1:
                    db.set_active(row[0], 1)
            except:
                db.set_active(row[0], 0)
        await bot.send_message(message.from_user.id, "Успешная рассылка")


#Обработка кнопки start
@dp.callback_query_handler(text_contains="menu")
async def subject(call: types.CallbackQuery):
    if call.data == "menu_new_hm":
        await bot.send_message(call.from_user.id, "<b>Выбери предмет</b>", reply_markup=nav.keyboard_start_subject,
                               parse_mode="html")
    elif call.data == "menu_essay":
        await bot.send_message(call.from_user.id, "<b>Напишите тему для сочинения (обязательно с точкой) ⬇️</b>\n\n"
                                                  "Например:\n"
                                                  "Как я провёл лето.\n"
                                                  "Что такое любовь.\n"
                                                  "И т.д.️", parse_mode="html")

#Обработка кнокпи предметов
@dp.callback_query_handler(text_contains="sub")
async def solution(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "<b>Отправьте фото в этот бот.\nФото должно быть хорошего качества.</b>",
                           parse_mode="html")

#Отправка фото после кнопок с предметами
@dp.message_handler(content_types=["photo"])
async def send_photo(message: types.Message):
    await bot.send_message(message.from_user.id, "<b>Отлично!✅</b>", parse_mode="html")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "<i>Загрузка...</i>", parse_mode="html")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "<i>Проверка данных...</i>", parse_mode="html")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "<i>Загрузка...</i>", parse_mode="html")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "<b>Успешно!✅\n\n"
                                                 "Нажмите кнопку ниже</b>", parse_mode="html",
                           reply_markup=nav.keyboard_next)

#Отправка темы сочинения начинается с кавычки
@dp.message_handler(filters.Text(endswith="."))
async def essay_topic(message: types.Message):
    await bot.send_message(message.from_user.id, "<b>Отлично!✅</b>", parse_mode="html")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "<i>Загрузка...</i>", parse_mode="html")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "<i>Проверка данных...</i>", parse_mode="html")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "<i>Загрузка...</i>", parse_mode="html")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "<b>Успешно!✅\n\n"
                                                 "Нажмите кнопку ниже</b>", parse_mode="html",
                           reply_markup=nav.keyboard_next)

@dp.callback_query_handler(text_contains="next")
async def next_step(message: types.CallbackQuery):
    await bot.send_message(message.from_user.id, "<b>Отлично!</b>\n"
                                                 "\n⛔Для того, чтобы использовать нашего бота, "
                                                 "тебе <b>необходимо подписаться на каналы спонсоры,"
                                                 "благодаря которым наш бот работает бесплатно </b>\n"
                                           
                                                 "\n1) <a href='https://t.me/+C1gJJZvZTB1kNGFi'>Алина Морозова</a>"
                                                 "\n2) <a href='https://t.me/+RfnxztguzIVmYWRi'>Новости</a>"  
                                                 "\n2) <a href='https://t.me/+4iC742RG1VdkNmIy'>Змеиное гнездо</a>"
                                                 "\n3) <a href='https://t.me/+rDsALfB2HrYwYTBi'>RTVI</a>"
                                                 "\n4) <a href='https://t.me/+SIxsukR3sWM4OWYy'>radioшоу</a>"
                                                 "\n5) <a href='https://t.me/+P0h9opjr-pA1NzUy'>Testo</a>"
                                                 "\n5) <a href='https://t.me/+_FgIfvxdwrk3NWZi'>Aesthetics</a>"
                                                 "\n6) <a href='https://t.me/+bs1bckvZ6eRiMmQy'>Выжималка</a>",
                               parse_mode="html", reply_markup=nav.keyboard_check)

def check_sub_channels(chat_member):
    print(chat_member["status"])
    if chat_member["status"] != "left":
        return True
    else:
        return False

@dp.callback_query_handler(text_contains="check")
async def check(message:types.CallbackQuery):
    if check_sub_channels(await bot.get_chat_member(chat_id=cfg.URL_CHAT, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "<b>Успешно!✅</b>\n\n"
                                                     "К сожалению сейчас большая нагрузка на бот. "
                                                     "В течение <b>24-48 часов</b> придет ответ, ожидайте!🤗 "
                                                     "<b>В дальнейшем запрос будет обрабатываться мгновенно!</b> "
                                                     "Во время ожидания <b>нельзя отписываться</b> от каналов спонсоров, "
                                                     "иначе бот остановит свою работу.", parse_mode="html")
    else:
        await bot.send_message(message.from_user.id, "<b>‼Подпишитесь на все каналы</b>", parse_mode="html")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
