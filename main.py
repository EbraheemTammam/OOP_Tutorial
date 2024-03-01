
"""
        programming paradigms:
                |
                |
                |---->  procedural
                |
                |---->  functional 
                |
                |---->  declarative 
                |
                |---->  object-oriented

        

    oo pyramid:
            
                      /\                                    |----->   class
                     /  \                                   |
                    /    \                                  |----->   objects
                   /      \                                 |
----------------- /paradigm\                                |----->   encapsulation
|                /----------\                               |
|               /  concepts  \ -----------------------------|----->   abstraction
|              /--------------\                             |
|             /   principles   \ -----------------------    |----->   polymorphism
|            /------------------\                      |    |
|           /   design pattern   \ ----                |    |----->   inheritance
|          /______________________\    |               |
|                                      |               |
|                                      |              \./
|                                      |               |
|                                      |             SOLID
|           best practice for <--------|               |
|           some repetitive            |               |
|           tasks                      |               |---->  Single Responsibility (SRP)     #   each class responsible for one single perpose
|                                      |               |
|           overstress in     <--------|               |---->  Open/Closed (OCP)               #   open for extension, closed for modification
|           study? X                   |               |
|           overuse in                 |               |---->  Liscov Substitution (LSP)       #   child class substitutable for parent class
|           projects? X                |               |
|                                      |               |---->  Interface Segregation (ISP)     #   small client-specific interface
|           use when needed   <--------|               |
|           domains?          <--------|               |---->  Dependency Inversion (DIP)      #   high level classes shouldn't depend on low level classes
|       
|       
|                     Important
|                          |
|              ------------|------------
|              |           |           |
|             DRY        KISS        YAGNI
|             |            |           |
|             |            |           |
|          Don't         Keep         You 
|          Repeat        It           Ain't
|          Yourself      Simple,      Gonna
|                        Stupid!      Need It
|       
|       
|                           |-------> OOA (Object oriented analysis)
|                           |
|---------------------------|-------> OOD (Object oriented design)
                            |
                            |-------> OOP (Object oriented programming)
                            
"""


"""
    class definition

    --> reference vs instance/object

	--> python has no variable declaration, i.e. must set default value
"""


"""
	constructor & destructor

    --> special member functions?
    --> constructor
    --> default constructor

    --> destructor


    --> the 'self' pointer 
"""


"""
	data hiding concept

    --> visible vs. hidden

    --> why we need data hiding?
    --> access modifiers
    
    --> getters & setters | accessors and mutators
    --> evil or not?

    --> the philosophy of python
	--> between python and c++

    --> can data hiding in python be broken?
"""


"""
    abstraction concept

    --> what vs. how
    --> separate what from how

    --> other files for code separation (header files/modules)
"""


"""
    static members

    --> static variables
    --> static functions
"""


"""
    UML

    --> class diagram

    -->   relationships
                |
                |------> association
                |------> aggregation                    :   weak 'has a' relationship
                |------> composition                    :   strong 'has a' relationship
                |------> generalization (inheritance)   :   'is a' relationship

    how to draw each of which

    multiplicity / specify cardinality

    importance of class diagrams
"""

"""
    inheritance

    --> 'is a' relationship
    --> common vs. unique

    --> reusability

    --> inheritance and data hiding

    |--> multiple inheritance
    |--> multilevel inheritance
    |--> hyprid
"""

"""
    polymorphism = "can have multiple shapes"

    --> override methods
    --> constructor & destructor


    --> override vs overload
    --> python doesn't support function overloading

    --> usage

    --> abstract class vs interface

    --> coupling
"""

"""
    operator overloading

    dir
"""

#   import our classes
from book import Book
from admin import Admin
from customer import Customer



if __name__ == "__main__":
    #   initial admin user
    admin = Admin("Ebraheem", "admin@example.com", "password", "010")
    #   initialize 2 books for initial usage
    Book(title="book of laugher and forgetting", author="Milan Kundera", genre="novel")
    Book(title="the unbearable lightness of being", author="Milan Kundera", genre="novel")
    #   simulate server
    while 1:
        inp = int(input("Enter 1 to login or 2 to sign up: "))
        if inp == 1:
            email = input("Enter your Email: ")
            password = input("Enter your password: ")
            #   check admin login
            if admin.login(email=email, password=password):
                admin.profile()
                continue
            #   search for customer login
            for user in Customer.all_customers:
                if user.login(email, password):
                    print("logged in successfully!")
                    user.profile()
                    break
                print("invalid credentials")
        elif inp == 2:
            name = input("Enter your name: ")
            phone_number = input("Enter your phone number: ")
            email = input("Enter your Email: ")
            password = input("Enter your password: ")
            user = Customer(name=name, email=email, phone_number=phone_number, password=password)
            print("account created successfully!")
            user.profile()
            continue
        else:
            print("not a valid input")
            continue