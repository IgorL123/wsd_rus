from flask import request, Blueprint, redirect, url_for, make_response, flash, current_app
from flask_login import LoginManager, login_required, current_user
from ..models import db, Request, Response
from ..core import main

prompt = Blueprint('prompt', __name__)
login_manager = LoginManager()
login_manager.init_app(prompt)


@prompt.route('/prompt', methods=['GET', 'POST'])
@login_required
def show():

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
        current_app.logger.info(f"New prompt from user with id {current_user.id}")

        current_app.logger.info("Embeddings call")
        res, score = main(text, word)
        current_app.logger.info("Embeddings end call")

        new_res = Response(
            text=res,
            grade=0,
            id_request=new_req.id,
            model_type=current_app.config["MODEL"],
            score=round(100 * score, 2)
        )
        db.session.add(new_res)
        db.session.commit()

        result = {
            "result": res,
            "word": word,
            "score": round(100 * score, 2),
            "id_response": str(new_res.id)
        }

        score = round(100 * score, 2)
        id_response = str(new_res.id)

        return make_response(redirect(url_for("home.show", result=res,
                                              word=word, score=score, id_response=id_response
                                              )))

    if request.method == 'GET':
        return redirect(url_for("/home.show"))
