'''
ability of a class to inherit properties and methods from its parent 
class
This promotes code reuse and establishes a natural hierarchy between 
classes

Inheritance is a key concept for situations where you have an existing class with 
defined attributes and behaviors, and you need a new class that not only shares these 
characteristics but also has its own unique ones. Inheritance allows the new class 
to 'inherit' properties from the existing class while adding or modifying specific features as needed.

class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")

# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  
  # Overridden sound method for Dog
  def sound(self):
    # Call the sound method from Animal
    super().sound()
    # Additional functionality for Dog
    print("Woof!")

# Creating an instance of Dog
my_dog = Dog("Jax", "Bulldog", 5)

# Calling the overridden sound method
my_dog.sound()


'''
class Animal:
    def __init__(self, name):
        self.name= name

class Dog(Animal):
    def bark(self):
        print(self.name,'is bark')

d = Dog("hach puppy")
d.bark()    
#multi level inheritance( grandfather-> father-> child)
class person:  
    def display(self):
        print("clas person calling here")

class employee(person):
    def printing(self):
        print("classs empolyee calling here")

class programmer(employee):
    print("hii")
    def show(self):
        print("class prfogrammer print here")

d = programmer()
d.display()
d.printing()
d.show()  

#multiple inheritanece(father, maother -> child)
class landanimal:
    def printing(self):
        print("this animal will leave on land")

class wateranimal:
    def dispaly(self):
        print("this animal will leave on land")

class frog(landanimal, wateranimal):
    pass

d= frog()
d.dispaly()
d.printing()

#method overriding
'''Method overriding in Python refers to defining a 
method in a child class that already exists in its 
parent class with the same name and signature. The 
method in the child class overrides the method in the 
parent class, providing a different implementation.
'''
class A:
    def display(self):
        print("calss a is calling this is calss A metod")

class B(A):
    def display(self):
        print("calss B is calling this is class B method")
        #super().display()

d = B()
d.display()  
         