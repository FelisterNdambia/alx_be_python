# Base class - Book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived class - EBook (inherits from Book)
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Initialize the base class attributes
        self.file_size = file_size  # Additional attribute for EBook

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


# Derived class - PrintBook (inherits from Book)
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Initialize the base class attributes
        self.page_count = page_count  # Additional attribute for PrintBook

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


# Library class demonstrating composition
class Library:
    def __init__(self):
        self.books = []  # List to store book objects

    def add_book(self, book):
        self.books.append(book)  # Add book to the collection

    def list_books(self):
        for book in self.books:
            print(book)  # Print each book's details
