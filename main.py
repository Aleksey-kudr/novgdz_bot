import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import config as cfg
import time
from aiogram.dispatcher import filters

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

#Создание кнопки start
@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "<b>Привет! 👋 \n"
                                                 "Этот бот поможет тебе с домашкой, контрольной, сочинениями и тд. \n"
                                                 "Выбери необходимую функцию⬇️</b>", reply_markup=nav.keyboard_menu,
                           parse_mode="html")

#Обработка кнопки start
@dp.callback_query_handler(text_contains="menu")
async def subject(call: types.CallbackQuery):
    if call.data == "menu_new_hm":
        await bot.send_message(call.from_user.id, "<b>Выбери предмет</b>", reply_markup=nav.keyboard_start_subject,
                               parse_mode="html")
    elif call.data == "menu_essay":
        await bot.send_message(call.from_user.id, "<b>Напишите тему для сочинения⬇️</b>", parse_mode="html")

#Обработка кнокпи предметов
@dp.callback_query_handler(text_contains="sub")
async def solution(call: types.CallbackQuery):
    await bot.send_message(call.from_user.id, "<b>Отправьте фото в этот бот.\nФото должно быть четкого качества.</b>",
                           parse_mode="html")

#Отправка фото после кнопок с предметами
@dp.message_handler(content_types=["photo"])
async def send_photo(message: types.Message):
    await bot.send_message(message.from_user.id, "Отлично!✅")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Загрузка...")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Проверка данных...")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Загрузка...")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "<b>Успешно!✅  Нажмите кнопку ниже</b", parse_mode="html",
                           reply_markup=nav.keyboard_next)

#Отправка темы сочинения начинается с кавычки
@dp.message_handler(filters.Text(startswith="\""))
async def essay_topic(message: types.Message):
    await bot.send_message(message.from_user.id, "Отлично!✅")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Загрузка...")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Проверка данных...")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "Загрузка...")
    time.sleep(3)
    await bot.send_message(message.from_user.id, "<b>Успешно!✅  Нажмите кнопку ниже</b>", parse_mode="html",
                           reply_markup=nav.keyboard_next)

@dp.callback_query_handler(text_contains="next")
async def next_step(message: types.CallbackQuery):
    await bot.send_message(message.from_user.id, "<b>Отлично, подпишись на каналы!</b>"
                                              "\n1) <a href='https://t.me/estetts'>Мой канал</a>",
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
        await bot.send_message(message.from_user.id, "GOOD")
    else:
        await bot.send_message(message.from_user.id, "Не харощь")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)