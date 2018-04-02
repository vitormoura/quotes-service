from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import app

db = SQLAlchemy(app.myapp)
ma = Marshmallow(app.myapp)

def create_tables():
    with app.myapp.app_context():
        db.create_all()   