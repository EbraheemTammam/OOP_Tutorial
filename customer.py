from user import User, Book

#   inherite from User class
class Customer(User):
    #   static variable
    all_customers = []
    #   cosntructor
    def __init__(self, name: str, email: str, password: str, phone_number: str, books: list = []) -> None:
        #   invoke parent constructor
        super().__init__(name, email, password, phone_number)
        self.books = books

    def buy_book(self, book_title: str) -> None:
        book_index = User.get_book(title=book_title)
        if book_index == -1:
            print(f"No book found with this title: {book_title}")
        self.books.append(Book.all_books[book_index])
        print(f"successfully added {book_title} to the shelf")

    def view_my_books(self):
        print(self.books)
    #   override profile function of parent class
    def profile(self):
        print("\n\n\n")
        self.welcome()
        while 1:
            print("\n\n\n")
            inp = int(input("Enter\n1 to buy a book\n2 to see your books\n3 to view all books\n4 to logout\n\n: "))
            if inp == 1:
                title = input("Enter the title of book to be buy: ")
                self.buy_book(title)
                continue
            elif inp == 2:
                print(self.books)
                continue
            elif inp == 3:
                User.view_all_books()
                continue
            elif inp == 4:
                return
            else:
                print("Not a valid input")
                continue