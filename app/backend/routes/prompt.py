from flask import request, Blueprint, redirect, url_for, make_response, flash
from flask_login import LoginManager, login_required, current_user
from ..models import db, Request, Response
from ..core import main

prompt = Blueprint('prompt', __name__)
login_manager = LoginManager()
login_manager.init_app(prompt)


@prompt.route('/prompt', methods=['GET', 'POST'])
@login_required
def show():
    res = "error"
    word = "error"
    if request.method == 'POST':
        text = request.form['text']
        word = request.form['word']

        if text.find(word) == -1:
            flash("В предложении нет такого слова!", "error")
            return redirect(url_for("home.show"))

        new_req = Request(
            text=text,
            word=word,
            id_user=current_user.id
        )
        db.session.add(new_req)
        db.session.commit()

        res = main()

        new_res = Response(
            text=res,
            grade=0,
            id_request=new_req.id
        )
        db.session.add(new_res)
        db.session.commit()

    if request.method == 'GET':
        pass

    resp = make_response(redirect(url_for("home.show", result=res, word=word)))
    return resp
