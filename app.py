from flask import Flask
from flask_restful import Api

from resources.quotes import QuotesResource, QuoteResource
from model import create_db_for_app
from mixins import CustomJSONEncoder

__app = Flask(__name__)
__app.json_encoder = CustomJSONEncoder

__db = create_db_for_app(
    __app, sqliteConnString="sqlite:///quotes.db", createTables=True)


def get_db():
    """ get a reference to global app db """
    return __db


def run():
    """ run the flask app (development only) """

    api = Api(__app)
    api.add_resource(QuotesResource, '/quotes')
    api.add_resource(QuoteResource, '/quotes/<int:id>')

    __app.run(debug=True)
