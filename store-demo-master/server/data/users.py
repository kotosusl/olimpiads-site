import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm
from datetime import time


class User(SqlAlchemyBase):  # таблица с пользователями
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Text, primary_key=True)
    telegram_name = sqlalchemy.Column(sqlalchemy.Text, unique=True)
    telegram_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True)
    name = sqlalchemy.Column(sqlalchemy.Text)
    surname = sqlalchemy.Column(sqlalchemy.Text)
    school_class = sqlalchemy.Column(sqlalchemy.Integer)
    email = sqlalchemy.Column(sqlalchemy.Text, unique=True, nullable=False)
    password = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    get_telegram_notifications = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    get_gmail_notifications = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    # использование в других таблицах
    olimp = orm.relationship('Relation')
    subject = orm.relationship('User_Subject')
    notification = orm.relationship('Notification')