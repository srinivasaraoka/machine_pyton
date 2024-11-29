'''bundling of data and methods that operate on that data within a single
unit (class).
True or False?

You can use a private attribute within the class method.true

It refers to the concept of bundling data (attributes) and methods 
(functions) that operate on the data into a single unit, 
known as a class, and restricting access to some of the object's 
components.
This helps in hiding the internal state of the object and only 
exposing a controlled interface.


Benefits of Encapsulation
Controlled Access: Encapsulation allows you to control how the data is
 accessed and modified. For example, you can validate data before updating it.
Increased Flexibility: By hiding the internal implementation details, you can 
change the internal workings of a class without affecting code that uses the class.

Improved Maintenance: Encapsulation helps in organizing code better, making it 
easier to understand and maintain.
Enhanced Security: By restricting access to internal data, encapsulation helps
 protect the integrity of the data and prevents unintended interference.


Accessing a private attribute directly from outside its class is generally discouraged in Python. However, Python 
employs name mangling for private attributes, which means you can access them using a specific naming convention from 
outside the class if necessary. 
#accesing using name mangling
print(my_car._Car__odometer)
Methods of objects we've looked at so far are called by an instance of a class. However, there are other types methods that 
a class can have - class and static methods.




'''

class car:
    __speed=0
    __name= ''
    def __init__(self):
        self.__updatesoftware()
        self.__speed='200'
        self.__name= 'super car'

    def display(self):
        #print("drive") 
        print(self.__speed) 

    def __updatesoftware(self):
        print("software is updateing")

    def setspeed(self, speed):
        self.__speed= speed
        print(self.__speed)    

d= car()
d.display()
d.setspeed(100)
d.__speed=50
print(d.__speed)
d.display()
#d.__updatesoftware()(try error AttributeError: 'car' object has no attribute 
# '__updatesoftware'. Did you mean: '_car__updatesoftware'?)
        
class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  #regular method
  def describe_book(self):
    print(self.title, 'by', self.author)

  #class method
  @classmethod
  def books_in_series(cls, series_name, number_of_books):
    print('There are', number_of_books, 'books in the', series_name, 'series')

# Creating an instance of Book
my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")

# Using the instance method to describe the book
my_book.describe_book()

# Using the class method to display information about the series
Book.books_in_series("Harry Potter", 7)
