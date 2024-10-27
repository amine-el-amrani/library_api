from flask_restx import Resource, fields
from flask import request
from models.author import Author, db
from schemas.author_schema import AuthorSchema
from marshmallow import ValidationError

# Initialiser le schéma Marshmallow pour Author
author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

# Définir le modèle pour la documentation Swagger avec Flask-RESTX
author_model = {
    "name": fields.String(required=True, description="Name of the author"),
    "bio": fields.String(description="Biography of the author")
}

class AuthorListResource(Resource):
    def get(self):
        """List all authors"""
        authors = Author.query.all()
        return authors_schema.dump(authors), 200

    def post(self):
        """Create a new author"""
        try:
            data = author_schema.load(request.get_json())
        except ValidationError as err:
            return {"errors": err.messages}, 400

        new_author = Author(**data)
        db.session.add(new_author)
        db.session.commit()
        return {"message": "Author created", "author_id": new_author.id}, 201


class AuthorResource(Resource):
    def get(self, author_id):
        """Retrieve an author by ID"""
        author = Author.query.get(author_id)
        if not author:
            return {"message": "Author not found"}, 404
        return author_schema.dump(author), 200

    def put(self, author_id):
        """Update an author by ID"""
        author = Author.query.get(author_id)
        if not author:
            return {"message": "Author not found"}, 404

        try:
            data = author_schema.load(request.get_json(), partial=True)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        # Mettre à jour les champs de l'auteur
        for key, value in data.items():
            setattr(author, key, value)

        db.session.commit()
        return {"message": "Author updated", "author_id": author.id}, 200

    def delete(self, author_id):
        """Delete an author by ID"""
        author = Author.query.get(author_id)
        if not author:
            return {"message": "Author not found"}, 404

        db.session.delete(author)
        db.session.commit()
        return {"message": "Author deleted"}, 200
