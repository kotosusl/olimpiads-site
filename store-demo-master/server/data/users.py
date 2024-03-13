import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from datetime import time


class User(SqlAlchemyBase):  # таблица с пользователями
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    telegram_name = sqlalchemy.Column(sqlalchemy.Text)  # id в телеграме
    name = sqlalchemy.Column(sqlalchemy.Text)
    surname = sqlalchemy.Column(sqlalchemy.Text)
    age = sqlalchemy.Column(sqlalchemy.Integer)
    email = sqlalchemy.Column(sqlalchemy.Text, unique=True, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.Text, nullable=False)


    # использование в других таблицах
    olimp = orm.relationship('Relation')
