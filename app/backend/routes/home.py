from flask import Blueprint, render_template, request, current_app
from flask_login import LoginManager, login_required

home = Blueprint('home', __name__)
login_manager = LoginManager()
login_manager.init_app(home)


@home.route('/home', methods=['GET'])
@login_required
def show():
    res = request.args.get('result')
    word = request.args.get('word')
    score = request.args.get('score')
    id_response = request.args.get('id_response')

    tmp = ["tinyBert", "LaBSE", "Lamma", "FastText"]
    return render_template('home_b.html', models=tmp, result=res,
                           word=word, score=score, id_response=id_response,
                           model_type=current_app.config["MODEL"])
