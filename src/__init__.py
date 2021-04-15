import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        FLASK_APP = "src",
        SECRET_KEY = "secret-key-goes-here",
        SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite",
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        PROPAGATE_EXCEPTIONS = True
    )

    db.init_app(app)

    """try:
        os.makedirs(app.instance_path)
    except OSError:
        pass"""

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
