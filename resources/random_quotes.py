from flask_restful import Resource, Api, reqparse, fields, abort
from flask import jsonify, Response

from models.quote import Quote
import app
import random

class RandomQuoteResource(Resource):

    def get(self, categ_acc):
        qtde = Quote.query.filter(Quote.category.has(acronym=categ_acc)).count()
        q = None
        
        if qtde == 0:
            return "desculpe, mas a princesa está em outro castelo - toad"
        elif qtde == 1:
            q = Quote.query.first()
        else:    
            randomPos = random.randrange(0, qtde)
            q = Quote.query.order_by('id').offset(randomPos).limit(1).first()

        return '{} - {}'.format(q.description,q.author)

    @staticmethod
    def register(api):
        api.add_resource(RandomQuoteResource, '/random_quotes/<string:categ_acc>')   