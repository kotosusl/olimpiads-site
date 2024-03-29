from flask import Flask
from data import db_session
from load_olimpycs_db import new_olimpycs
from load_subjects import load_subjects
from flask_restful import reqparse, abort, Api, Resource


app = Flask(__name__)
api = Api(app)
if __name__ == "__main__":
    db_session.global_init("../db/main_database.db")
    load_subjects()
    new_olimpycs()
    app.run(host='127.0.0.1', port=8888)



