from flask_restful import Api

from resources.quotes import QuotesResource, QuoteResource
from resources.quote_categories import QuoteCategoriesResource
from resources.random_quotes import RandomQuoteResource

def register(app):
    """ register resources in the api """

    api = Api(app)

    QuoteResource.register(api)
    QuotesResource.register(api)
    RandomQuoteResource.register(api)
    QuoteCategoriesResource.register(api)