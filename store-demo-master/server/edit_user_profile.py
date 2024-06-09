from flask import Blueprint
from data import db_session
from data import users
from validations import valid_telegram_name
from flask import jsonify, request
from token_required import token_required

blueprint_edit_user_profile = Blueprint('blueprint_edit_user_profile', __name__)


@blueprint_edit_user_profile.route('/api/edit_user_profile', methods=['POST'])
@token_required
def editing_user_profile(current_user):
    session = db_session.create_session()
    json_obj = request.get_json() or {}
    user = session.query(users.User).filter(users.User.id == current_user.id).first()
    if json_obj.get('name', 0):
        user.name = json_obj['name']
    if json_obj.get('surname', 0):
        user.surname = json_obj['surname']
    if json_obj.get('school_class', 0):
        user.school_class = int(json_obj['school_class'])
    if json_obj.get('telegram_name', 0):
        if valid_telegram_name(json_obj['telegram_name']) == 'OK':
            user.telegram_name = json_obj['telegram_name']
        else:
            return jsonify({"success": valid_telegram_name(json_obj['telegram_name'])})

    session.commit()
    return jsonify({"success": "OK"})