'''  Auther: Srinivas '''

import os
'''
SyntaxError(print("hello))                       Incorrect syntax: 
NameError(name="Anna", print(age))               The variable is not defined:
IndexError(a=[1,2] print(a[5]))                  Out-of-range index: 
TypeError(len(5))                                Incorrect type of an argument: 
ValueError:(int("hello"))                        Inappropriate value: 
  
Exception handling in Python is a mechanism used to handle runtime errors, 
ensuring that a program can continue running smoothly even when unexpected events occur.
An exception is an error that occurs during the execution of a program, and exception 
handling provides a way to respond to these errors gracefully, rather than crashing 
the program.

try:
    # Code that might raise an exception
except SomeException as e:
    # Code to handle the exception
else:
    # Optional: Code that runs if no exceptions occur
finally:
    # Optional: Code that runs whether or not an exception occurred

'''
try:
    str1= len(10)
    print(str1)
except TypeError:
    print("#error")
finally:
    print("#sytex error")   
print("#hi")
#error
#sytex error
#hi

   
'''            
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print("File read successfully.")
    finally:
        print("File handling operation completed.")

# Example usage
read_file("2_1_set.py")  # Existing file
read_file("non_existent_file.txt")  # Non-existent file
read_file("/restricted_access_file.txt")  # File with restricted access
print("Continuing with the rest of the program...")
file_path = os.path.expanduser("~//Desktop//python_training//1_mymath//9_excepationhandling.py")
#directory = os.path.dirname(file_path)
#os.makedirs(directory, exist_ok=True)
text_file = open(file_path,'w')
text_file.write(" Auther: Srinivas ")
text_file.close()

#The else statement can be used in conjunction with the try/except block and will execute only when no error occurs in the try block.
#You can trigger your own exceptions based on specific conditions using the raise statement. This will immediately stop the program's execution and indicate an error has occurred.
'''
def check_value(value):
    if value < 0:
        raise ValueError("Value must be positive!")
    return value

try:
    check_value(-5)
except ValueError as e:
    print(e)



try:
    str1= len(10)
    print(str1)
except ValueError as e:
    print("error1",e)
  
finally:
    print("sytex error2")   
#sytex error2
print("hi2") # must declare TypeError otherwise this print wont execute
