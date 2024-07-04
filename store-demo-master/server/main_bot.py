import logging
from secret_keys import TELEGRAM_BOT_TOKEN
import asyncio
from datetime import datetime
from aiogram import Bot, Dispatcher, executor, types
from check_user_in_db import check_user_telegram_id_in_db
from data import db_session, users
from sqlalchemy import select

API_TOKEN = TELEGRAM_BOT_TOKEN
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

chat_ids = {}

@dp.message_handler(commands='start')
async def echo(message: types.Message):
    if check_user_telegram_id_in_db(message.from_user.id):
        text = f"""Привет, {message.from_user.full_name}!
Вы уже зарегистрировались на сайте. 
Здесь будут приходить уведомления о тех олимпиадах, которые вы выбрали на сайте {111}."""
    else:
        # проверить ниже
        if check_user_telegram_id_in_db(message.from_user.username):
            text = f"""Привет, {message.from_user.full_name}!
Твой аккаунт успешно найден. Здесь будут расположены уведомления о твоих олимпиадах."""
            session = db_session.create_session()
            q = select(users.User).select_from(users.User).where(users.User.telegram_name == message.from_user.username)
            user = list(session.execute(q))[0]
            user.telegram_id = message.from_user.id
            session.commit()
        else:
            text = f"""Привет, {message.from_user.full_name}!
Чтобы продолжить, зарегистрируйся на сайте {111}."""
    await message.reply(text, reply=False)


async def periodic(sleep_for):
    while True:
        await asyncio.sleep(sleep_for)
        now = datetime.utcnow()
        print(f"{now}")
        for id in chat_ids:
            await bot.send_message(id, f"{now}", disable_notification=True)


async def f():
    await bot.send_message(1393667810, 'hi')


if __name__ == '__main__':
    db_session.global_init("../db/main_database.db")
    loop = asyncio.get_event_loop()
    loop.create_task(f())
    executor.start_polling(dp)
