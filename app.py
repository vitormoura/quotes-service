from flask import Flask
from flask_restful import Api

from models import create_db_for_app
from utils import CustomJSONEncoder

import resources

#Flask app
__app = Flask(__name__)
__app.json_encoder = CustomJSONEncoder
__app.config.from_json('./appsettings.json', silent=False)

#Database config
__db = create_db_for_app(__app, createTables=True)


def get_db():
    """ get a reference to global app db """
    return __db


def run():
    """ run the flask app (development only) """

    api = Api(__app)
    resources.register(api)
        
    __app.run(debug=True)
