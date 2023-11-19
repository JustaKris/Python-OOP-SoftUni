from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content


class PressFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[:20]


class EmailFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[:700]


class Printer:
    @staticmethod
    def get_book(book: Book, formatter: Formatter) -> str:
        formatted_book = formatter.format(book)
        return formatted_book
