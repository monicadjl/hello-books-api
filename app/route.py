from flask import Blueprint
#blueprint objects lets us decorate or tag functions to specific routes - if it gets a requestfor hello worls it knows what to do 
from flask import Blueprint, jsonify


books_bp = Blueprint("books", __name__, url_prefix="/books")

class Book:
    def __init__(self, id, title, description):
        self.id = id, 
        self.title = title,
        self.description = description

books = [
    Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
] 

@books_bp.route("", methods=["GET"])
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)