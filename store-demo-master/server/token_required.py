from data import db_session
from data import users
from flask import jsonify, request
import jwt
from functools import wraps
# from secret_keys import APP_CONFIG_SECRET_KEY
from os import environ

APP_CONFIG_SECRET_KEY = environ.get('APP_CONFIG_SECRET_KEY', '')
TOKEN_ALGORITHM = environ.get('TOKEN_ALGORITHM', '')


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'success': 'Token is missing'})

        try:
            data = jwt.decode(token, APP_CONFIG_SECRET_KEY, algorithms=TOKEN_ALGORITHM)
            session = db_session.create_session()
            current_user = session.query(users.User).filter(users.User.id == data['id']).first()
            session.close()
            return f(current_user, *args, **kwargs)
        except Exception as err:
            print(err)
            return jsonify({
                'success': 'Token is invalid'
            })


    return decorated