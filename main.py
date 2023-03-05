import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import config as cfg
import time

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "<b>Привет! 👋 \n"
                                                 "Этот бот поможет тебе с домашкой, контрольной, сочинениями и тд. \n"
                                                 "Выбери необходимую функцию⬇️</b>", reply_markup=nav.keyboard_menu,
                           parse_mode="html")

@dp.callback_query_handler(text_contains="menu")
async def subject(call: types.CallbackQuery):
    if call.data == "menu_new_hm":
        await bot.send_message(call.from_user.id, "<b>Выбери предмет</b>", reply_markup=nav.keyboard_start_subject,
                               parse_mode="html")
    elif call.data == "menu_essay":
        await bot.send_message(call.from_user.id, "<b>Напишите тему для сочинения\nи нажмите кнопку ниже</b>⬇️",
                               parse_mode="html",
                               reply_markup=nav.keyboard_send)

@dp.callback_query_handler(text_contains="sub")
async def solution(call: types.CallbackQuery):
    if call.data == "sub_send":
        await bot.send_message(call.from_user.id, "Отлично!✅")
        time.sleep(3)
        await bot.send_message(call.from_user.id, "Загрузка...")
        time.sleep(3)
        await bot.send_message(call.from_user.id, "Проверка данных...")
        time.sleep(3)
        await bot.send_message(call.from_user.id, "Загрузка...")
        time.sleep(3)
        await bot.send_message(call.from_user.id, "Успешно!✅  Нажмите кнопку ниже")
    else:
        await bot.send_message(call.from_user.id, "<b>Отправьте фото в этот бот.\nФото должно быть четкого качества.</b>",
                           parse_mode="html")

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
    await bot.send_message(message.from_user.id, "Успешно!✅  Нажмите кнопку ниже")



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)