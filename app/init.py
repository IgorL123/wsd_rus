from flask import Flask
import os
from routes import init_routes


def create_app(test_config=None):

    app = Flask(__name__)
    app.config.from_object("config.Config")
    init_routes(app)

    return app
