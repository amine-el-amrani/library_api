from flask import Blueprint, jsonify

books_bp = Blueprint('books_bp', __name__)

@books_bp.route('/', methods=['GET'])
def get_books():
    return jsonify({"message": "Welcome to the Books API"})