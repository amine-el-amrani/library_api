from flask import Blueprint
from flask_restx import Api, Namespace
from resources.author_resource import AuthorListResource, AuthorResource

# Créer le Blueprint pour les auteurs
authors_bp = Blueprint('authors', __name__)
api = Api(authors_bp)

# Définir un Namespace pour les opérations sur les auteurs
authors_ns = Namespace('authors', description="Operations related to authors")

# Ajouter les ressources au Namespace
authors_ns.add_resource(AuthorListResource, '/')
authors_ns.add_resource(AuthorResource, '/<int:author_id>')

# Ajouter le Namespace à l'API du Blueprint
api.add_namespace(authors_ns)