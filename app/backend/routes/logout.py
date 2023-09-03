from flask import Blueprint, url_for, redirect, current_app
from flask_login import LoginManager, login_required, logout_user, current_user

logout = Blueprint('logout', __name__)
login_manager = LoginManager()
login_manager.init_app(logout)


@logout.route('/logout')
@login_required
def show():
    current_app.logger.info(f"Logout user with id {current_user.id}")
    logout_user()
    return redirect(url_for('login.show') + '?success=logged-out')
