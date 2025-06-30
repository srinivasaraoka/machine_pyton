'''  Auther: Srinivas '''
'''

Abstraction: representing essential features and hiding unnecessary details to 
simplify the complexity.(sunil nareina bowling)
Abstraction is about simplifying the interface, hiding complex details, and 
allowing the user to interact with the object without knowing the internal 
mechanics. It is implemented using abstract classes or methods.

􏰁 Encapsulation: bundling of data and methods that operate on that data within a single
 unit (class).􏰀
Encapsulation is about controlling access to an object’s internal state by using 
public, private, or protected access modifiers, ensuring that the data is not 
directly exposed.
􏰁 Inheritance: ability of a class to inherit properties and methods from its parent 
class.􏰀
􏰁 Polymorphism: ability of an object to take on different forms or behaviors based on 
the context.􏰀
􏰁 


Method overloading:Method overloading in Python refers to 
defining multiple methods with the same name but different 
parameters within a class. However, Python does not support 
method overloading by default as it does in languages like Java. In Python, you can a
chieve a similar effect by using default arguments or using variable-length arguments.


methodoveriding:Method overriding in Python refers to defining 
a method in a child class that already exists in its parent class with the same name 
and signature. The method in the child class overrides the method in the parent class, 
providing a different implementation.

__init__.py file
__init__() function
   The __init__.py file lets the Python interpreter know that a directory contains 
code for a Python module. It can be blank. Without one, you cannot import modules from 
another folder into your project.
The role of the __init__.py file is similar to the __init__ function in a Python class. 
The file essentially the constructor of your package or directory without it being called such. 
It sets up how packages or functions will be imported into your other files.
 The __init__ method is similar to constructors in C++
  and Java. Constructors are used to initialize the object’s
   state.
   # A Sample class with init method
  class Person:
 # init method or constructor
  def __init__(self, name):
 self.name = name
   # Sample Method
 def say_hi(self):
 

Abstraction works on the design level.

Abstraction is implemented to hide unnecessary data and withdrawing
relevant data.
It highlights what the work of an object instead of how the objec work is
Abstraction focuses on outside viewing, for example, shifting the car
Abstraction is supported in Java with the interface and the abstract class  


Encapsulation works on the application level.
Encapsulation is the mechanism of hiding the code and the data together from the outside world or misuse.
It focuses on the inner details of how the object works. Modifications can be done later to the settings.
Encapsulation focuses on internal working or inner viewing, for example, the production of the car.
Encapsulation is supported using, e.g. public, private and secure access modification systems.
In a nutshell, encapsulation is hiding the data with the help of getters and setters.

'''

Basic Class Definition


class MyClass:  
    pass
Create an Object of a Class
obj = MyClass()

#Class with Constructor
class Person:  
    def __init__(self, name):  
        self.name = name
Access Class Attribute
print(obj.name)

#Define Instance Method
class Person:  
    def greet(self):  
        print("Hello")
Call Instance Method
obj.greet()
Class with Class Variable
class Dog:  
    species = "Canine"
Access Class Variable
print(Dog.species)
Class Inheritance
class Animal:  
    pass  
class Dog(Animal):  
    pass
Override Method in Child Class




class Animal:  
    def sound(self):  
        print("Generic sound")  
class Dog(Animal):  
    def sound(self):  
        print("Bark")
Call Parent Class Method Using super()
class Dog(Animal):  
    def sound(self):  
        super().sound()
Use isinstance() to Check Object Type
isinstance(obj, Dog)
Use issubclass() to Check Inheritance
issubclass(Dog, Animal)
Private Variable with Name Mangling
class Demo:  
    def __init__(self):  
        self.__hidden = 42
Protected Member Convention
class Demo:  
    def __init__(self):  
        self._value = 10
Static Method
class Math:  
    @staticmethod  
    def add(a, b):  
        return a + b
#Class Method
class Example:  
    count = 0  
    @classmethod  
    def increment(cls):  
        cls.count += 1
        
#Magic Method: __str__
def __str__(self):  
    return f"Person({self.name})"
Magic Method: __len__
def __len__(self):  
    return len(self.data)
Operator Overloading: +
def __add__(self, other):  
    return self.value + other.value

#Encapsulation Example
class Bank:  
    def __init__(self):  
        self.__balance = 0  
    def deposit(self, amount):  
        self.__balance += amount
#Polymorphism via Duck Typing
def make_sound(animal):  
    animal.sound()
#Abstract Base Class
from abc import ABC, abstractmethod  
class Shape(ABC):  
    @abstractmethod  
    def area(self):  
        pass
Multiple Inheritance
class A: pass  
class B: pass  
class C(A, B): pass

#Check Method Resolution Order (MRO)
print(C.__mro__)
Use __slots__ to Limit Attributes
class Limited:  
    __slots__ = ['name', 'age']
Object Composition (HAS-A Relationship)
class Engine: pass  
class Car:  
    def __init__(self):  
        self.engine = Engine()
Dynamic Attribute Assignment
obj.new_attr = "dynamic"
Delete Attribute
del obj.name
Class Representation with __repr__
def __repr__(self):  
    return f"MyClass({self.name})"