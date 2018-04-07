from flask_restful import Resource, Api, reqparse, fields, abort
from flask import jsonify, Response, request, app
from marshmallow import ValidationError

from ..models import db
from ..models.quote import Quote, QuoteSchema
from ..models.quote_category import QuoteCategory


class QuoteResource(Resource):

    @staticmethod
    def register(api):
        api.add_resource(QuoteResource, '/quotes/<int:id>')

    def get(self, id):
        q = Quote.query.get_or_404(id)
        
        return jsonify(q)

    def delete(self, id):
        q = Quote.query.get(id)

        if q is None:
            return Response(status=200)
        
        db.session.delete(q)
        db.session.commit()

        return Response(status=200)  


class QuotesResource(Resource):

    @staticmethod
    def register(api):
        api.add_resource(QuotesResource, '/quotes/<string:categ_acc>')

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'author', help="quote author name", required=True)
        self.parser.add_argument(
            'description', help="quote description", required=True)
        self.parser.add_argument(
            'category_id', type=int, help="quote category id", required=True)

    def get(self, categ_acc):
        result = Quote.query.filter(Quote.category.has(acronym=categ_acc)).all()
        return jsonify(result)

    def post(self, categ_acc):

        categ = QuoteCategory.query.filter_by(acronym=categ_acc).first()

        if categ == None:
            abort(400, message='quote category {} not found'.format(categ_acc))

        args = self.parser.parse_args()

        if len(args.description) == 0 or len(args.author) == 0:
            abort(400, message='invalid quote description or author name')

        q = Quote(description=args.description,
                  category_id=categ.id, author=args.author)

        db.session.add(q)
        db.session.commit()

        return jsonify(q)    
