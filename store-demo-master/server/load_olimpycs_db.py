from main import get_olimpiads
import asyncio
from data.db_session import create_session, global_init
from data.olimpics import Olimp
from data.subjects import Subject
from data.olimp_subject import Olimp_Subject
from data.olimp_dates import Olimp_dates
from datetime import date, timedelta
from sqlalchemy import select


def new_olimpycs():  # загрузка олимпиад в бд
    session = create_session()
    pm = 0
    for i in get_olimpiads():  # цикл по всем олимпиадам
        if not session.query(Olimp).filter(Olimp.name == i[0]).all():  # добавление при отсутствии олимпиады в бд
            session.add(Olimp(name=i[0], desc=i[2], href=i[3], min_class=i[9], max_class=i[10]))
            session.commit()

            for j in i[1]:  # связь с предметами
                session.add(Olimp_Subject(olimp=session.query(Olimp.id).filter(Olimp.name == i[0]).first()[0],
                                          subject=session.query(Subject.id).filter(Subject.name == j.lower()).first()[
                                              0]))
                session.commit()

            for k in range(4, 9):
                for j in i[k]:
                    first_day = j['date'].split('-')
                    session.add(Olimp_dates(olimp=session.query(Olimp.id).filter(Olimp.name == i[0]).first()[0],
                                            start_date=date(int(first_day[0]), int(first_day[1]), int(first_day[2])),
                                            end_date=date(int(first_day[0]), int(first_day[1]),
                                                          int(first_day[2])) + timedelta(days=int(j['length'])),
                                            event=j.find('span', class_='tl_cont_f').find('font').get_text()))
                    session.commit()  # добавление сроков олимпиады

        else:
            q = select(Olimp_dates).select_from(Olimp_dates).join(Olimp, Olimp.id == Olimp_dates.olimp).where(Olimp.name == i[0])
            sel_dates = list(session.execute(q))
            sel_dates_list = [(x[0].event, x[0].start_date) for x in list(sel_dates)]
            for k in range(4, 9):
                for j in i[k]:
                    first_day = j['date'].split('-')
                    if (j.find('span', class_='tl_cont_f').find('font').get_text(), date(int(first_day[0]), int(first_day[1]), int(first_day[2]))) not in sel_dates_list:

                        session.add(Olimp_dates(olimp=session.query(Olimp.id).filter(Olimp.name == i[0]).first()[0],
                                            start_date=date(int(first_day[0]), int(first_day[1]), int(first_day[2])),
                                            end_date=date(int(first_day[0]), int(first_day[1]),
                                                          int(first_day[2])) + timedelta(days=int(j['length'])),
                                            event=j.find('span', class_='tl_cont_f').find('font').get_text()))
                        session.commit()  # добавление сроков олимпиады"""
    session.close()
