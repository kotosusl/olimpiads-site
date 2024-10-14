from sqlalchemy import select, insert
from data import db_session
from data import olimpics, olimp_dates, user_olimpyc, notifications, users
import datetime
from uuid import uuid4


def checker_dates_olimps():
    users_telegram_ids_and_msgs = []
    session = db_session.create_session()
    query = select(olimpics.Olimp)
    all_olimps = session.execute(query)
    for i in all_olimps:
        query = select(olimpics.Olimp, olimp_dates.Olimp_dates).select_from(olimpics.Olimp).join(olimp_dates.Olimp_dates, i[0].id == olimp_dates.Olimp_dates.olimp).where(i[0].id == olimpics.Olimp.id)
        one_olimp_dates = session.execute(query)
        query = select(users.User).select_from(users.User).join(user_olimpyc.Relation, user_olimpyc.Relation.user == users.User.id).where(i[0].id == user_olimpyc.Relation.olimp)
        #query = select(user_olimpyc.Relation.user).select_from(user_olimpyc.Relation).where(i[0].id == user_olimpyc.Relation.olimp)
        users_on_olimp = session.execute(query)
        for olimp, dates in one_olimp_dates:
            if datetime.date.today() + datetime.timedelta(days=3) == dates.start_date:
                for j in users_on_olimp:
                    msg = f'Через 3 дня проходит {dates.event} по мероприятию {olimp.name}. Длительность этапа (в днях): {(dates.end_date - dates.start_date).days}. Подробнее об олимпиаде: https://olimpiada.ru{olimp.href}'
                    time_now = datetime.datetime.now().time().strftime('%H:%M:%S')
                    query = insert(notifications.Notification).values(id=str(uuid4()), user_id=j[0].id, olimp_id=olimp.id,
                    message_text=msg,
                    message_date=str(datetime.date.today()),
                    message_time=time_now)
                    session.execute(query)
                    session.commit()
                    if j[0].get_telegram_notifications:
                        users_telegram_ids_and_msgs.append((j[0].telegram_id, msg))

            if datetime.date.today() + datetime.timedelta(days=1) == dates.start_date:
                for j in users_on_olimp:
                    msg = f'Уже завтра проходит {dates.event} по мероприятию {olimp.name}. Длительность этапа (в днях): {(dates.end_date - dates.start_date).days}. Подробнее об олимпиаде: https://olimpiada.ru{olimp.href}'
                    time_now = datetime.datetime.now().time().strftime('%H:%M:%S')
                    query = insert(notifications.Notification).values(id=str(uuid4()), user_id=j[0].id, olimp_id=olimp.id,
                    message_text=msg, message_date=str(datetime.date.today()), message_time=time_now)
                    session.execute(query)
                    session.commit()
                    if j[0].get_telegram_notifications:
                        users_telegram_ids_and_msgs.append((j[0].telegram_id, msg))

            delta_days = dates.end_date - dates.start_date
            if datetime.date.today() + datetime.timedelta(days=1) == dates.end_date and delta_days.days >= 3:
                for j in users_on_olimp:
                    msg = f'Завтра заканчивается {dates.event} по мероприятию {olimp.name}. Подробнее об олимпиаде: https://olimpiada.ru{olimp.href}'
                    time_now = datetime.datetime.now().time().strftime('%H:%M:%S')
                    query = insert(notifications.Notification).values(id=str(uuid4()), user_id=j[0].id, olimp_id=olimp.id,
                    message_text=msg, message_date=str(datetime.date.today()), message_time=time_now)
                    session.execute(query)
                    session.commit()
                    if j[0].get_telegram_notifications:
                        users_telegram_ids_and_msgs.append((j[0].telegram_id, msg))
    session.close()
    return users_telegram_ids_and_msgs