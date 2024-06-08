from uuid import uuid4
from flask import Flask
from data import db_session
from load_olimpycs_db import new_olimpycs
from load_subjects import load_subjects
from flask_restful import reqparse, abort, Api, Resource
from data import users
from validations import valid_email, valid_password, valid_school_class, valid_telegram_name
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify, request
from base64 import b64encode, b64decode
import jwt
from datetime import datetime, timedelta
from functools import wraps
from secret_keys import APP_CONFIG_SECRET_KEY


app = Flask(__name__)
api = (Api(app))
app.config['SECRET_KEY'] = APP_CONFIG_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms='HS256')
            session = db_session.create_session()
            current_user = session.query(users.User).filter(users.User.id == data['id']).first()
        except Exception as err:
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        return f(current_user, *args, **kwargs)

    return decorated


@app.route('/api/test', methods=['GET'])
@token_required
def test(current_user):
    return jsonify({'success': 'AAAAAAAA'})



@app.route('/api/login', methods=['POST'])
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
                }, app.config['SECRET_KEY'], algorithm='HS256')
                return jsonify({'success': 'OK', 'token': token})
        else:
            return jsonify({'success': 'no user with such email'})
    else:
        return jsonify({'success': 'no email or password'})


@app.route('/api/add_user', methods=['POST'])
def adding_user():
    try:
        session = db_session.create_session()
        json_obj = request.get_json() or {}
        if json_obj.get('email', 0) and json_obj.get('password', 0):
            if valid_email(json_obj['email']) != 'OK':
                return jsonify({'success': valid_email(json_obj['email'])})
            if valid_password(json_obj['password']) != 'OK':
                return jsonify({'success': valid_password(json_obj['password'])})
            if not (session.query(users.User).filter(users.User.email == json_obj['email']).all()):
                new_user = users.User(id=str(uuid4()),
                                      email=json_obj['email'],
                                      password=generate_password_hash(json_obj['password']))
                session.add(new_user)
                session.commit()
                return jsonify({'success': 'OK'})
            else:
                return jsonify({'success': 'email already exists'}), 202
        else:
            return jsonify({'success': 'no email or password'})
    except Exception as err:
        print(err)
        return jsonify({'success': 'ERROR'}), 500


@app.route('/api/edit_user_profile', methods=['POST'])
@token_required
def editing_user_profile():
    session = db_session.create_session()
    json_obj = request.get_json() or {}
    user = session.query(users.User).filter(users.User.email == json_obj['email']).first()
    if user:
        if json_obj.get('name', 0):
            user.name = json_obj['name']
        if json_obj.get('surname', 0):
            user.surname = json_obj['surname']
        if json_obj.get('school_class', 0):
            if valid_school_class(json_obj['school_class']) == "OK":
                user.school_class = int(json_obj['school_class'])
            else:
                return jsonify({"success": valid_school_class(json_obj['school_class'])})
        if json_obj('telegram_name', 0):
            if valid_telegram_name(json_obj['telegram_name']) == 'OK':
                user.telegram_name = json_obj['telegram_name']
            else:
                return jsonify({"success": valid_telegram_name(json_obj['telegram_name'])})

        session.commit()
        return jsonify({"success": "OK"})
    else:
        return jsonify({"success": "no user with this email"})


if __name__ == "__main__":
    db_session.global_init("../db/main_database.db")
    #load_subjects()
    #new_olimpycs()
    app.run(host='127.0.0.1', port=8888)



