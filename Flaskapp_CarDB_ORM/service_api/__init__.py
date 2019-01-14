from flask import Flask

from Flaskapp_CarDB_ORM.service_api import user_api
from Flaskapp_CarDB_ORM.service_api import db, ma
from Flaskapp_CarDB_ORM.service_api import runtime_config
from Flaskapp_CarDB_ORM.service_api import create_db_api
from Flaskapp_CarDB_ORM.service_api import one_to_many_api


def run_app():
    app = Flask(__name__)
    db.init_app(app)
    ma.init_app(app)
    app.config.from_object(runtime_config())
    app.register_blueprint(user_api)
    app.register_blueprint(create_db_api)
    app.register_blueprint(one_to_many_api)
    return app
