from flask import Blueprint, render_template
from flask_login import LoginManager, login_required, current_user
from ..models import db, Request, Response

history = Blueprint('history', __name__)
login_manager = LoginManager()
login_manager.init_app(history)


@history.route('/history', methods=['GET'])
@login_required
def show():

    requests = db.session.execute(db.select(Request, Response.text.label("meaning")) \
                                  .join(Response) \
                                  .order_by(Request.date.desc()) \
                                  .filter(Request.id_user == current_user.id)).scalars()

    return render_template('history.html', data=requests)
