from data import db_session
from data import users
from flask import jsonify, request
import jwt
from functools import wraps
from secret_keys import APP_CONFIG_SECRET_KEY


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        try:
            data = jwt.decode(token, APP_CONFIG_SECRET_KEY, algorithms='HS256')
            session = db_session.create_session()
            current_user = session.query(users.User).filter(users.User.id == data['id']).first()
        except Exception as err:
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        return f(current_user, *args, **kwargs)

    return decorated