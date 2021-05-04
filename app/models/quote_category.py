from . import db, ma
from .mixins import OutputMixin

class QuoteCategory(OutputMixin, db.Model):
    """ Category of a quote """

    __tablename__ = "quote_category"

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    acronym = db.Column(db.String(64), nullable=False, unique=True)
    
    def __repr__(self):
        return '<QuoteCategory id={}, description={}, acronym={} >'.format(self.id, self.description, self.acronym)

class QuoteCategorySchema(ma.Schema):
    class Meta:
        model = QuoteCategory