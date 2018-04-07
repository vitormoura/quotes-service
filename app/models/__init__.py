from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()

def register(app):

    if app is None:
        raise ValueError()

    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        db.create_all()
