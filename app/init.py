from flask import Flask

from routes import init_routes


def create_app(test_config=None):

    app = Flask(__name__)

    app.config["SECRET_KEY"] = "some_dev_key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://user:12345@pgsql:5432/postgres_wsd"

    init_routes(app)

    return app
