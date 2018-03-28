from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_db_for_app(app, createTables=False):
    """Create and register a new SqlAlchemy db object to a Flask app"""
    
    db.init_app(app)

    if createTables:
        with app.app_context():
            db.create_all()

    return db