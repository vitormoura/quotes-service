from os import getcwd
from flask import Flask, render_template
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

db.create_all()

#admin = User(username='admin', email='admin@example.com')
#guest = User(username='guest', email='guest@example.com')
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()

api = Api(app)

@app.route('/daniel')
def hello():
    usr = User.query.find(1)
    return render_template('daniel.html', usuario=usr)


class HelloWorld(Resource):
    def get(self):
        return [u.as_dict() for u in User.query.all()]


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
