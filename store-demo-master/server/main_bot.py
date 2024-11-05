import logging
# from secret_keys import TELEGRAM_BOT_TOKEN
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from data import db_session, users, usernames_in_bot
from sqlalchemy import select
from uuid import uuid4
from checker_dates_olimps import checker_dates_olimps
from keyboards import menu_keyboard_with_notif, menu_keyboard_without_notif, menu_keyboard_start
from os import environ

API_TOKEN = environ.get('TELEGRAM_BOT_TOKEN','')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
loop = asyncio.get_event_loop()
chat_ids = {}


@dp.message_handler(commands='start')
async def send_start_message(message: types.Message):
    try:
        session = db_session.create_session()

        if list(session.execute(
                select(users.User).select_from(users.User).where(
                        users.User.telegram_id == message.from_user.id))):
            text = f"""Привет, {message.from_user.full_name}!
Вы уже успешно привязали аккаунт к боту. 
Здесь будут приходить уведомления о тех олимпиадах, которые вы выбрали на сайте https://olimpik.klsh.ru. Команды бота: /help."""

            q = select(users.User).select_from(users.User).where(users.User.telegram_id == message.from_user.id)
            curr_user = list(session.execute(q))[0][0]
            if curr_user.get_telegram_notifications:
                session.close()
                await message.reply(text, reply_markup=menu_keyboard_with_notif)
            else:
                session.close()
                await message.reply(text, reply_markup=menu_keyboard_without_notif)

        else:
            if not list(session.execute(select(usernames_in_bot.Usernames_in_bot).select_from(
                    usernames_in_bot.Usernames_in_bot).where(usernames_in_bot.Usernames_in_bot.telegram_username == message.from_user.username))):
                new_username_in_db = usernames_in_bot.Usernames_in_bot(id=str(uuid4()),
                                                                       telegram_username=message.from_user.username,
                                                                       user_telegram_id=message.from_user.id)
                session.add(new_username_in_db)
                session.commit()
            session.close()
            await message.reply(f"""Привет, {message.from_user.full_name}!
В этом боте Вы сможете получать уведомления о тех олимпиадах, которые Вы выбрали на сайте https://olimpik.klsh.ru. Для продолжения перейдите на сайт, укажите Ваше имя пользователя Telegram(username) и нажмите "Проверить username". Помощь в боте: /help""",
                                reply=False, reply_markup=menu_keyboard_start)
    except Exception as err:
        await bot.send_message(1393667810, err)


@dp.message_handler(text=["Помощь"])
@dp.message_handler(commands='help')
async def send_help_message(message: types.Message):
    try:
        text = """Бот поддерживает следующие команды:
        
1. /start - Приветствие, подтверждение привязки аккаутна к боту.
2. /help - Помощь (данное сообщение).
3. /to_main_site - Ссылка на сайт с олимпиадами
4. /delete_notifications - Больше не присылать уведомления в боте.
5. /add_notifications - Начать присылать уведомления в боте."""

        session = db_session.create_session()
        q = select(users.User).select_from(users.User).where(users.User.telegram_id == message.from_user.id)
        curr_user = list(session.execute(q))
        if curr_user:
            curr_user = curr_user[0][0]
            if curr_user.get_telegram_notifications:
                session.close()
                await bot.send_message(message.from_user.id, text, reply_markup=menu_keyboard_with_notif)
            else:
                session.close()
                await bot.send_message(message.from_user.id, text, reply_markup=menu_keyboard_without_notif)
        else:
            session.close()
            await bot.send_message(message.from_user.id, text, reply_markup=menu_keyboard_start)
    except Exception as err:
        await bot.send_message(message.from_user.id, err, reply_markup=menu_keyboard_with_notif)


@dp.message_handler(text=['Ссылка на сайт'])
@dp.message_handler(commands='to_main_site')
async def to_main_site(message: types.Message):
    try:
        text = f'https://olimpik.klsh.ru/about'
        session = db_session.create_session()
        q = select(users.User).select_from(users.User).where(users.User.telegram_id == message.from_user.id)
        curr_user = list(session.execute(q))
        if curr_user:
            curr_user = curr_user[0][0]
            if curr_user.get_telegram_notifications:
                session.close()
                await bot.send_message(message.from_user.id, text, reply_markup=menu_keyboard_with_notif)
            else:
                session.close()
                await bot.send_message(message.from_user.id, text, reply_markup=menu_keyboard_without_notif)
        else:
            session.close()
            await bot.send_message(message.from_user.id, text, reply_markup=menu_keyboard_start)
    except Exception as err:
        await bot.send_message(1393667810, err)


@dp.message_handler(text=['Не присылать уведомления в боте'])
@dp.message_handler(commands='delete_notifications')
async def delete_notifications(message: types.Message):
    try:
        session = db_session.create_session()
        curr_user = session.query(users.User).where(users.User.telegram_id == message.from_user.id).first()
        if curr_user:
            if curr_user.get_telegram_notifications:
                curr_user.get_telegram_notifications = 0
                session.commit()
                text = "Уведомления в боте успешно отключены"

            else:
                text = 'Уведомления уже выключены'
            session.close()
            await bot.send_message(message.from_user.id, text, reply_markup=menu_keyboard_without_notif)
        else:
            session.close()
            await bot.send_message(message.from_user.id, 'Сначала зарегистрируйтесь на сайте и привяжите бот.', reply_markup=menu_keyboard_start)
    except Exception as err:
        await bot.send_message(1393667810, err)


@dp.message_handler(text=['Включить уведомления в боте'])
@dp.message_handler(commands='add_notifications')
async def add_notifications(message: types.Message):
    try:
        session = db_session.create_session()
        curr_user = session.query(users.User).where(users.User.telegram_id == message.from_user.id).first()
        if curr_user:
            if curr_user.get_telegram_notifications == 0:
                curr_user.get_telegram_notifications = 1
                session.commit()
                text = "Уведомления в боте успешно включены"

            else:
                text = 'Уведомления уже включены'
            session.close()
            await bot.send_message(message.from_user.id, text, reply_markup=menu_keyboard_with_notif)
        else:
            session.close()
            await bot.send_message(message.from_user.id, 'Сначала зарегистрируйтесь на сайте и привяжите бот.', reply_markup=menu_keyboard_start)
    except Exception as err:
        await bot.send_message(1393667810, err)


async def send_notifications_in_telegram_bot():
    try:
        while True:
            await asyncio.sleep(86390)
            users_of_sending = checker_dates_olimps()
            for user_telegram_id, user_msg in users_of_sending:
                if user_telegram_id:
                    await bot.send_message(user_telegram_id, user_msg)

    except Exception as err:
        await bot.send_message(1393667810, err)


async def f():
    await bot.send_message(1393667810, 'hi')


if __name__ == '__main__':
    db_session.global_init("../db/main_database.db")

    loop.create_task(f())
    loop.create_task(send_notifications_in_telegram_bot())
    executor.start_polling(dp)
