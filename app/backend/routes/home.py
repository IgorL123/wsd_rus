from flask import Blueprint, render_template
from flask_login import LoginManager, login_required


home = Blueprint('home', __name__)
login_manager = LoginManager()
login_manager.init_app(home)


@home.route('/home', methods=['GET'])
@login_required
def show():
    return render_template('home.html')
