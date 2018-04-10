import os

from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS

from .utils import CustomJSONEncoder
from .resources import register as register_resources_of
from .models import register as register_model_of


def create_app(config_opts):

    if config_opts is None:
        raise ValueError('Invalid config_opts: None')

    # Flask app
    myapp = Flask(__name__)
    myapp.json_encoder = CustomJSONEncoder

    CORS(myapp)

    if isinstance(config_opts, str):

        if not os.path.isfile(config_opts):
            raise FileNotFoundError(
                'Config file not found: {}'.format(config_opts))

        if not config_opts.lower().endswith('.json'):
            raise ValueError(
                'Invalid json config file: {}'.format(config_opts))

        myapp.config.from_json(config_opts)

    elif isinstance(config_opts, dict):
        myapp.config.from_object(config_opts)
    else:
        raise ValueError('Invalid configuration object')

    # Routes
    @myapp.route('/index.html')
    def index():
        return myapp.send_static_file('index.html')

    # Model
    register_model_of(myapp)

    #API and resources
    register_resources_of(myapp)

    return myapp
