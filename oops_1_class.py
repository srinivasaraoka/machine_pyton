'''
Class
A class is a blueprint for creating objects. 
It defines a set of attributes (data) and methods (functions) that 
the objects created from the class will have. 
Think of a class as a template for objects

object
An object is an instance of a class. It represents a specific 
realization of the class with actual values for its attributes.
Each object can have unique attribute values but shares the same 
structure and behavior defined by its class.

To add attributes to a class, you must define the __init__ method. 
This method's first parameter is always self, which represents the instance of the 
class. Following self, you specify the attributes you wish to include. Then, inside 
the function, you assign values to the initialized object's attributes, setting their 
initial state.

#Class methods are called on the class itself, not on individual instances. 
# This allows their use without needing to create a class instance. 
# They are especially useful for actions relevant to the class as a whole, 
# rather than actions limited to a single object. Here's an example:
#Class methods are created using the @classmethod decorator and take the cls argument, 
# which refers to the class itself.
The main difference between functions and methods is that functions are independent 
and can be called on their own, while methods are associated with a class and can be 
called only with its instance. This means that you can't call a method without having 
the instance of a class where that method is defined.

Identify the elements
print(): func
my_car.honk(): met

'''

class person:
    def __init__(self, name):
        self.name= name
    def display(self):
        print("hello",self.name)    

d= person("srinu")
d.display()  
person("sriinu").display()

#Q1, how to access the class variable 

# Parent class
class Parent:
    parent_variable= 'srinivas1'
    def dispaly(self):
        print("I am parent class")
class Child(Parent):
    child_variable  = 'chiled varibl2'
    def childdisplay(self):
        print("I am child class")
        print(Parent.parent_variable, self.child_variable, self.parent_variable)      


parent_obj=Parent()
child_obj=Child()
print(child_obj.child_variable, child_obj.parent_variable)


#Class methods are called on the class itself, not on individual instances. 
# This allows their use without needing to create a class instance. 
# They are especially useful for actions relevant to the class as a whole, 
# rather than actions limited to a single object. Here's an example:
#Class methods are created using the @classmethod decorator and take the cls argument, 
# which refers to the class itself.


Instances share everything that a class has, including the class methods. This means that you call a class method on instances as well.

class Book:
  def __init__(self, title, author):
    #If the value of a variable is varied from object to object, then such type of variables are called 
    #instance variables.  
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



#Static methods are similar to class methods, except they don't receive any additional 
# arguments; they are identical to normal functions that belong to a class.

#They are marked with the @staticmethod decorator.

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  #regular method
  def describe_book(self):
    print(self.title, 'by', self.author)

  #staticmethod
  @staticmethod
  def books_in_series(series_name, number_of_books):
    print('There are', number_of_books, 'books in the', series_name, 'series')

# Creating an instance of Book
my_book = Book("Harry Potter and the Sorcerer's Stone", "J.K. Rowling")

# Using the instance method to describe the book
my_book.describe_book()

# calling the static method
Book.books_in_series("Harry Potter", 7)
