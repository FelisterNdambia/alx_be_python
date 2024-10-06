# library_management.py

class Book:
    def __init__(self, title, author):
        """Initialize a new book with title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available (not checked out)."""
        self._is_checked_out = False

    def is_available(self):
        """Return True if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store book objects

    def add_book(self, book):
        """Add a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"{title} has been checked out.")
                return
        print(f"{title} is either not available or already checked out.")

    def return_book(self, title):
        """Return a book by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"{title} has been returned.")
                return
        print(f"{title} was not checked out or does not exist in the library.")

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
