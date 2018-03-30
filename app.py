from flask import Flask, render_template
from flask_restful import Api

from models import create_db_for_app
from utils import CustomJSONEncoder

import resources

#Flask app
__app = Flask(__name__)
__app.json_encoder = CustomJSONEncoder
__app.config.from_json('./appsettings.json', silent=False)

@__app.route('/index.html')
def index():
    return __app.send_static_file('index.html')

#Database config
__db = create_db_for_app(__app, createTables=True)

#API and resources
api = Api(__app)
resources.register(api)

def get_db():
    """ get a reference to global app db """
    return __db