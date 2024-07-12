import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Relation(SqlAlchemyBase):  # таблица "многие ко многим", связь пользователей с олимпиадами
    __tablename__ = 'user_olimpyc'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    user = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.id'), nullable=False)  # пользователь
    olimp = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('olimpycs.id'), nullable=False)  # олимпиада
