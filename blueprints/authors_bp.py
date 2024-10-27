from flask import Blueprint
from flask_restful import Api
from resources.author_resource import AuthorResource

authors_bp = Blueprint('authors', __name__)
api = Api(authors_bp)

api.add_resource(AuthorResource, '', '/<int:author_id>')
