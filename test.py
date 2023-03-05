import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav
import config as cfg
URL_CHAT = "@channel_testpopa"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=cfg.TOKEN)
dp = Dispatcher(bot)

def check_sub_channels(chat_member):
    print(chat_member["status"])
    if chat_member["status"] != "left":
        return True
    else:
        return False

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    if check_sub_channels(await bot.get_chat_member(chat_id=URL_CHAT, user_id=message.from_user.id)):
        await bot.send_message(message.from_user.id, "Привет, харощь")
    else:
        await bot.send_message(message.from_user.id, "Не харощь")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)