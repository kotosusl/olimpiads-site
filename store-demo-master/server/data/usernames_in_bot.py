import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from datetime import time


class Usernames_in_bot(SqlAlchemyBase):  # таблица с пользователями
    __tablename__ = 'usernames_in_bot'

    id = sqlalchemy.Column(sqlalchemy.Text, primary_key=True, unique=True)
    telegram_username = sqlalchemy.Column(sqlalchemy.Text, unique=True)
    user_telegram_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True)
