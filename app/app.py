from flask_migrate import Migrate
from backend.factory import create_app
from backend.models import db
import sys
sys.path.append("..")


app = create_app()
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == "__main__":
    app.run()
