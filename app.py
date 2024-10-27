from flask import Flask
from flask_restful import Api
from resources.book_resource import BookResource
from resources.author_resource import AuthorResource
from models.db import db
from schemas.schemas import ma
from blueprints.books_bp import books_bp
from blueprints.authors_bp import authors_bp

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
ma.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(authors_bp, url_prefix='/authors')

if __name__ == "__main__":
    app.run(debug=True)