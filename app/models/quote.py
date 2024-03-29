from . import db, ma
from .mixins import OutputMixin
from .quote_category import QuoteCategory


class Quote(OutputMixin, db.Model):
    """Quote"""

    RELATIONSHIPS_TO_DICT = True

    __tablename__ = "quote"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(2048), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('quote_category.id'), nullable=False)
    category = db.relationship(QuoteCategory, lazy=True)

    def __repr__(self):
        return '<Quote id={}, description={}, category_id={}, author={} >'.format(self.id, self.description, self.category_id, self.author)

class QuoteSchema(ma.Schema):
    class Meta:
        model = Quote
