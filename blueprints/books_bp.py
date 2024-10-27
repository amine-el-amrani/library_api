from flask import Blueprint
from flask_restx import Api, Namespace
from resources.book_resource import BookListResource, BookResource

books_bp = Blueprint('books', __name__)
api = Api(books_bp)

# Créer le namespace pour les livres
books_ns = Namespace('books', description="Operations related to books")

# Ajouter les ressources au namespace
books_ns.add_resource(BookListResource, '/')
books_ns.add_resource(BookResource, '/<int:book_id>')

# Ajouter le namespace à l'API du Blueprint
api.add_namespace(books_ns)