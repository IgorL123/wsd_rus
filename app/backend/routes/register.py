from flask import request, redirect, url_for, Blueprint, render_template, current_app
from flask_login import LoginManager, login_user
from ..models import Users, db
from .hash import create_hash

register = Blueprint('register', __name__, template_folder="../../templates")
login_manager = LoginManager()
login_manager.init_app(register)


@register.route('/register', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if email and password:
            password_hash = create_hash(password)

            try:
                new_user = Users(
                        email=email,
                        password=password_hash,
                    )
                user = Users.query.filter_by(email=email).first()
                if user:
                    current_app.logger.info("Register attempt with invalid email")
                    return redirect(url_for('register.show') + '?error=user-or-email-exists')
                else:
                    db.session.add(new_user)
                    db.session.commit()
                    login_user(new_user)
                    next = request.args.get('next')
                    current_app.logger.info("Register successful attempt")

            except db.exc.IntegrityError:
                current_app.logger.info("Register attempt with some exception")
                return redirect(url_for('register.show') + '?error=exception')

            return redirect(next or url_for('home.show'))
        else:
            current_app.logger.info("Register attempt with missing fields")
            return redirect(url_for('register.show') + '?error=missing-fields')
    else:
        return render_template('register.html')
