from . import _db
from .mixins import OutputMixin
from .quote_category import QuoteCategory


class Quote(OutputMixin, _db.Model):
    """Quote"""

    RELATIONSHIPS_TO_DICT = True

    id = _db.Column(_db.Integer, primary_key=True, autoincrement=True)
    author = _db.Column(_db.String(255), nullable=False)
    description = _db.Column(_db.String(2048), nullable=False)
    category = _db.relationship(QuoteCategory, lazy=True)
    category_id = _db.Column(_db.Integer, _db.ForeignKey(
        'quote_category.id'), nullable=False)

    def __init__(self, author, description, category_id):
        self.author = author
        self.description = description
        self.category_id = category_id
