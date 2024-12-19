from typing import List, Optional

class Book:
    def __init__(self, id: int, title: str, author: str, year: int):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

class Member:
    def __init__(self, id: int, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email

# In-memory storage
books_db: List[Book] = []
members_db: List[Member] = []

