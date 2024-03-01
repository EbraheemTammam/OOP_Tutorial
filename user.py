from book import Book

class User:
    #   constructor
    def __init__(self, name: str, email: str, password: str, phone_number: str) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def login(self, email: str, password: str) -> bool:
        return self.email == email and self.password == password
    
    def welcome(self):
        print(f"Welcome, {self.name}!!, hope you doing well")

    @staticmethod
    def view_all_books():
        print(Book.all_books)

    @staticmethod
    def get_book(title: str) -> int:
        for book in Book.all_books:
            if book.title == title:
                return Book.all_books.index(book)
        return -1
    #   abstract method
    def profile(self):
        pass
    
    def __repr__(self) -> str:
        return self.name