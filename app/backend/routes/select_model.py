from flask import request, Blueprint, redirect, url_for, current_app
from flask_login import LoginManager, login_required
from ..core import load_vectors

select = Blueprint('select', __name__)
login_manager = LoginManager()
login_manager.init_app(select)


@select.route('/select/model', methods=['POST'])
@login_required
def change():
    model_type = request.json["model_type"]
    current_app.config["MODEL"] = model_type
    # too slow
    load_vectors()

    return redirect(url_for("home.show"))
