class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.is_borrowed = False

    def borrow_book(self):
        if (not self.is_borrowed):
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if (self.is_borrowed):
            self.is_borrowed = False
            return True
        return False

class Borrower:
    def __init__(self, name, max_books=3):
        self.name = name
        self.borrowed_books = []
        self.max_books = max_books

    def borrow(self, book):
        if (len(self.borrowed_books) < self.max_books and book.borrow_book()):
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if ((book in self.borrowed_books) and book.return_book()):
            self.borrowed_books.remove(book)
            return True
        return False

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self, book):
        self.books.append(book)

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)

    def get_available_books(self):
        return [book for book in self.books if not book.is_borrowed]

    def get_genres(self):
        return set(book.genre for book in self.books)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_borrower(self, name):
        for borrower in self.borrowers:
            if borrower.name == name:
                return borrower
        return None

# Create library
library = Library()
# Add books to library
book1 = Book("1984", "George Orwell", "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Fiction")
library.add_book(book1)
library.add_book(book2)

# Add borrower to library
borrower1 = Borrower("Alice")
library.add_borrower(borrower1)
# Borrow a book
print(borrower1.borrow(book1))
# Check available books
print([book.title for book in library.get_available_books()])
# Check genres
print(library.get_genres())
# Return a book
print(borrower1.return_book(book1))
# Check available books again
print([book.title for book in library.get_available_books()])
