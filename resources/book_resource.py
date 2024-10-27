from flask_restful import Resource
from flask import request
from models.book import Book, db
from schemas.book_schema import BookSchema
from marshmallow import ValidationError

book_schema = BookSchema()
books_schema = BookSchema(many=True)

class BookResource(Resource):
    def get(self, book_id=None):
        if book_id:
            book = Book.query.get(book_id)
            if not book:
                return {"message": "Book not found"}, 404
            return book_schema.dump(book), 200
        else:
            books = Book.query.all()
            return books_schema.dump(books), 200

    def post(self):
        try:
            data = book_schema.load(request.get_json())
        except ValidationError as err:
            return {"errors": err.messages}, 400

        new_book = data if isinstance(data, Book) else Book(**data)
        db.session.add(new_book)
        db.session.commit()
        return {"message": "Book created", "book_id": new_book.id}, 201

    def put(self, book_id):
        book = Book.query.get(book_id)
        if not book:
            return {"message": "Book not found"}, 404

        try:
            data = book_schema.load(request.get_json(), partial=True)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        for key, value in data.items():
            setattr(book, key, value)

        db.session.commit()
        return {"message": "Book updated", "book_id": book.id}, 200

    def delete(self, book_id):
        book = Book.query.get(book_id)
        if not book:
            return {"message": "Book not found"}, 404

        db.session.delete(book)
        db.session.commit()
        return {"message": "Book deleted"}, 200