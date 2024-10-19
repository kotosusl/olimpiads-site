from flask import Blueprint
from data import db_session, notifications
from token_required import token_required
from sqlalchemy import select
from datetime import datetime


blueprint_get_notifications = Blueprint('blueprint_get_notifications', __name__)


@blueprint_get_notifications.route('/api/get_notifications', methods=['GET'])
@token_required
def get_notifications(current_user):
    session = db_session.create_session()
    query = select(notifications.Notification).select_from(notifications.Notification).where(notifications.Notification.user_id == current_user.id)
    res = session.execute(query)
    res.sort(key=lambda x: int(''.join(str(x[0].message_date).split('-')) + ''.join(str(x[0].message_time).split(':'))), reverse=True)
    jsn = {
        'success': 'OK',
        'notifications': [
            {
                'id': p[0].id,
                'message_text': p[0].message_text,
                'message_date': p[0].message_date,
                'message_time': str(p[0].message_time),
                'user_id': p[0].user_id,
                'olimp_id': p[0].olimp_id
            } for p in res
        ]
    }
    session.close()
    return jsn