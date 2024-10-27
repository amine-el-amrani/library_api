from flask_restx import Resource, fields
from flask import request
from models.book import Book, db
from schemas.book_schema import BookSchema
from marshmallow import ValidationError

# Initialiser le schéma Marshmallow pour Book
book_schema = BookSchema()
books_schema = BookSchema(many=True)

# Définir le modèle pour la documentation Swagger avec Flask-RESTX
book_model = {
    "title": fields.String(required=True, description="Title of the book"),
    "description": fields.String(description="Description of the book"),
    "publication_date": fields.Date(description="Publication date of the book"),
    "author_id": fields.Integer(required=True, description="Author ID of the book")
}

class BookListResource(Resource):
    def get(self):
        """List all books"""
        books = Book.query.all()
        return books_schema.dump(books), 200

    def post(self):
        """Create a new book"""
        try:
            data = book_schema.load(request.get_json())
        except ValidationError as err:
            return {"errors": err.messages}, 400

        new_book = Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return {"message": "Book created", "book_id": new_book.id}, 201


class BookResource(Resource):
    def get(self, book_id):
        """Retrieve a book by ID"""
        book = Book.query.get(book_id)
        if not book:
            return {"message": "Book not found"}, 404
        return book_schema.dump(book), 200

    def put(self, book_id):
        """Update a book by ID"""
        book = Book.query.get(book_id)
        if not book:
            return {"message": "Book not found"}, 404

        try:
            data = book_schema.load(request.get_json(), partial=True)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        # Mettre à jour les champs du livre existant
        for key, value in data.items():
            setattr(book, key, value)

        db.session.commit()
        return {"message": "Book updated", "book_id": book.id}, 200

    def delete(self, book_id):
        """Delete a book by ID"""
        book = Book.query.get(book_id)
        if not book:
            return {"message": "Book not found"}, 404

        db.session.delete(book)
        db.session.commit()
        return {"message": "Book deleted"}, 200
