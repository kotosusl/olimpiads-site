from data import db_session
import json
from data.subjects import Subject
from sqlalchemy import select


def load_subjects():
    session = db_session.create_session()
    q = select(Subject).select_from(Subject)
    sub = list(session.execute(q))
    if len(sub) == 0:
        with open('subject_to_code.json', encoding='utf-8') as file:
            dct = json.load(file)
            for i in dct:
                session.add(Subject(id=int(dct[i]),
                                    name=i))
                session.commit()
