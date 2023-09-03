from flask import redirect, current_app


def init_routes(app):
    @app.route('/')
    def index():
        current_app.logger.info("Default route user")
        return redirect('login')
