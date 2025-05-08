# Assignment-3: Library Management System
# Create a base class Book.
# Create a derived class EBook that inherits from Book.
# Create a Library class to hold and manager Books information
# Implement methods add_books and display_books in Library class.
# Make use of a list to store info of books in the Library
# Make use of for loop to display info of all the books available in the Library
# Add the class member book_count to Library class and keep track of count whenever a book is added to the library
# Optional: Add any additional methods as you want inside

class Book:
    def __init__(self,book_name,authour,edition,price):
        self.book_name = book_name
        self.authour = authour
        self.edition = edition  
        self.price = price  

class Library:
    def __init__(self):
        self.books = []

    def add_books(self,book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No book found in library")
            return
        print("\n--- Book List ---")
        for book in self.books:
            print(f"{book.book_name} by {book.authour} - {book.edition} | ₹{book.price}")  
            if isinstance(book, EBook):
                print(f"Download link: {book.download_link}")
        print("\n")  

class EBook(Book):
    def __init__(self,book_name,author,edition,price,download_link):
        super().__init__(book_name,author,edition,price)
        self.download_link = download_link


Lib = Library()

Lib.add_books(Book('JavaScript','Brendan Eich', '2nd Edition', 500))
Lib.add_books(Book('Python','Guido van Rossum', '3rd Edition', 300))
Lib.add_books(Book('React','Jordan Walke', '1st Edition', 1300))
Lib.display_books()
Lib.add_books(EBook('eBook','amendon', '1st edition', 100,'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'))
Lib.display_books()