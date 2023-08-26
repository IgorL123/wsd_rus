from flask import request, Blueprint, redirect, url_for
from flask_login import LoginManager, login_required, current_user
from ..models import db, Request
import datetime
from ..core import main

prompt = Blueprint('prompt', __name__)
login_manager = LoginManager()
login_manager.init_app(prompt)


@prompt.route('/prompt', methods=['GET', 'POST'])
@login_required
def show():
    res = "error"
    if request.method == 'POST':
        text = request.json['text']
        word = request.json['word']

        if text.find(word) != 1:
            print(1, flush=True)

        new_req = Request(
            text=text,
            word=word,
            date=datetime.datetime.today(),
            id_user=current_user.id
        )
        db.session.add(new_req)
        db.session.commit()

        res = main()
    if request.method == 'GET':
        pass

    return res
