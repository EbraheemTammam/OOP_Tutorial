from user import User, Book

#   extends User class
class Admin(User):
    #   constructor
    def __init__(self, name: str, email: str, password: str, phone_number: str) -> None:
        #   invoke parent constructor
        super().__init__(name, email, password, phone_number)
    #   override profile function in parent class
    def profile(self):
        print("\n\n\n")
        self.welcome()
        while 1:
            print("\n\n\n")
            inp = int(input("Enter\n1 to add a book\n2 to remove a book\n3 to view all books\n4 to logout\n\n: "))
            if inp == 1:
                title = input("Enter the title of book to be added: ")
                author = input("Enter the author name for the book to be added: ")
                genre = input("Enter the genre of book to be added: ")
                Admin.add_book(title=title, author=author, genre=genre)
                continue
            elif inp == 2:
                title = input("Enter the title of book to be removed: ")
                Admin.remove_book(title=title)
                continue
            elif inp == 3:
                User.view_all_books()
            elif inp == 4:
                return
            else:
                print("Not a valid input")
                continue
    #   static method
    @staticmethod
    def add_book(title: str, author: str, genre: str) -> None:
        Book(title=title, author=author, genre=genre)
        print(f"book {title} added successfully!")

    @staticmethod
    def remove_book(title: str) ->  None:
        book_index = User.get_book(title)
        if book_index == -1:
            print(f"no book found with title: {title}")
        Book.all_books.pop(book_index)    
        print(f"book {title} deleted successfully!")