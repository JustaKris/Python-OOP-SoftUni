from typing import List
from project.user import User


class Library:
    def __init__(self):
        self.user_records: List[User] = []
        self.books_available = {}  # {author: [books_available]}
        self.rented_books = {}  # {usernames: {book names: days to return}}

    def get_books(self, author: str, book_name: str, days_to_return: int, user: User):
        if book_name in self.rented_books:
            return f'"The book "{book_name}" is already rented and will be available in {[book.keys() for book in self.rented_books.values()]} days!"'
        elif book_name in self.books_available:
            pass

    def return_book(self, author: str, book_name: str, user: User):
        pass
