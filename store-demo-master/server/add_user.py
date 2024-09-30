from data import db_session
from data import users
from flask import jsonify, request, Blueprint
from validations import valid_password, valid_email
from werkzeug.security import generate_password_hash
from uuid import uuid4

blueprint_add_user = Blueprint('blueprint_add_user', __name__)


@blueprint_add_user.route('/api/add_user', methods=['POST'])
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
                session.close()
                return jsonify({'success': 'OK'})
            else:
                session.close()
                return jsonify({'success': 'Email уже зарегистрирован'}), 202
        else:
            session.close()
            return jsonify({'success': 'Неверный Email или пароль'})
    except Exception as err:
        print(err)

        return jsonify({'success': 'ERROR'}), 500








