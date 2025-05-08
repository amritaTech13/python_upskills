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
    def __init__(self):
        self.libraray = []

    def add_books(self,book_name, writer, edition, price):
        self.book_name = book_name
        self.writer = writer
        self.edition = edition  
        self.price = price  
        # if not self.libraray:
        self.libraray.append({
            'book_name':book_name, 
            'writer':writer,
            'edition':edition, 
            'price':price
            })

    def display_books(self):
        print("\n--- Book List ---")
        for book in self.libraray:
            print(f"{book['book_name']} by {book['writer']} - {book['edition']} | ₹{book['price']}")  

        print("\n")
class EBook(Book):
    def add_books(self,book_name, write, edition,price):
        super().add_books(book_name, write, edition,price)
    def display_books(self):
        super().display_books()
        print("coming from inherite data")



list = Book()
# inheritLis = EBook()
list.add_books('JavaScript','Brendan Eich', '2nd Edition', 500)
list.add_books('Python','Guido van Rossum', '3rd Edition', 300)
list.display_books()
# inheritLis.add_books("eBook","amendon", '1st edition', 100)
# inheritLis.display_books()