from flask import Blueprint
from data import db_session
from data import users, user_subject, subjects
from validations import valid_telegram_name
from flask import jsonify, request
from token_required import token_required
from sqlalchemy import delete, insert
from uuid import uuid4

blueprint_edit_user_profile = Blueprint('blueprint_edit_user_profile', __name__)


@blueprint_edit_user_profile.route('/api/edit_user_profile', methods=['POST'])
@token_required
def editing_user_profile(current_user):
    session = db_session.create_session()
    json_obj = request.get_json() or {}
    user = session.query(users.User).filter(users.User.id == current_user.id).first()
    if json_obj.get('name', 0):
        user.name = json_obj['name']
    else:
        user.name = None
    if json_obj.get('surname', 0):
        user.surname = json_obj['surname']
    else:
        user.surname = None
    if json_obj.get('school_class', 0):
        user.school_class = int(json_obj['school_class'])
    if json_obj.get('telegram_name', 0):
        if valid_telegram_name(json_obj['telegram_name']) == 'OK':
            user.telegram_name = json_obj['telegram_name']
        else:
            session.close()
            return jsonify({"success": valid_telegram_name(json_obj['telegram_name'])})
    else:
        user.telegram_name = None
    if json_obj.get('subjects', 0):
        query = delete(user_subject.User_Subject).where(user_subject.User_Subject.user_id == current_user.id)
        session.execute(query)
        session.commit()
        for i in json_obj['subjects']:
            query = insert(user_subject.User_Subject).values(id=str(uuid4()), user_id=current_user.id, subject_id=session.query(subjects.Subject.id).filter(subjects.Subject.name == i.lower()).first()[0])
            session.execute(query)
            session.commit()
    else:
        query = delete(user_subject.User_Subject).where(user_subject.User_Subject.user_id == current_user.id)
        session.execute(query)
        session.commit()
    if json_obj.get('messages_places'):
        if 'Mail' in json_obj['messages_places']:
            user.get_gmail_notifications = True
        else:
            user.get_gmail_notifications = False
        if 'Telegram' in json_obj['messages_places']:
            user.get_telegram_notifications = True
        else:
            user.get_telegram_notifications = False
    else:
        user.get_telegram_notifications = False
        user.get_gmail_notifications = False

    if json_obj.get('male', 0):
        user.male = json_obj['male']

    session.commit()
    session.close()
    return jsonify({"success": "OK"})