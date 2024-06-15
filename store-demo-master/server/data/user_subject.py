import sqlalchemy
from .db_session import SqlAlchemyBase


class User_Subject(SqlAlchemyBase):
    __tablename__ = 'user_subject'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    subject_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('subjects.id'), nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey('users.id'), nullable=False)
