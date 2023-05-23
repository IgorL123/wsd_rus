from flask import request, Blueprint, redirect, url_for
from flask_login import LoginManager, login_required, current_user
from ..models import db, Request
import datetime
import flask


prompt = Blueprint('prompt', __name__)
login_manager = LoginManager()
login_manager.init_app(prompt)


@prompt.route('/prompt', methods=['GET', 'POST'])
@login_required
def show():
    if request.method == 'POST':
        text = request.form['prompt']
        word = request.form['word']

        new_req = Request(
            text=text,
            word=word,
            date=datetime.datetime.today(),
            id_user=current_user.id
        )
        db.session.add(new_req)
        db.session.commit()
        flask.flash("Success")
    return redirect(url_for('home.show'))
