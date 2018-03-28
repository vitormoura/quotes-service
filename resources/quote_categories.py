from flask_restful import Resource, Api, reqparse, fields
from flask import jsonify

from models.quote_category import QuoteCategory
import app

class QuoteCategoriesResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('id', type=int, help="category id", required=True)
        self.parser.add_argument('description', help="category description", required=True)
        self.parser.add_argument('accronym', help="category accronym", required=True)

    def get(self):
        return jsonify(QuoteCategory.query.all())
    
    def post(self):
        args = self.parser.parse_args()

        c = QuoteCategory(args['id'],args['description'], args['accronym'])

        db = app.get_db()
        db.session.add(c)
        db.session.commit()  

        return jsonify(c)

    @staticmethod
    def register(api):
        api.add_resource(QuoteCategoriesResource, '/quotes/categories')