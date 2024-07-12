from sqlalchemy import select, insert
from data import db_session
from data import olimpics, olimp_dates, user_olimpyc, notifications
import datetime
from uuid import uuid4


def checker_dates_olimps():
    session = db_session.create_session()
    query = select(olimpics.Olimp)
    all_olimps = session.execute(query)
    for i in all_olimps:
        query = select(olimpics.Olimp, olimp_dates.Olimp_dates).select_from(olimpics.Olimp).join(olimp_dates.Olimp_dates, i[0].id == olimp_dates.Olimp_dates.olimp)
        one_olimp_dates = session.execute(query)
        query = select(user_olimpyc.Relation.user).select_from(user_olimpyc.Relation).where(i[0].id == user_olimpyc.Relation.olimp)
        users_on_olimp = session.execute(query)
        for olimp, dates in one_olimp_dates:
            if datetime.date.today() + datetime.timedelta(days=3) == dates.start_date:
                for j in users_on_olimp:
                    time_now = datetime.datetime.now().time().strftime('%H:%M:%S').split(':')
                    query = insert(notifications.Notification).values(id=str(uuid4()), user_id=j[0], olimpid=olimp.id,
                    message_text=f'Через 3 дня проходит {dates.event} по мероприятию {olimp.name}. Длительность этапа (в днях): {(dates.end_date - dates.start_date).days}.',
                    message_date=datetime.date.today(),
                    message_time=datetime.time(hour=int(time_now[0]), minute=int(time_now[1]), second=int(time_now[2])))
                    session.execute(query)
                    session.commit()

            if datetime.date.today() + datetime.timedelta(days=1) == dates.start_date:
                for j in users_on_olimp:
                    time_now = datetime.datetime.now().time().strftime('%H:%M:%S').split(':')
                    query = insert(notifications.Notification).values(id=str(uuid4()), user_id=j[0], olimpid=olimp.id,
                    message_text=f'Уже завтра проходит {dates.event} по мероприятию {olimp.name}. Длительность этапа (в днях): {(dates.end_date - dates.start_date).days}.', message_date=datetime.date.today(), message_time=datetime.time(hour=int(time_now[0]), minute=int(time_now[1]), second=int(time_now[2])))
                    session.execute(query)
                    session.commit()

            delta_days = dates.end_date - dates.start_date
            if datetime.date.today() + datetime.timedelta(days=1) == dates.end_date and delta_days.days >= 3:
                for j in users_on_olimp:
                    time_now = datetime.datetime.now().time().strftime('%H:%M:%S').split(':')
                    query = insert(notifications.Notification).values(id=str(uuid4()), user_id=j[0], olimp_id=olimp.id,
                    message_text=f'Завтра заканчивается {dates.event} по мероприятию {olimp.name}.', message_date=datetime.date.today(), message_time=datetime.time(hour=int(time_now[0]), minute=int(time_now[1]), second=int(time_now[2])))
                    session.execute(query)
                    session.commit()