from data import db_session
from data import users
from werkzeug.security import check_password_hash
from flask import jsonify, request, Blueprint
import jwt
from datetime import datetime, timedelta
from secret_keys import APP_CONFIG_SECRET_KEY


blueprint_login = Blueprint('blueprint_login', __name__)


@blueprint_login.route('/api/login', methods=['POST'])
def logining():
    session = db_session.create_session()
    json_obj = request.get_json() or {}
    if json_obj.get('email', 0) and json_obj.get('password', 0):
        user_in_db = session.query(users.User).filter(users.User.email == json_obj['email']).all()
        if user_in_db:
            if check_password_hash(user_in_db[0].password, json_obj['password']):
                token = jwt.encode({
                    'id': user_in_db[0].id,
                    'exp': datetime.utcnow() + timedelta(hours=1)
                }, APP_CONFIG_SECRET_KEY, algorithm='HS256')
                return jsonify({'success': 'OK', 'token': token})
        else:
            return jsonify({'success': 'Неверный email или пароль'})
    else:
        return jsonify({'success': 'Введите email и пароль'})