import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Notification(SqlAlchemyBase):
    __tablename__ = 'notifications'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    message_text = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    message_date = sqlalchemy.Column(sqlalchemy.Date, nullable=False)
    message_time = sqlalchemy.Column(sqlalchemy.Time, nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.id'), nullable=False)
    olimp_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('olimpycs.id'), nullable=False)


