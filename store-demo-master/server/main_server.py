import flask
from data import db_session
from load_olimpycs_db import new_olimpycs
from load_subjects import load_subjects


app = flask.Flask(__name__)
if __name__ == "__main__":
    db_session.global_init("../db/main_database.db")
    load_subjects()
    new_olimpycs()
    app.run(host='127.0.0.1', port=8888)



