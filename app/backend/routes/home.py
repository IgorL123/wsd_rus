from flask import Blueprint, render_template, request
from flask_login import LoginManager, login_required, current_user
from ..models import db, Request

home = Blueprint('home', __name__)
login_manager = LoginManager()
login_manager.init_app(home)


@home.route('/home', methods=['GET'])
@login_required
def show():
    res = request.args.get('result')
    requests = db.session.execute(db.select(Request) \
                                  .order_by(Request.date.desc()) \
                                  .filter(Request.id_user == current_user.id)).scalars()
    tmp = ["Bert", "LLM", "Clusterisation", "Embeddings"]
    return render_template('home_b.html', data=requests, models=tmp, result=res)
