# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse, fields, abort
from flask import jsonify, Response
from ..utils import request_wants_json

from ..models.quote import Quote
import random

class RandomQuoteResource(Resource):

    @staticmethod
    def register(api):
        api.add_resource(RandomQuoteResource, '/random_quotes/<string:categ_acc>')   

    def get(self, categ_acc):
        qtde = Quote.query.filter(Quote.category.has(acronym=categ_acc)).count()
        q = None
        
        if qtde == 0:
            return Response("desculpe, mas a princesa está em outro castelo - toad", mimetype="text/plain")
        elif qtde == 1:
            q = Quote.query.filter(Quote.category.has(acronym=categ_acc)).first()
        else:    
            random_pos = random.randrange(0, stop=qtde)
            q = Quote.query.filter(Quote.category.has(acronym=categ_acc)).order_by('id').offset(random_pos).first()

        if q is None:
            abort(500, 'internal error')

        if request_wants_json():
            return jsonify(q)
        else:
            return Response('{} - {}'.format(q.description, q.author), mimetype="text/plain")