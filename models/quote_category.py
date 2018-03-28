from . import _db
from .mixins import OutputMixin

class QuoteCategory(OutputMixin, _db.Model):
    """ Category of a quote """

    id = _db.Column(_db.Integer, primary_key=True)
    description = _db.Column(_db.String(255), nullable=False)
    accronym = _db.Column(_db.String(64), nullable=False)

    def __init__(self, id, description, accronym):
        self.id = id
        self.description = description
        self.accronym = accronym