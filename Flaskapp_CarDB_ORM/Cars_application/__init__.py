from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from Flaskapp_CarDB_ORM.Cars_application.config import run_config

from Flaskapp_CarDB_ORM.Cars_application.db.app_database import db, ma

bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
login_manager.session_protection = "strong"


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from Flaskapp_CarDB_ORM.Cars_application.keyspaces.keyspaces import create_db
    from Flaskapp_CarDB_ORM.Cars_application.main.views import main
    from Flaskapp_CarDB_ORM.Cars_application.users.views import users
    from Flaskapp_CarDB_ORM.Cars_application.cars.views import cars
    from Flaskapp_CarDB_ORM.Cars_application.errors.handlers import errors
    from Flaskapp_CarDB_ORM.Cars_application.api.views import car_api

    app.register_blueprint(create_db)
    app.register_blueprint(main)
    app.register_blueprint(users)
    app.register_blueprint(cars)
    app.register_blueprint(errors)
    app.register_blueprint(car_api)

    return app
