'''
 
It enables a single function or operator to work in different ways based on the 
type of object it is operating on. Polymorphism facilitates flexibility and the 
ability to handle different data types or objects using a unified interface.

Polymorphism means that some code or operations or objects behave differently 
in different contexts. In C++, following features support polymorphism.
Compile Time Polymorphism: Compile time polymorphism means compiler knows 
which function should be called when a polymorphic call is made. C++ supports 
compiler time polymorphism by supporting features like templates, function overloading and default arguments.
Run Time Polymorphism: Run time polymorphism is supported by virtual functions. 
The idea is, virtual functions are called according to the type of object pointed or referred, not according to the 
type of pointer or reference. In other words, virtual functions are resolved late, at runtime.



Key Aspects of Polymorphism
Method Overriding: Subclasses can provide specific implementations of methods that 
are already defined in their parent classes. This allows the same method name to be 
used in different contexts.
Method Overloading: This allows multiple methods with the same name but different 
parameters to be defined in the same class. (Note: Python does not support method 
overloading in the traditional sense as seen in languages like Java, but you can 
achieve similar behavior using default arguments or variable-length argument lists.)

There are two main types of polymorphism in Python:

Compile-time polymorphism (also known as method overloading): Python doesn't support method overloading natively.
Run-time polymorphism (method overriding): This is where Python shines by allowing subclasses to define their own versions of methods that are already defined in their parent classes.

Duck Typing: Python uses duck typing, which means that if an object behaves like a 
certain type (i.e., it implements the expected methods and properties), it can be 
used as that type. This allows for more flexible and less tightly coupled code.

'''

class Dog:
    def make_sound(self):
        print("dog bars")

class Cat:
    def make_sound(self):
        print("cat memmmm meioem ")  

def makessound(animalobj):
    animalobj.make_sound()   

dogobj= Dog()
catobj= Cat()
makessound(dogobj)
makessound(catobj)  




'''Method Overloading (Pythonic Approach)

While Python does not support traditional method overloading, you can achieve similar functionality using default arguments or variable-length arguments.
'''
class Greeter:
    def greet(self, name=None):
        if name is None:
            return "Hello, World!"
        else:
            return f"Hello, {name}!"

greeter = Greeter()

print(greeter.greet())            # Output: Hello, World!
print(greeter.greet("Alice"))     # Output: Hello, Alice!
'''
In this example, the greet method handles different numbers of arguments using 
default values, effectively providing multiple behaviors for the same method name.
'''
'''
Duck Typing

Duck typing means that you don’t need to specify the exact type of an object; 
you only need to ensure that it behaves as expected.

'''
class Bird:
    def fly(self):
        return "Flies in the sky"

class Airplane:
    def fly(self):
        return "Soars through the clouds"

def let_it_fly(flyable):
    print(flyable.fly())

# Using duck typing
flyables = [Bird(), Airplane()]

for flyable in flyables:
    let_it_fly(flyable)

'''    
In this example, let_it_fly can accept any object that has a fly method,
 demonstrating polymorphism through duck typing. 
 Both Bird and Airplane are treated as “flyable” objects because they 
 both implement the fly method.
 '''

#1,Duck type
'''
The term "duck typing" comes from the saying:

"If it looks like a duck, swims like a duck, and quacks like a duck, then it 
probably is a duck."

In Python, this means that the type or class of an object is less important 
than the methods or properties it supports. If an object behaves like a 
certain type (e.g., it has the methods or properties you need), then it can 
be used as if it were that type.

Key Points:
No Explicit Type Checking: In duck typing, you don't explicitly check the type 
of an object. Instead, you use the object based on its behavior.
Flexibility: This allows for more flexible and reusable code because functions 
or methods can work with any object that supports the expected behavior, 
regardless of its actual type

'''
class Duck:
    def swim(self):
        print("duck is swimming")
    def speak(self):
        print("duck is speak like quik.. quick..")   

class Dog:
    def swim(self):
        print("dog is swimming")
    def speak(self):
        print("dog is speak like bow.. bow..")  

def display(obj):
    obj.swim()
    obj.speak()
o= Dog()
o2= Duck()
display(o)
display(o2) # irrecpect of class it will run using the object


#2,oprator(+) overloading

print(1+2)
print("1"+"2")
print(int.__add__(1,2))
print(str.__add__("1","3"))

class Compleaxnumbers:
    def __init__(self, real, imagenary):
        self.real=real
        self.imagenary= imagenary
    def __add__(self, other):
        return (f'{self.real+other.real} "+" {self.imagenary+other.imagenary}i')   

c1= Compleaxnumbers(1,2)
c2= Compleaxnumbers(3,4)
print(c1+c2)

#3)method overloading(compile time polymorphism )
#a)default arguments
class Demo:
    def add(self,a,b,c=0): #default arguments
        return a+b+c


d=Demo()
print(d.add(1,2))
print(d.add(1,2,3))
#b) using args and kwargs
class Demo:
    def add(self,*args): #default arguments
        total =0
        for x in args:
            total= total+x
        return total    


d=Demo()
print(d.add(1,2))
print(d.add(1,2,3))
print(d.add(1,2,3,4,5,6))

class Kwademo:
    def add(self,**kwargs): #default arguments
        total =0
        for key, value in kwargs.items():
            print(f'{key}={value}')
        return total    


d=Kwademo( )
d.add(name='srinu',age='28',hight=5.7)
#4)method overriding(run time poly)
class Demo1:
    def dispaly(self):
        print("demo1 display method is calling")

class Demo2(Demo1):
    def dispaly(self):
        print("demo2 display method is called")
        super().dispaly()

d=Demo2()
d.dispaly()        

