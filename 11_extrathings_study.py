'''  Auther: Srinivas '''

'''
When you are not clear how many arguments you need to pass to a particular function, 
then we use *args and **kwargs.
The *args keyword represents a varied number of arguments. It is used to add together 
the values of multiple arguments
The **kwargs keyword represents an arbitrary number of arguments that are passed to a 
function. **kwargs keywords are stored in a dictionary. You can access each item by 
referring to the keyword you associated with an argument when you passed the argument.

Pickling:
In python, the pickle module accepts any Python object, transforms it into a string representation, and dumps it into a file by using the dump function. This process is known as pickling. The function used for this process is pickle.dump()
Unpickling:
The process of retrieving the original python object from the stored string representation is called unpickling. The function used for this process is pickle.load()
            - They are inverses of each other.
- Pickling, also called serialization, involves converting a Python object into a series of bytes which can be written
out to a file.
- Unpicking, or de-serialization, does the opposite–it converts a series of bytes into the Python object it represents.


'''