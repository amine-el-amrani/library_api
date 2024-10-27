from flask import Flask
from models.book import Book
from models.author import Author
from models.book import db
from blueprints.books_bp import books_bp

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(books_bp, url_prefix='/books')

if __name__ == "__main__":
    app.run(debug=True)