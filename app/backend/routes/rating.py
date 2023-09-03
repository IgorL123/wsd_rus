from flask import request, Blueprint, redirect, url_for, current_app
from flask_login import LoginManager, login_required
from ..models import db, Response

rating = Blueprint('rating', __name__)
login_manager = LoginManager()
login_manager.init_app(rating)


@rating.route('/rate', methods=['GET'])
@login_required
def change():
    id_response = request.args["id_response"]
    response = db.session.query(Response).filter_by(id=id_response).first()
    if response:
        response.grade = 1
        db.session.commit()

    current_app.logger.info("New rating committed")
    return redirect(url_for("home.show"))
