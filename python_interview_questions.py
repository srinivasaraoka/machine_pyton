'''  Auther: Srinivas '''
#difference between sleep and time.sleep()

#1,what is MRO in python
# MRO stands for Method Resolution Order. It is the order in which Python looks for a method in a hierarchy of classes. 
# Python uses the C3 linearization algorithm to determine the MRO, which ensures a consistent and predictable method resolution order.

#2,what is the difference between classmethod and staticmethod in python
# A class method takes cls as the first parameter, which refers to the class itself. It can access or modify class-level variables and is often used for factory methods or alternative constructors.
# A static method, on the other hand, does not take any special first parameter (like self or cls). It behaves like a regular function but belongs to the class's namespace. Static methods cannot access or modify class or instance variables.    

#3,what is the difference between a shallow copy and a deep copy in python
# A shallow copy creates a new object, but inserts references into it to the objects found in the original. In contrast, a deep copy creates a new object and recursively adds copies of nested objects found in the original, resulting in a completely independent clone.         

#4,what is the difference between a list and a tuple in python
# A list is mutable, meaning you can change its elements after it has been created. A tuple, on the other hand, is immutable, meaning its elements cannot be changed once it is created. Tuples are typically used for fixed collections of items that should not be modified.      

#5,what is the difference between a set and a frozenset in python
# A set is mutable, meaning you can add or remove elements from it after it has been created. A frozenset, on the other hand, is immutable and cannot be changed once it is created. It is useful when you need a fixed set of elements that should not be modified.    

#6,what is the difference between a dictionary and a defaultdict in python
# A dictionary is a built-in data structure that stores key-value pairs, while a defaultdict is a subclass of the dictionary that allows you to specify a default value for keys that do not exist. When you try to access a non-existent key in a defaultdict, it will create the key and assign it the default value. 

#7,what is the difference between a list and a dictionary comprehension in python
# A list comprehension is used to create a new list by applying an expression to each item in an existing list, while a dictionary comprehension is used to create a new dictionary by applying an expression to each key-value pair in an existing dictionary. 

#8,what is the difference between a generator and a list in python
# A generator is a special type of iterator that allows you to iterate over a sequence of items without storing them all in memory at once. It is created using a function with the yield keyword, which returns a value each time the function is called. In contrast, a list stores all its elements in memory, which can be inefficient for large datasets.  

#9,what is the difference between a decorator and a context manager in python
# A decorator is a function that modifies the behavior of another function, typically by wrapping it in additional functionality. It is used to add functionality to existing functions without changing their code. A context manager, on the other hand, is used to manage resources by defining setup and cleanup actions that are executed before and after a block of code. It is implemented using the with statement and the __enter__ and __exit__ methods. 

#10,what is the difference between a module and a package in python
# A module is a single file that contains Python code, while a package is a directory that contains multiple modules and an __init__.py file. Packages allow you to organize related modules into a hierarchy, making it easier to manage and reuse code.

#11,what is the difference between a class and an object in python
# A class is a blueprint for creating objects, while an object is an instance of a class. Classes define the structure and behavior of objects, while objects are specific instances of those classes with their own unique state and behavior.

#12,what is the difference between a class and a module in python
# A class is a blueprint for creating objects, while a module is a file that contains Python code, typically related to a specific functionality or set of functions. Modules can contain classes, functions, and variables that can be imported and used in other Python files.

#13,what is the difference between a class and a function in python
# A class is a blueprint for creating objects, while a function is a block of reusable code that performs a specific task. Classes define the structure and behavior of objects, while functions encapsulate logic and can be used to perform operations on data.

#14,what is the difference between a class and a method in python
# A class is a blueprint for creating objects, while a method is a function that is defined within a class and operates on objects created from that class. Methods are used to define the behavior of objects and can access and modify the object's state.

#15,what is the difference between a class and a variable in python
# A class is a blueprint for creating objects, while a variable is a container that stores data. Classes define the structure and behavior of objects, while variables can be used to store and manipulate data within a class or an object.    

