from flask_sqlalchemy import SQLAlchemy
from mixins import OutputMixin

_db = SQLAlchemy()

class Quote(OutputMixin, _db.Model):
    """Quote"""

    RELATIONSHIPS_TO_DICT = True

    id = _db.Column(_db.Integer, primary_key=True, autoincrement=True)
    author = _db.Column(_db.String(255), nullable=False)
    description = _db.Column(_db.String(2048), nullable=False)
    category = _db.relationship("QuoteCategory", lazy=True)
    category_id = _db.Column(_db.Integer, _db.ForeignKey(
        'quote_category.id'), nullable=False)

    def __init__(self, author, description, category_id):
        self.author = author
        self.description = description
        self.category_id = category_id

    def to_dict(self):
        return super(Quote, self).to_dict(exclude=['category_id','id'])


class QuoteCategory(OutputMixin, _db.Model):
    """ Category of a quote """
    id = _db.Column(_db.Integer, primary_key=True)
    description = _db.Column(_db.String(255), nullable=False)


def create_db_for_app(app, sqliteConnString, createTables=False):
    """Create and register a new SqlAlchemy db object to a Flask app"""

    app.config['SQLALCHEMY_DATABASE_URI'] = sqliteConnString
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    _db.init_app(app)

    if createTables:
        with app.app_context():
            _db.create_all()

    return _db
