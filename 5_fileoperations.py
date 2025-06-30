import os
print(os.getcwd())
with open('llbinarysearchtree.py', 'w') as text_file:
    text_file.write("auther:srinivas")
    pass

#file_path = os.path.expanduser("//Desktop//python_training//1_mymath//graph.py")
#file_path = os.path.expanduser("~//Desktop//python_training//1_mymath//ruff.py")
#directory = os.path.dirname(file_path)
#os.makedirs(directory, exist_ok=True)
text_file = open('C:\\Users\\kagsrini\\machine_pyton\\pytest_learning\\interviewquestions.py','w')
text_file.write("'''  Auther: Srinivas '''")
text_file.close()

text_file = open("text.txt",'w')
text_file.write("hello pedddople \n www")
text_file.close()

text_file= open('text.txt','rb')
#print(text_file.readlines())
'''
It is good programming habit to use the "with" keyword when working with file objects.
This has the advantage that the file is properly closed after it is used even if 
an error occurs during read or write operation or even when you forget to explicitly
 close the file.
'''
with open('LLbinarysearchtree.py', 'w+') as text_file:
    print(text_file.read())
    text_file.write("auther srinivas")

# how to find the numbers files given dictionny(sub dictionary also)

'''

 test_file.flush()


ChatGPT said:
The test_file.flush() method is used in Python to force the writing of buffered data to the file immediately.

✅ What flush() Does:
When you write to a file using Python, the data is usually first written to an in-memory buffer for performance. The flush() method clears this buffer and writes the data to

'''

import os 
# Specify the path to the file you want to delete 
file_path = "path/to/your/file . txt" 
# Check if the file exists before attempting to delete it 
if os. path . exists(file_path) : 
# Attempt to delete the file 
    try: 
        os.remove(file_path) 
        print(f" {file_path} has been deleted successfully . ") 
    except OSError as e: 
        print(f"Error deleting {file_path}: {e}") 
else: 
    print(f"{file_path} does not exist.")