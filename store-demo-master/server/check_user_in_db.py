from data import db_session
from sqlalchemy import select
from data import users


def check_user_telegram_id_in_db(user_telegram_id):
    session = db_session.create_session()
    q = select(users.User).select_from(users.User).where(user_telegram_id == users.User.telegram_id)
    user_in_db = list(session.execute(q))
    if user_in_db:
        return True
    else:
        return False


def check_telegram_username_in_db_and_add_telegram_id(telegram_name):
    session = db_session.create_session()
    q = select(users.User).select_from(users.User).where(users.User.telegram_name == telegram_name)
    user_in_db = list(session.execute(q))
    if user_in_db:
        return True
    else:
        return False
