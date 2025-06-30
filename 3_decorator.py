'''

A decorator is a special type of higher-order function that takes a function as an argument and
returns a new function with additional behavior. 
All decorators are higher-order functions, but not all higher-order functions are decorators.

Decorator is just a function that takes another function as an argument, add some 
kind of functionality and then returns another function.
All of this without altering the source code of the original function
that you passed in.

a decorator is a design pattern that allows you to modify or enhance
the behavior of a function or method without changing its code. 
Decorators are commonly used to add "wrapping" functionality to 
existing functions or methods.

Common Uses of Decorators
Logging: Track function calls and outputs.
Authentication: Verify user permissions before executing a function.
Caching: Store results of expensive function calls and reuse them.
Validation: Check inputs or outputs to ensure they meet certain criteria.
'''

def dev(func):
    def inner(x,y): #what are the parameters mentioned in original function, we can mention that parameters here
        if y==0:
            print("give proper input")
            x,y=y,x
        return func(x,y)
    return inner    
@dev
def division(a,b):
    return a/b
print(division(3,0))

#takes a function as an argument
def uppercase(func):
    #wrapper function to keep the
    #original function code unchanged
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper
# define greet function
def greet():
    return "Hello, how are you?"

greet_upper = uppercase(greet)
print(greet_upper())

def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello, {name}!")


greet("Alice")
#It's a good practice to use *args and **kwargs in the signature of a wrapper 
# function within a decorator. 
#This approach ensures that the decorator is versatile and can be applied to any 
# function, regardless of the number and type of its arguments.

#Code a wrapper function signature with args and kwargs
'''
def some_decorator(func):
  def wrapper(*args, **kwargs)

'''

'''
 Advanced Python Decorators Interview Questions
✅ Conceptual Understanding
What is a Python decorator? How does it differ from a higher-order function?

Can a decorator return something other than a function? Explain with an example.

How do decorators maintain the metadata (like docstring and function name) of the original function?

What is functools.wraps and why is it important in custom decorators?

What is the difference between a decorator and a context manager in Python?

⚙️ Implementation & Practical Usage
Write a decorator that measures the execution time of a function.

Implement a retry decorator that retries a function 3 times if it fails.

Create a decorator that accepts arguments (e.g., a logging level) and logs accordingly.

How do you write a decorator that can be used both with and without arguments?

Write a decorator to limit the number of times a function can be called.

🔁 Chaining and Nesting Decorators
What happens when multiple decorators are applied to a function? In what order are they executed?

Write a function with two decorators and show the order in which they are applied.

How do you ensure the decorators are reusable and modular across a large codebase?

📦 Class-based and Method Decorators
How would you write a class-based decorator? What are the advantages?

Can decorators be applied to class methods and static methods? Show with an example.

What are the differences between using a class-based decorator and a function-based decorator?

How do you write a decorator that modifies a class's behavior or attributes?

🧪 Use Cases in Testing & Automation
Write a decorator that automatically retries a flaky WiFi test case with exponential backoff.

Design a decorator to log test case names and their outcomes in a custom test framework.

Implement a decorator to skip test execution based on a hardware flag or condition.

🔄 Decorator Internals and Pitfalls
Explain the closure mechanism in decorators. How does it help preserve state?

What issues might arise from using decorators in multithreaded applications?

Can a decorator change the signature of a function? What are the implications?

Is it possible to remove a decorator once applied to a function? Explain.

How would you debug a decorator when something goes wrong inside the wrapper?

'''
def song_name(name):
  return "Song name: " + name
def info(name, func):
  print(func(name))

print("Hallelujah", song_name)

def order():
  def prepare():
    return "Your meal is being prepared!"
  status = prepare()
  return status

order()
def greet():
    return "Welcome!"


def checkname(func):
    def inner(ref):
        if ref.name=='srinu':
            print("you are allowed to access the function")
        else:
            return func(ref)
    return inner    
#decorator in class

class Printing:
    def __init__(self, name):
        self.name= name
     
    @checkname
    def print_name(self):
        print("enter name is ", self.name)    
obj=Printing("srinu")
obj.print_name()        
         