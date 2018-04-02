from flask import Flask, render_template
from flask_restful import Api
from utils import CustomJSONEncoder

#Flask app
myapp = Flask(__name__)
myapp.json_encoder = CustomJSONEncoder
myapp.config.from_json('./appsettings.json', silent=False)

@myapp.route('/index.html')
def index():
    return myapp.send_static_file('index.html')

import models
import resources

#Database
models.create_tables()

#API and resources
resources.register(myapp)