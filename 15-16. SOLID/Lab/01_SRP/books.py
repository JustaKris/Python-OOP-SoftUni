from typing import List


class Book:

    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page: int):
        self.page = page


class Library:

    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def find_book(self, book: Book):
        return next((b for b in self.books if b.title == book.title), "Book not found")

    def __repr__(self):
        return f"Library books:\n" + '\n'.join(f"{book.title} by {book.author}" for book in self.books)
