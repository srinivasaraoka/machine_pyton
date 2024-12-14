'''
Sometimes we can declare a function without any name,such type of 
nameless functions  are called anonymous functions or lambda functions.


Syntax of lambda Function: lambda argument_list:expression
lambda n:n*n

Note: By using Lambda Functions we can write very concise code so that 
readability of the program will be improved.


A lambda function is an anonymous function defined 
using the lambda keyword. It is typically used for short, one-line functions.

*we can not add for loop in lambda 
'''
import sys

s = lambda a:a**2

s= (lambda a,b:a**b)(2,3)
print(s)
def mult(n):
  return lambda a : a * n

doubler = mult(2)
tripler = mult(3)

print(doubler(5))
print(tripler(5))

s=lambda a,b:a if a>b else b 

student_records=[(1, 'Charlie', 19, (90, 95, 88)), (2, 'Alice', 20, (185, 90, 92)), (3, 'Bob Smith', 21, (78, 80, 85, 88))]
sorted_students = sorted(student_records, key=lambda student: sum(student[3]) / len(student[3]), reverse=True)


key= lambda student: sum(student[3]) / len(student[3])
for student_record in student_records:
    
    print(key(student_record))


#map
'''
#map(function, iterable)
#The map function takes two arguments - an iterable and… function

#The map function requires the first argument to be a function and the second argument 
# to be an iterable.

#Do you remember lambda expressions? Another valuable aspect of them is their ability 
to be directly provided to the map function. This eliminates the need to define a 
regular function explicitly.
The map() function applies a specified function to every element in an iterable, 
like lists or tuples. It produces a result that can be transformed into a list using 
the list() function for easy viewing or further use.

'''   
numbers = [1, 2, 3]

doubled = list(map(lambda x: x*2, numbers))

print(doubled) 
#List of names in various cases
names = ["alice", "bob", "CHARLIE", "dEborah"]

# Function to capitalize each name
def capitalize(name):
  return name.capitalize()

# Using map() to apply the capitalization to each name
capitalized = map(capitalize, names)

# Converting map object to a list
capitalized = list(capitalized)

print("#caplitalized is ",capitalized)
#caplitalized is  ['Alice', 'Bob', 'Charlie', 'Deborah']



#The code below has a mistake. Can you fix it?

exam_scores = [85, 62, 95, 40, 78]
def is_passing(score):
  return score >= 70

status = list(map(exam_scores,is_passing))

print(status)

#filetr
'''
The filter() function, just like the map() function, 
takes in a function and an iterable as arguments. The key purpose of filter() is to 
apply a condition specified in the provided function to each item in the iterable 
and return only those for which the function evaluates to True.

This code filters and returns products with names 4 characters long.
'''
products = ["Table", "Sofa", "Cushion", "Bookshelf", "Vase"]

# Filters products with name length equal to 4
filtered_prod = list(filter(lambda name: len(name) == 4, products))

print(filtered_prod)
#transforms the items of an iterable:map()
#returns items that meet a condition:fileter()
# The map() function applies a specified function to every element in an iterable

#
#  The filter() function filters out items from an iterable based on a specified condition

# Both can accept lambda expressions as arguments
# Enter your code here. Read input from STDIN. Print output to STDOUT


# Read all the input at once
input_data = sys.stdin.read().splitlines()

# Extract the first line to get `n` (number of students) and `x` (number of subjects)
n_stu, x_sub = map(int, input_data[0].split())
#print(n_stu,x_sub)

# Initialize an empty list to store marks of all subjects
marks = []

# Extract marks for each subject from the remaining lines
for i in range(1, x_sub + 1):
    marks.append(list(map(float, input_data[i].split())))

#print(marks)
stu_marks=zip(*marks)
#print(list(stu_marks))
for stu in stu_marks:
    avarage= sum(stu)/x_sub
    print(avarage)


# Sample list of user answers (some are empty strings)
user_answers = ["answer1", "", "answer2", " ", "answer3", ""]

# Use filter() with a lambda function to exclude empty or whitespace-only strings
cleaned_answers = list(filter(lambda x: x.strip() != "", user_answers))

# Display the new cleaned list of answers
print(cleaned_answers)

#Write a map function that adds 10 to each item in the iterable scores

map(lambda x: x+10,scroes)

#Complete the code to filter out values from the ages list that are less than 30

filter(lambda age:age< 30, ages)

  

