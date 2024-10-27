from flask_restful import Resource
from flask import request
from models.author import Author, db
from schemas.author_schema import AuthorSchema
from marshmallow import ValidationError

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)

class AuthorResource(Resource):
    def get(self, author_id=None):
        if author_id:
            author = Author.query.get(author_id)
            if not author:
                return {"message": "Author not found"}, 404
            return author_schema.dump(author), 200
        else:
            authors = Author.query.all()
            return authors_schema.dump(authors), 200

    def post(self):
        try:
            data = author_schema.load(request.get_json())
        except ValidationError as err:
            return {"errors": err.messages}, 400

        new_author = data if isinstance(data, Author) else Author(**data)
        db.session.add(new_author)
        db.session.commit()
        return {"message": "Author created", "author_id": new_author.id}, 201

    def put(self, author_id):
        author = Author.query.get(author_id)
        if not author:
            return {"message": "Author not found"}, 404

        try:
            data = author_schema.load(request.get_json(), partial=True)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        for key, value in data.items():
            setattr(author, key, value)

        db.session.commit()
        return {"message": "Author updated", "author_id": author.id}, 200

    def delete(self, author_id):
        author = Author.query.get(author_id)
        if not author:
            return {"message": "Author not found"}, 404

        db.session.delete(author)
        db.session.commit()
        return {"message": "Author deleted"}, 200