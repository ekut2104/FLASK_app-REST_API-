from flask import Flask

from week6.lesson2_Database_ORM.homework.DmytroMelnyk.service_api.api import user_api
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.service_api.app_database import db, ma
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.service_api.config import runtime_config
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.service_api.keyspaces.keyspaces import create_db_api
from week6.lesson2_Database_ORM.homework.DmytroMelnyk.service_api.one_to_many import one_to_many_api


def run_app():
    app = Flask(__name__)
    db.init_app(app)
    ma.init_app(app)
    app.config.from_object(runtime_config())
    app.register_blueprint(user_api)
    app.register_blueprint(create_db_api)
    app.register_blueprint(one_to_many_api)
    return app
