from flask import Flask
from flask_restful import Api
from ressources.book_ressource import BookResource
from models.db import db
from schemas.schemas import ma
from blueprints.books_bp import books_bp

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
ma.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()


api.add_resource(BookResource, '/books', '/books/<int:book_id>')


app.register_blueprint(books_bp, url_prefix='/books')

if __name__ == "__main__":
    app.run(debug=True)