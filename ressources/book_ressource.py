from flask_restful import Resource
from models.book import Book, db
from flask import jsonify, request
from schemas.book_schema import BookSchema
from marshmallow import ValidationError

book_schema = BookSchema()

class BookResource(Resource):
    def get(self, book_id=None):
        if book_id:
            book = Book.query.get(book_id)
            if book:
                return jsonify({
                    "id":book.id,
                    "title": book.title,
                    "description": book.description,
                    "publication_date": book.publication_date,
                    "author_id": book.author_id
                })
            return{"message": "Book not found"}, 404
        else:
            books = Book.query.all()
            return jsonify([{
                "id": book.id,
                "title": book.title,
                "description": book.description,
                "publication_date": book.publication_date,
                "author_id": book.author_id
            } for book in books])
    
    def post(self):
        try:
            data = book_schema.load(request.get_json())
        except ValidationError as err:
            return {"errors",err.messages}, 400
        if isinstance(data, Book):
            new_book = data
        else:
            new_book = Book(**data)
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
        if book:
            db.session.delete(book)
            db.session.commit()
            return {"message": "Book deleted"}, 200
        return {"message": "Book not found"}, 404