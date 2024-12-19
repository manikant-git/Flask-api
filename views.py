from flask import Flask, jsonify, request, abort
from models import Book, Member, books_db, members_db
from typing import List
import random

app = Flask(__name__)

# Simple token-based authentication
valid_tokens = {"admin_token": "admin"}

def require_authentication():
    token = request.headers.get('Authorization')
    if token not in valid_tokens:
        abort(403, description="Forbidden: Invalid Token")

# CRUD for Books
@app.route('/books', methods=['GET'])
def get_books():
    search_title = request.args.get('title')
    search_author = request.args.get('author')
    
    filtered_books = books_db

    if search_title:
        filtered_books = [book for book in filtered_books if search_title.lower() in book.title.lower()]
    if search_author:
        filtered_books = [book for book in filtered_books if search_author.lower() in book.author.lower()]

    return jsonify([book.__dict__ for book in filtered_books])

@app.route('/books', methods=['POST'])
def add_book():
    require_authentication()
    data = request.get_json()
    book = Book(id=random.randint(1, 1000), **data)
    books_db.append(book)
    return jsonify(book.__dict__), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id: int):
    require_authentication()
    book = next((b for b in books_db if b.id == book_id), None)
    if not book:
        abort(404, description="Book not found")
    
    data = request.get_json()
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.year = data.get('year', book.year)
    
    return jsonify(book.__dict__)

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id: int):
    require_authentication()
    book = next((b for b in books_db if b.id == book_id), None)
    if not book:
        abort(404, description="Book not found")
    
    books_db.remove(book)

