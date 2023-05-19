from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import LoginManager, login_user
from models import Users, db
import hash

login = Blueprint('login', __name__, template_folder='../templates')
login_manager = LoginManager()
login_manager.init_app(login)


@login.route('/login', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']

        user = Users.query.filter_by(email=email).first()
        if user:
            if hash.check_password_hash(user.password_hash, password):
                login_user(user)
                return redirect(url_for('home.show', username=email))
            else:
                return redirect(url_for('login.show') + '?error=incorrect-password')
        else:
            return redirect(url_for('login.show') + '?error=user-not-found')
    else:
        return render_template('login.html')
