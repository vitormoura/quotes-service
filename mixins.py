from uuid import UUID
from sqlalchemy.ext.declarative import DeclarativeMeta
from flask.json import JSONEncoder
import json

class CustomJSONEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            return obj.to_dict()
            
        return super(CustomJSONEncoder, self).default(obj)

class OutputMixin(object):
    
    RELATIONSHIPS_TO_DICT = False

    def __iter__(self):
        return self.to_dict().iteritems()

    def to_dict(self, rel=None, backref=None, exclude=()):
        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT

        res = {column.key: getattr(self, attr)
            for attr, column in self.__mapper__.c.items()
            if column.key not in exclude}

        if rel:
            for attr, relation in self.__mapper__.relationships.items():
                # Avoid recursive loop between to tables.
                if backref == relation.table:
                    continue
                value = getattr(self, attr)
                if value is None:
                    res[relation.key] = None
                elif isinstance(value.__class__, DeclarativeMeta):
                    res[relation.key] = value.to_dict(backref=self.__table__)
                else:
                    res[relation.key] = [i.to_dict(backref=self.__table__)
                                        for i in value]
        return res


    def to_json(self, rel=None, exclude=None):
        def extended_encoder(x):
            if isinstance(x, datetime):
                return x.isoformat()
            if isinstance(x, UUID):
                return str(x)

        if rel is None:
            rel = self.RELATIONSHIPS_TO_DICT
            
        return json.dumps(self.to_dict(rel, exclude=exclude),
                        default=extended_encoder)