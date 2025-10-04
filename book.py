class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            raise ValueError("The book is already borrowed")
        else:
           print("The borrow is not borrowed")
        self.borrowed = True

    def return_book(self):
        if not self.borrowed:
            raise ValueError("The book is not currently borrowed")
        self.borrowed = False

if __name__ == "__main__":
    libro=Book("El racismo de Mischa", "Aly", "2024", "isbn0001")
    libro.return_book()
