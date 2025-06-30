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
#sign = 1 if char == '+' else -1

x = [1, 2, 3] 
y = x # Both x and y reference the same list object in memory 
resultl =x is y # True, as they reference the same obj ect 
result2 = x == y # True, as their contents are equal 
z = [1, 2, 3] # A new list object with the same contents 
result3 = x is z # False, as they are different objects with the same

some_variable = None 
if some_variable is None: 
    print("The variable is None. ")
    
import copy 
original_list = [1, 2, [3, 4 ] ] 
copied_list = copy .copy (original_list) 
original_list[2] [0] = 99 
print(original_list ) # [l, 2, [99, 4]] 
print(copied_list) # [1, 2, [99 , 4 ] ] 
#Deep Copy with copy.deepcopy(): 
import copy 
original_list = [1, 2, [3, 4]] 
deep_copied_list = copy.deepcopy(original_list) 
original_list[2][0] = 99 
print(original_list) 
print(deep_copied_list) 
# [ 1, 2, [ 99, 4 ] ] 
# [1, 2, [3, 4 ] ] 
#Deep Copy with copy.deepcopy(): 
original_list = [1, 2, 3] 
copied_list = original_list[:] 
original_list[0] = 99 
print(original_list) # Output: [99, 2, 3] 
print(copied_list) # Output: [l, 2, 3]    