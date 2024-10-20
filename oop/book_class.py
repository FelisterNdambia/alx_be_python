class Book:
    # Constructor to initialize book attributes
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    # Destructor to print a message when a book instance is deleted
    def __del__(self):
        print(f"Deleting {self.title}")
    
    # String representation (__str__) to return a readable format
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    
    # Official representation (__repr__) to return a format for recreating the object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"
