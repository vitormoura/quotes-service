from flask_restful import Resource, Api, reqparse, fields, abort
from flask import jsonify, Response

from models.quote import Quote
from models.quote_category import QuoteCategory
import app

class QuoteResource(Resource):
        
    def get(self, id):
        q = Quote.query.get(id)
        
        if q != None:
            return jsonify(q)
        else:
            abort(404, message='quote {} not found'.format(id))

    def delete(self, id):
        q = Quote.query.get(id)

        if q == None:
            abort(404, message='quote {} not found'.format(id))
        
        db = app.get_db()
        db.session.delete(q)
        db.session.commit() 

        return Response(200)  

    @staticmethod
    def register(api):
        api.add_resource(QuoteResource, '/quotes/<int:id>')

class QuotesResource(Resource):
        
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('author', help="quote author name", required=True)
        self.parser.add_argument('description', help="quote description", required=True)
        self.parser.add_argument('category_id', type=int, help="quote category id", required=True)
            
    def get(self, categ_acc):
        return jsonify(Quote.query.filter(Quote.category.has(acronym=categ_acc)).all())

    def post(self, categ_acc):
        args = self.parser.parse_args()
        
        categ = QuoteCategory.query.filter_by(acronym=categ_acc).first()

        if categ == None:
            abort(400, message='quote category {} not found'.format(categ_acc))

        q = Quote(description=args.description, category_id=categ.id, author=args.author)

        db = app.get_db()
        db.session.add(q)
        db.session.commit()  

        return jsonify(q)

    @staticmethod
    def register(api):
        api.add_resource(QuotesResource, '/quotes/<string:categ_acc>')   
