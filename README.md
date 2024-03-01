# Programming paradigms:

- ### procedural
```py
def sum_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers = [1, 2, 3, 4, 5]
result = sum_numbers(numbers)
print(result)  # Output: 15
```
- ### functional 
```py
from functools import reduce

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15
```
- ### declarative 
```py
numbers = [1, 2, 3, 4, 5]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)  # Output: [2, 4]

```
- ### object-oriented
***
# OO pyramid:
```py
"""
                  /\                              |----->   class
                 /  \                             |
                /    \                            |----->   objects
               /      \                           |
------------- /paradigm\                          |----->   encapsulation
|            /----------\                         |
|           /  concepts  \ -----------------------|----->   abstraction
|          /--------------\                       |
|         /   principles   \ -----------------    |----->   polymorphism
|        /------------------\                |    |
|       /   design pattern   \ ----          |    |----->   inheritance
|      /______________________\    |         |
|                                  |         |
|                                  |        \./
|                                  |         |
|                                  |       SOLID
|       best practice for <--------|         |
|       some repetitive            |         |
|       tasks                      |         |---->  Single Responsibility (SRP)
|                                  |         |
|       overstress in     <--------|         |---->  Open/Closed (OCP)
|       study? X                   |         |
|       overuse in                 |         |---->  Liskov Substitution (LSP)
|       projects? X                |         |
|                                  |         |---->  Interface Segregation (ISP)
|       use when needed   <--------|         |
|       domains?          <--------|         |---->  Dependency Inversion (DIP)
|   
|   
|                 Important
|                      |
|          ------------|------------
|          |           |           |
|         DRY        KISS        YAGNI
|         |            |           |
|         |            |           |
|      Don't         Keep         You 
|      Repeat        It           Ain't
|      Yourself      Simple,      Gonna
|                    Stupid!      Need It
|   
|   
|                   |-------> OOA (Object oriented analysis)
|                   |
|-------------------|-------> OOD (Object oriented design)
                    |
                    |-------> OOP (Object oriented programming)
"""
```
***
# How to define class:
```py
class MyClass:
    #   code goes here
``` 
## refrence vs. object:
```py
obj = MyClass   #   refrence
obj = MyClass() #   object
```
##  Special functions:
- ### constructor:
> special function that's called automatically when instance is created
```py
class MyClass:
    #   cosntructor
    def __init__(self):
        pass

class MyClass:
    #   assign member variables using constructor
    def __init__(self, attribute):
        self.attribute = attribute

class MyClass:
    #   default constructor
    #   has no parameters
    #   or all parameters 
    #   has default values
    def __init__(self, attribute="value"):
        self.attribute = attribute
```
- ### destructor:
> special function called when object deleted
```py
class MyClass:
    def __init__(self, attribute="value"):
        self.attribute = attribute
    #   destructor
    def __del__(self):
        print("object deleted")

obj = MyClass()
del obj #   output: object deleted
```
## the self pointer:
> refer to the current object
***
# Data hiding:
> visible vs. hidden
```py
class Person:
    def __init__(self, name, national_id):
        self.name = name
        self.__national_id = national_id # marked hidden

p = Person("name", "123")
p.__national_id # result in error
```
> getters and setters
```py
class Person:
    def __init__(self, name, national_id):
        self.name = name
        self.__national_id = national_id # marked hidden
    def get_national_id(self):
        return self.national_id

p = Person("name", "123")
p.get_national_id() # output: 123
```
> are they evil?
#### the philosophy of python has no data hiding
```py
class Person:
    def __init__(self, name, national_id):
        self.name = name
        self.__national_id = national_id # marked hidden
    def get_national_id(self):
        return self.national_id

p = Person("name", "123")
#   break data hiding
p._Person__national_id # output: 123
```
# Abstraction concept:
> what vs. how
```py
def who_am_i(self):
    print(f"I'm {self.name}")

class Person:
    def __init__(self, name):
        self.name = name
    who_am_i = who_am_i #   separate what from how

def get_name(self):
    return self.name

Person.get_name = get_name #    dynamically assigned
```
> using different files for code separation
```py
#   file name: person.py
class Person:
    def __init__(self, name, national_id):
        self.name = name
```
```py
#   file name: main.py
from person import Person
p = Person("name")
```
***
# Static members
```py
class MyClass:
    attribute = "value" # static member variable
    @staticmethod       # static member function
    def foo():          # no self passed
        pass
```
***
# UML:
##  class diagram
### relationships between class
- #### association
- #### aggregation                    
> weak 'has a' relationship
- #### composition
> strong 'has a' relationship
- #### generalization (inheritance)
> 'is a' relationship
***
# Inheritence:
> 'is a' relationship\
> common vs. unique
```py
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person): # extends person
    pass

s = Student("name")
s.name # output: name
```
***
# Pplymorphism:
> can have multiple forms
```py
class GeometricalShape:
    #   abstract method
    def compute_area(self):
        pass

class Square(Geometricalshape):
    def __init__(self, length):
        self.length = length
    #   override compute_area
    def compute_area(self):
        return self.length ** 2
```
> coupling
***
# Operator overloading
```py

class GeometricalShape:
    def compute_area(self):
        pass

class Square(Geometricalshape):
    def __init__(self, length):
        self.length = length
    def compute_area(self):
        return self.length ** 2
    #   override operator +
    def __add__(self, other):
        return Square(self.length + other.length)

s1 = Square(2)
s2 = Square(3)
s = s1 + s2
s.length # output: 5
```