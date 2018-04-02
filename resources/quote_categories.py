from flask_restful import Resource, Api, reqparse, fields, abort
from flask import jsonify
from sqlalchemy import or_

from models import db
from models.quote_category import QuoteCategory, QuoteCategorySchema


class QuoteCategoriesResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'id', type=int, help="category id", required=True)
        self.parser.add_argument(
            'description', help="category description", required=True)
        self.parser.add_argument(
            'acronym', help="category acronym", required=True)

    def get(self):
        return jsonify(QuoteCategory.query.all())

    def post(self):
        args = self.parser.parse_args()

        if len(args.description) == 0 or len(args.acronym) == 0:
            abort(400, message='invalid category description or acronym')

        existing_categ = QuoteCategory.query.filter(
            or_(QuoteCategory.acronym == args.acronym, QuoteCategory.id == args.id)).first()

        if existing_categ is not None:
            abort(400, message='category already exists')

        c = QuoteCategory(id=args.id, description=args.description, acronym=args.acronym)

        db.session.add(c)
        db.session.commit()

        return jsonify(c)

    @staticmethod
    def register(api):
        api.add_resource(QuoteCategoriesResource, '/quotes/categories')
