from flask import redirect


def init_routes(app):
    @app.route('/')
    def index():
        return redirect('login')


