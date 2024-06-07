from flask import Flask
from data import db_session
from load_olimpycs_db import new_olimpycs
from load_subjects import load_subjects
from flask_restful import reqparse, abort, Api, Resource
from data import users
import add_user
from validations import valid_email, valid_password, valid_school_class, valid_telegram_name
from flask import jsonify, request


app = Flask(__name__)
api = (Api(app))


@app.route('/api/add_user', methods=['POST'])
def adding_user():
    try:
        session = db_session.create_session()
        json_obj = request.get_json() or {}
        print(request.headers.get('Authorization',  0))
        if json_obj.get('email', 0) and json_obj.get('password', 0):
            if valid_email(json_obj['email']) != 'OK':
                return jsonify({'success': valid_email(json_obj['email'])})
            if valid_password(json_obj['password']) != 'OK':
                return jsonify({'success': valid_password(json_obj['password'])})
            new_user = users.User(email=json_obj['email'], password=json_obj['password'])
            session.add(new_user)
            session.commit()
            return jsonify({'success': 'OK'})
        else:
            return jsonify({'success': 'no email or password'})
    except Exception as err:
        print(err)
        return jsonify({'success': 'ERROR'})


@app.route('/api/edit_user_profile', methods=['POST'])
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



