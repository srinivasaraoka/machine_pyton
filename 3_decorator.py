'''
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

def song_name(name):
  return "Song name: " + name
def info(name, func):
  print(func(name))

info("Hallelujah", song_name)

def order():
  def prepare():
    return "Your meal is being prepared!"
  status = prepare()
  return status

order()
def greet():
    return "Welcome!"

#takes a function as an argument
def uppercase(func):
    #wrapper function to keep the
    #original function code unchanged
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper

greet_upper = uppercase(greet)
print(greet_upper())

def dev(func):
    def inner(x,y):
        if y==0:
            print("give proper input")
            x,y=y,x
        return func(x,y)
    return inner    

@dev
def division(a,b):
    return a/b
print(division(3,0))


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