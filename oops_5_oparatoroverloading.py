class methodol:
    def __init__(self, real, imgenary):
        self.real= real
        self.imgenary= imgenary
        

    def __add__(self, other):
        return f"{self.real+other.real}+ {self.imgenary+other.imgenary}i"    
    
c1= methodol(1,2)
c2= methodol(3,4)
print(c1+c2)


class methodoverloading:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c):
        return a+b+c
d=methodoverloading()
# error print(d.add(1,2))
print(d.add(1,2,3))

class methodoverload:
    def add(self, *args):
        z=0
        for i in args:
            z=z+i
        return z

d=methodoverload()
print(d.add(1,3,5,6,5))

def greed(name,sub, depart='cs'):
    print('srini',name, sub, depart)

greed('jenny',sub='python')

def salary(*numbers, name):
    c=0
    for x in numbers:
        c +=x
    print(c, name)    

salary(1,2,3,name='srinu')  
def person_info(*args, **kwargs):
    for key, value in kwargs.items():
        print(key, value)  
        print(args)
person_info(1,3,name='srinu', age='27', phnum='8309895383') 
person_info(4,5,7,name='srinu', phnum='8309895383') 


'''

Method overloading in Python refers to the concept of having multiple 
methods with the same name but different parameters in a class. 
Unlike some other languages like Java or C++, Python doesn't support 
method overloading in the traditional sense. In Python, if you define 
multiple methods with the same name, the last one defined will 
override the previous ones.

However, Python does provide ways to achieve similar functionality using 
default arguments, 
variable-length arguments, or by using the @staticmethod and 
@classmethod decorators. 
Here's how you can work around the lack of traditional method overloading:

1. Using Default Arguments
You can use default arguments to achieve a form of overloading by giving parameters default values. This allows you to call the method with different numbers of arguments.

'''
class Example:
    def greet(self, name=None):
        if name is None:
            print("Hello!")
        else:
            print(f"Hello, {name}!")

# Usage
obj = Example()
obj.greet()           # Output: Hello!
obj.greet("Alice")    # Output: Hello, Alice!
'''
2. Using Variable-Length Arguments
You can use *args and **kwargs to accept a variable number of arguments,
 which allows for more flexible method signatures.

'''
class Example:
    def add(self, *args):
        return sum(args)

# Usage
obj = Example()
print(obj.add(1, 2))          # Output: 3
print(obj.add(1, 2, 3, 4, 5)) # Output: 15
'''
3. Using Type Checking
You can manually handle different types or numbers of arguments within
 a single method by using type checking.


'''
class Example:
    def process(self, data):
        if isinstance(data, str):
            print(f"Processing string: {data}")
        elif isinstance(data, int):
            print(f"Processing integer: {data}")
        else:
            print("Unsupported type")

# Usage
obj = Example()
obj.process("hello")   # Output: Processing string: hello
obj.process(42)        # Output: Processing integer: 42
'''
4. Using Function Overloading Libraries
For more advanced use cases, you can use libraries like functools or 
multipledispatch to provide method overloading capabilities.

'''
from multipledispatch import dispatch

class Example:
    @dispatch(int)
    def process(self, data):
        print(f"Processing integer: {data}")

    @dispatch(str)
    def process(self, data):
        print(f"Processing string: {data}")

# Usage
obj = Example()
obj.process("hello")   # Output: Processing string: hello
obj.process(42)        # Output: Processing integer: 42
'''

In summary, while Python does not support method overloading in the traditional sense,
 you can use various techniques to achieve similar outcomes based on your requirements.



'''