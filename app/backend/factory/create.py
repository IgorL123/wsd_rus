from flask import Flask
from ..routes import login, logout, register, home, prompt, init_routes, rating
from flask_login import LoginManager
from ..models import Users
from ..core import load_vectors


def create_app(test_config=None):

    app = Flask(__name__,
                template_folder='../../templates',
                static_folder='../../static')
    app.config.from_object("backend.factory.config.Config")
    init_routes(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    app.register_blueprint(login)
    app.register_blueprint(logout)
    app.register_blueprint(register)
    app.register_blueprint(home)
    app.register_blueprint(prompt)
    app.register_blueprint(rating)
    app.app_context().push()

    load_vectors()

    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    return app
