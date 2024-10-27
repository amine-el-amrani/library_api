from flask import Flask
from models.db import db
from flask_restx import Api
from schemas.schemas import ma
from blueprints.books_bp import books_bp, books_ns
from blueprints.authors_bp import authors_bp, authors_ns

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)
ma.init_app(app)

api = Api(app, version="1.0", title="Library API", description="Documentation automatique de l'API", doc="/docs")

api.add_namespace(books_ns, path='/books')
api.add_namespace(authors_ns, path='/authors')

app.register_blueprint(books_bp, url_prefix='/books')
app.register_blueprint(authors_bp, url_prefix='/authors')

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)