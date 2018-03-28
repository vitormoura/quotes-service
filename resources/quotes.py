from flask_restful import Resource, Api, reqparse, fields
from model import Quote, QuoteCategory
from flask import jsonify
import app

class QuoteResource(Resource):
    
    def get(self, id):
        
        q = Quote.query.get(id)
        print(q.category)
        if q != None:

            return jsonify(q)
        else:
            return None

    def delete(self, id):
        q = Quote.query.get(id).first()

        if q == None:
            return None, 404
        
        db = app.get_db()
        db.session.delete(q)
        db.session.commit() 

        return "OK"


class QuotesResource(Resource):
        
    def get(self):
        return [jsonify(q) for q in Quote.query.all()]

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('author', help="quote author name", required=True)
        parser.add_argument('description', help="quote description", required=True)
        parser.add_argument('category_id', type=int, help="quote category id", required=True)
        args = parser.parse_args()
        
        q = Quote(description=args.description, category_id=args.category_id, author=args.author)

        db = app.get_db()
        db.session.add(q)
        db.session.commit()  

        return q.as_dict(), 201
