from . import db, ma
from .mixins import OutputMixin

class QuoteCategory(OutputMixin, db.Model):
    """ Category of a quote """

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    acronym = db.Column(db.String(64), nullable=False, unique=True)

    def __init__(self, id, description, acronym):
        self.id = id
        self.description = description
        self.acronym = acronym

class QuoteCategorySchema(ma.ModelSchema):
    class Meta:
        model = QuoteCategory