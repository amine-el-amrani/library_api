from flask import Blueprint
from flask_restful import Api
from resources.book_resource import BookResource

# Créer le Blueprint pour les livres
books_bp = Blueprint('books', __name__)
api = Api(books_bp)

# Ajouter les routes pour les livres
api.add_resource(BookResource, '', '/<int:book_id>')
