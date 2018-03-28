from resources.quotes import QuotesResource, QuoteResource
from resources.quote_categories import QuoteCategoriesResource
from resources.random_quotes import RandomQuoteResource

def register(api):
    """ register resources in the api """

    QuoteResource.register(api)
    QuotesResource.register(api)
    
    RandomQuoteResource.register(api)
    
    QuoteCategoriesResource.register(api)
