from flask import Flask
from data import db_session
from flask_restful import Api
from flask import jsonify, request
from secret_keys import APP_CONFIG_SECRET_KEY
from add_user import blueprint_add_user
from login import blueprint_login
from get_searching_olimpiads import blueprint_get_searching_olimpiads
from edit_user_profile import blueprint_edit_user_profile
from get_one_olimp import blueprint_get_one_olimp
from token_required import token_required
from sqlalchemy import select
from data import users, subjects, olimp_subject, olimpics
from load_subjects import load_subjects
from load_olimpycs_db import new_olimpycs
import time


app = Flask(__name__)
app.register_blueprint(blueprint_login)
app.register_blueprint(blueprint_add_user)
app.register_blueprint(blueprint_edit_user_profile)
app.register_blueprint(blueprint_get_one_olimp)
app.register_blueprint(blueprint_get_searching_olimpiads)
api = (Api(app))
app.config['SECRET_KEY'] = APP_CONFIG_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/api/test', methods=['GET'])
@token_required
def test(current_user):
    return jsonify({'success': 'AAAAAAAA'})




if __name__ == "__main__":
    db_session.global_init("../db/main_database.db")
    #load_subjects()
    #new_olimpycs()

    app.run(host='127.0.0.1', port=8888)