#16,what is the difference between a class and an instance in python
# A class is a blueprint for creating objects, while an instance is a specific object created from that class. Classes define the structure and behavior of objects, while instances are individual objects with their own unique state and behavior.   

#17, what is constructor and destructor in python
# A constructor is a special method that is called when an object is created. It is used to initialize the object's state and set up any necessary resources. In Python, the constructor is defined using the __init__ method. A destructor, on the other hand, is a special method that is called when an object is destroyed or goes out of scope. It is used to clean up any resources that the object may have acquired during its lifetime. In Python, the destructor is defined using the __del__ method.

#18, reverse words in string using the python 

#19, what are the different ways to remove duplicates from a list in python
# There are several ways to remove duplicates from a list in Python:
# 1. Using a for loop and a temporary list
# 2. Using a set to store unique elements
# 3. Using dictionary keys (since keys are unique)
# 4. Using list comprehension   

#20 what are the data types in python
# Python has several built-in data types, including:
# 1. int (integer): whole numbers without a decimal point
# 2. float (floating-point number): numbers with a decimal point
# 3. str (string): sequences of characters
# 4. list: ordered collections of items
# 5. tuple: immutable ordered collections of items
# 6. dict (dictionary): unordered collections of key-value pairs
# 7. set: unordered collections of unique items
# 8. bool (boolean): represents True or False values
# 9. NoneType: represents the absence of a value (similar to null in other languages)
# 10. bytes and bytearray: used to store binary data
# 11. complex: numbers with a real and imaginary part   

#21, extract ip from the string using the python
# import re
# def extract_ip(string):   
#     ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', string)
#     if ip:    
#         return ip.group()
#     else:     
#         return "No IP found"
# string = "This is a sample string with an IP address 192.168.1.1"
# print(extract_ip(string)) 

#22, what is a class variable in python, why we need to use it
# A class variable is a variable that is shared among all instances of a class. It is defined within the class but outside any method.
# Class variables are used to store data that is common to all instances of the class, such as configuration settings or shared resources.
# They are accessed using the class name rather than the instance name. Class variables can be used to maintain state across all instances of a class and to share data between different instances.

#23, what is a class method in python, how is it different from an instance method
# A class method is a method that is bound to the class itself, rather than to any specific instance of the class. It is defined using the @classmethod decorator and takes a special first parameter cls, which refers to the class itself.

#24, what is polymorphism in python
# Polymorphism is the ability of an object to take on different forms or behaviors depending on the context. In Python, polymorphism is achieved through method overriding, where a subclass can provide a specific implementation of a method that is already defined in its superclass. This allows objects of different classes to be treated as instances of a common superclass and to respond to the same method call in different ways.

#25, get the bluetooth adderess form the string using the python
# import re     
# def extract_bluetooth_address(string):
#     mac = re.search(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', string)
#     if mac:
#         return mac.group()
#     else:
#         return "No Bluetooth address found"
# string = "This is a sample string with a Bluetooth address 00:1A:7D:DA:71:13"
# print(extract_bluetooth_address(string))

#25, reverse the list with out using the reverse function
# list1=[1,2,3,4,5]     
# list2=[]
# for i in range(len(list1)-1,-1,-1):
#     list2.append(list1[i])    

# print(list2)

#26, what is subprocess in python
# The subprocess module in Python allows you to spawn new processes, connect to their 
# input/output/error pipes, and obtain their return codes. It provides a high-level interface
# for executing shell commands and managing child processes. The subprocess module is used to
# create new processes, connect to their input/output/error streams, and obtain their return 
# codes. It provides a more flexible and powerful way to work with external programs compared 
# to the os.system() and os.popen() functions.
subprocess.run(["ls", "-l"])  # Run the command "ls -l"
# The subprocess module provides several functions for different use cases:
# 1. subprocess.run(): Runs a command and waits for it to complete.
# 2. subprocess.Popen(): Executes a command in a new process and allows for more complex interactions.
# 3. subprocess.call(): Runs a command and returns its return code.
# 4. subprocess.check_output(): Runs a command and returns its output.
