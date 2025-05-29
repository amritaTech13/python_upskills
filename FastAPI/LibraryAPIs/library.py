class Book:
    def __init__(self,book_name,author,edition,price):
        self.book_name = book_name
        self.author = author
        self.edition = edition  
        self.price = price  
        self.is_available= False

    def borrow(self, book_name):
        if not self.is_available:
            self.is_available = True
            print(f"you have borrow {book_name}")
        else:   
            print(f"you have already borrowd {book_name}")

    def returnBook(self, book_name):
        if self.is_available:
            self.is_available = False
            print(f"you have returend the {book_name} book ")
        else:
            print(f"{book_name} was not borrowd!")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            return []
        return self.books

    def book_borrow(self, book_name):
        for book in self.books:
            if book.book_name == book_name:
                book.borrow(book_name)
                return
        else:
            print(f"{book_name} not available in library")

    def book_return(self, book_name):
        for book in self.books:
            if book.book_name == book_name:
                book.returnBook(book_name)
                return
        else:
             print(f"{book_name} not available in library")


class EBook(Book):
    def __init__(self,book_name,author,edition,price,download_link):
        super().__init__(book_name,author,edition,price)
        self.download_link = download_link


# Lib = Library()

# Lib.add_books(Book('JavaScript','Brendan Eich', '2nd Edition', 500))
# Lib.add_books(Book('Python','Guido van Rossum', '3rd Edition', 300))
# Lib.add_books(Book('React','Jordan Walke', '1st Edition', 1300))
# Lib.display_books()
# Lib.add_books(EBook('eBook','amendon', '1st edition', 100,'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'))
# Lib.display_books()
# Lib.book_borrow('Python')
# Lib.book_return('Python')