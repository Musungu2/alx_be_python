class Book:
    def __init__(self, title, author,_is_checked_out):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        self.__is_checked_out = True

    def return_book(self):
        self.__is_checked_out = False

    def is_checked_out(self):
        return self.__is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self.__books.append(book)

    def check_out_book(self, title):
        for book in self.__books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                print(f'"{title}" has been checked out.')
                return
        print(f'"{title}" is not available.')

    def return_book(self, title):
        for book in self.__books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                print(f'"{title}" has been returned.')
                return
        print(f'"{title}" was not checked out.')

    def list_available_books(self):
        print("Available Books:")
        for book in self.__books:
            if not book.is_checked_out():
                print(f'- "{book.title}" by {book.author}')
