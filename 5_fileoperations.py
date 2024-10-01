import os
print(os.getcwd())
file_path = os.path.expanduser("~//Desktop//python_training//1_mymath//11_extrathings_study.py")
#directory = os.path.dirname(file_path)
#os.makedirs(directory, exist_ok=True)
text_file = open(file_path,'w')
text_file.write("'''  Auther: Srinivas '''")
text_file.close()

text_file = open("text.txt",'w')
text_file.write("hello pedddople \n www")
text_file.close()

text_file= open('text.txt','rb')
#print(text_file.readlines())
'''
It is good programming habit to use the with keyword when working with file objects.
This has the advantage that the file is properly closed after it is used even if 
an error occurs during read or write operation or even when you forget to explicitly
 close the file.
'''
with open('text.txt', 'r+') as text_file:
    print(text_file.read())

# how to find the numbers files given dictionny(sub dictionary also)