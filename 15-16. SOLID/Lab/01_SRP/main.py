from books import Book, Library


def main():
    book1 = Book("Lord of Ring", "Golum")
    book2 = Book("Harry Potter and the battle for gender equality", "J.K. 'The equalizer' Rolling")
    book3 = Book("Harry Potter and the alphabet people", "Joe Rogan")

    library = Library()
    library.add_book(book1)
    library.add_book(book2)

    print(repr(library))
    print(library.find_book(book3))


if __name__ == '__main__':
    main()
