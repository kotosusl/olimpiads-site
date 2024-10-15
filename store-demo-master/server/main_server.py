from flask import Flask
from data import db_session
from flask_restful import Api
from secret_keys import APP_CONFIG_SECRET_KEY
from add_user import blueprint_add_user
from login import blueprint_login
from get_searching_olimpiads import blueprint_get_searching_olimpiads
from edit_user_profile import blueprint_edit_user_profile
from get_one_olimp import blueprint_get_one_olimp
from load_subjects import load_subjects
from load_olimpycs_db import new_olimpycs
import schedule
from add_olimp_to_user import blueprint_add_olimp_to_user
from get_notifications import blueprint_get_notifications
from checker_dates_olimps import checker_dates_olimps
from remove_olimp_user import blueprint_remove_olimp_user
from get_profile_info import blueprint_get_profile_info
from get_user_olimps import blueprint_get_user_olimps
from check_telegram_name import blueprint_check_telegram_name


app = Flask(__name__)
app.register_blueprint(blueprint_login)
app.register_blueprint(blueprint_add_user)
app.register_blueprint(blueprint_edit_user_profile)
app.register_blueprint(blueprint_get_one_olimp)
app.register_blueprint(blueprint_get_searching_olimpiads)
app.register_blueprint(blueprint_add_olimp_to_user)
app.register_blueprint(blueprint_get_notifications)
app.register_blueprint(blueprint_remove_olimp_user)
app.register_blueprint(blueprint_get_profile_info)
app.register_blueprint(blueprint_get_user_olimps)
app.register_blueprint(blueprint_check_telegram_name)
api = (Api(app))
app.config['SECRET_KEY'] = APP_CONFIG_SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

def send_notifications_in_telegram_bot():
    users_of_sending = checker_dates_olimps()
    for user_telegram_id, user_msg in users_of_sending:
        print(user_telegram_id, user_msg)


if __name__ == "__main__":
    db_session.global_init("../db/main_database_beta.db")
    #load_subjects()
    #new_olimpycs()
    schedule.every(30).days.at('12:00').do(checker_dates_olimps)

    app.run(host='127.0.0.1', port=8888)



