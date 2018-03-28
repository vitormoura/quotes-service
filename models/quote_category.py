from . import db
from .mixins import OutputMixin

class QuoteCategory(OutputMixin, db.Model):
    """ Category of a quote """

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    accronym = db.Column(db.String(64), nullable=False)

    def __init__(self, id, description, accronym):
        self.id = id
        self.description = description
        self.accronym = accronym