from flask.json import JSONEncoder
from flask import request
from sqlalchemy.ext.declarative import DeclarativeMeta


class CustomJSONEncoder(JSONEncoder):
    """ JSON Encoder with support to sqlalchemy objects"""

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            return obj.to_dict()

        return super(CustomJSONEncoder, self).default(obj)


def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/plain'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/plain']
