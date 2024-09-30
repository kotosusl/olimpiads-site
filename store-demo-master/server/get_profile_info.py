from flask import Blueprint
from data import db_session
from flask import jsonify, request
from token_required import token_required
from data import olimpics, subjects, olimp_subject, user_olimpyc, users, user_subject
from sqlalchemy import select

blueprint_get_profile_info = Blueprint('blueprint_get_profile_info', __name__)


@blueprint_get_profile_info.route('/api/get_profile_info', methods=['POST'])
@token_required
def get_profile_info(current_user):
    try:
        session = db_session.create_session()
        q = select(users.User).select_from(users.User).where(users.User.id == current_user.id)
        profile_info = list(session.execute(q))[0][0]
        q = select(subjects.Subject.name).select_from(subjects.Subject).join(user_subject.User_Subject,
                                                                             user_subject.User_Subject.subject_id == subjects.Subject.id).join(
            users.User, user_subject.User_Subject.user_id == users.User.id).where(current_user.id == users.User.id)
        user_subjects_info = session.execute(q)
        message_places = []
        if profile_info.get_telegram_notifications:
            message_places.append('Telegram')
        if profile_info.get_gmail_notifications:
            message_places.append('Mail')
        jsn = {
                'success': 'OK',
                'profile_info': {
                    "user_id": profile_info.id,
                    "name": profile_info.name,
                    "surname": profile_info.surname,
                    "male": profile_info.male,
                    "school_class": profile_info.school_class,
                    "subjects": [p[0] for p in user_subjects_info],
                    "email": profile_info.email,
                    "messages_places": message_places,
                    "telegram_name": profile_info.telegram_name
                }
            }
        session.close()
        return jsonify(jsn)
    except Exception as err:
        return jsonify({'success': 'ERROR'})