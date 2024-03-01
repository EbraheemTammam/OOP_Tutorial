
#   define class
class Book:
    #   static variable
    all_books = []
    #   constructor
    def __init__(self, title: str, author: str, genre: str) -> None:
        self.title = title
        self.author = author
        self.genre = genre
        Book.all_books.append(self)
    #   special function for representation
    def __repr__(self) -> None:
        return self.title