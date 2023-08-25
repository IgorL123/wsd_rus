from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user
from ..models import db, Request

home = Blueprint('home', __name__)
login_manager = LoginManager()
login_manager.init_app(home)


@home.route('/home', methods=['GET'])
@login_required
def show():
    requests = db.session.execute(db.select(Request).filter(Request.id_user == current_user.id)).scalars()
    tmp = ["Embeddings method", "Cluster analysis", "Bert"]
    return render_template('home.html', data=requests, models=tmp)
