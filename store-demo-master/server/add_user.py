from main_server import app
from data import db_session
from data import users
import json
from flask import jsonify, request


@app.route('/adding_user', method=['POST'])
def adding_user():
    try:
        session = db_session.create_session()
        json_obj = request.get_json() or {}
        if json_obj.get('email', 0) and json_obj('password', 0):
            new_user = users.User(email=json_obj['email'], password=json_obj['password'])
            session.add(new_user)
            session.commit()
            return jsonify({'success': 'OK'})
        else:
            return jsonify({'success': 'no email or password'})
    except:
        return jsonify({'success': 'ERROR'})


@app.route('/edit_user_profile/<int:id_user>', method=['POST'])
def add_profile(id_user):
    session = db_session.create_session()
    json_obj = request.get_json() or {}
    user = session.query(User)



