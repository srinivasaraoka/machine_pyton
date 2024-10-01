'''  Auther: Srinivas '''
'''

Encapsulation is about controlling access to an object’s internal state by using 
public, private, or protected access modifiers, ensuring that the data is not 
directly exposed.
Abstraction is about simplifying the interface, hiding complex details, and 
allowing the user to interact with the object without knowing the internal 
mechanics. It is implemented using abstract classes or methods.
􏰁 Encapsulation: bundling of data and methods that operate on that data within a single
 unit (class).􏰀
􏰁 Inheritance: ability of a class to inherit properties and methods from its parent 
class.􏰀
􏰁 Polymorphism: ability of an object to take on different forms or behaviors based on 
the context.􏰀
􏰁 Abstraction: representing essential features and hiding unnecessary details to 
simplify the complexity.(sunil nareina bowling)


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