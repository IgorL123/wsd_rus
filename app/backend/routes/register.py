from flask import render_template, request, redirect, url_for, Blueprint
from flask_login import LoginManager
from ..models import Users, db
from .hash import create_hash

register = Blueprint('register', __name__, template_folder='/home/igor/projects/PycharmProjects/wsd/app/templates')
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
                    return redirect(url_for('register.show') + '?error=user-or-email-exists')
                else:
                    db.session.add(new_user)
                    db.session.commit()

            except db.exc.IntegrityError:
                return redirect(url_for('register.show') + '?error=exception')

            return redirect(url_for('login.show') + '?success=account-created')
        else:
            return redirect(url_for('register.show') + '?error=missing-fields')
    else:
        return render_template('register.html')