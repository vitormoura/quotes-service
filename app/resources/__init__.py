from flask_restful import Api

from .quotes import QuotesResource, QuoteResource
from .quote_categories import QuoteCategoriesResource
from .random_quotes import RandomQuoteResource

def register(app):
    """ register resources in the api """

    api = Api(app)

    QuoteResource.register(api)
    QuotesResource.register(api)
    RandomQuoteResource.register(api)
    QuoteCategoriesResource.register(api)