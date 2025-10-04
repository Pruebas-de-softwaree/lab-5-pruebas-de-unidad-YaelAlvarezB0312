from library import Library
from book import Book
from user import User

if __name__ == "__main__":
    Library_t = Library()
    Library_t.add_book(Book("To kll a Mockingbird", "Harper Lee", 1960, "ISBN002"))
    Book_t= Book("To kll a Mockingbird", "Harper Lee", 1960, "ISBN002")
    Book_t.borrow()
    Book_t.borrow()