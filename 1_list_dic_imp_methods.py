#n, m = map(int, input().split()) #importent remmeber
#' '.join(map(str, group_A[word])))
#return a==b
#vowel_indices = [i for i, char in enumerate(s_list) if char in vowels] if you want 
# indexes please take enumerate
'''
Introduction to List
Purpose of a List
Iterating through a List
List slicing, -ve indexing
Internals of list
List Operations
Searching for an element
In and count()
Adding an element
append()
insert()
Removing an element
remove()
pop()
Merging two lists
+ operator
extend()
Ordering a list
sort()
reverse()
Finding index of an element - index()
List of lists
Comparing list

'''
s='#!Hello, I am srinivas, I have two friends#! '
print(s.split())
#['Hello,', 'I', 'am', 'srinivas,', 'I', 'have', 'two', 'friends']
print(s.strip('#! '))
#Hello, I am srinivas, I have two friends
# A = list(map(int, input().split()))
s2=['q',1,2,3,4,5,'w']
print(s2.append('a'))
print(s2)
#[1, 2, 3, 4, 5, 'w', 'a']

print(s2.extend(["b","c"]))
print(s2)
#[1, 2, 3, 4, 5, 'w', 'a', 'b', 'c']
s2.insert(2, 2.1)
print("# s2=", s2)
# s2= ['q', 1, 2.1, 2, 3, 4, 5, 'w', 'a', 'b', 'c']

for index, value in enumerate(s2):
    print(index,'=', value, end=' ')
#0 = q 1 = 1 2 = 2 3 = 3 4 = 4 5 = 5 6 = w 7 = a 8 = b 9 = c #!Hello,

list1= s.split()
for x in list1:
    print(x)

ss= ' '.join(list1)
print(ss)
#!Hello, I am srinivas, I have two friends#!


s3={1:"a",2:"b"}
print(s3.get(1))
#a
print(s3)
print(s3.update({3:"c", 4:'d'}))
print(s3)
#{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
s3[5]='e'
print("adding new value", s3)
#{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
s3[1]='e'
print("changing value",s3)
#{1: 'e', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

for key,value in s3.items():
    print(key,'=', value, end=' ')

#1 = e 2 = b 3 = c 4 = d 5 = e 1

for key in s3.keys():
    print(key)
list1= [0,1,2,3,4]
list_1= list1[1:2]
list2= list1[:-1]  
print(list2)  
list3 = list1[:2]
print(list3)

my_list = [1, 2, 3, 4]
last_item = my_list.pop()
# Output: last_item = 4, my_list = [1, 2, 3]

specific_item = my_list.pop(1)
# Output: specific_item = 2, my_list = [1, 3]
my_list = [1, 2, 3, 4, 3]
count = my_list.count(3)
# Output: count = 2
z=my_list.pop()
print(z, my_list)

z2= my_list*3
print('#z2 is = ',z2)
#z2 is =  [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
#assert z2 == [1, 2, 3, 4, 1, 2, 3, 4, 2, 4]
list_1 = [1, 2, 3, 4, 'a', 'b']

# Extract only the character elements
for item in list_1:
    if isinstance(item, str):
        print(item)        
# Output: ['a', 'b']
for item in list_1:
    if type(item)== int:
        print(item)

'''
Extend vs. Append
Extend and append are both list methods. They both add 
elements to an existing list. The append() method adds one (1) 
item to the end of the list, whereas the append() method does 
not. The extend() method adds multiple items to the end of the 
list. Below, we use the append() method to append numbers2
to numbers1. You can see that the whole list of numbers2 has 
been appended to numbers1 as one (1) item.
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
# using append method
numbers1.append(numbers2)
print(numbers1)
Output: 
[1, 2, 3, [4, 5, 6]]
When we use the extend() method, notice the difference from
the append() method above. The extend() method takes the 
elements in number2, and appends them to numbers1, one 
item at a time, not as a whole list. See below:
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
# using extend method
numbers1.extend(numbers2)
print(numbers1)
Output: 
[1, 2, 3, 4, 5, 6]

'''



#Dictionary
#update(),get()   
#https://aigents.co/learn/merging-dictionaries-in-python
dic={'a':[1,2,3],'b':[4,5,6]}
print('# dic[b][1]=, dic[b]',dic['b'][1], dic['b'])
# dic[b][1]=, dic[b] 5 [4, 5, 6]
for k,v in dic.items():
    if v==[1,2,3]:
        print(key)
dic.update({'city': 'New York', 'job': 'Engineer'})        
#dic.update({'c':[7,5,6], 'd':[8,9,1]})
print(dic)
dic['d3']=[11,12,13]
print("#dic=", dic)

nested_dic={1:{'city':'new york','job':'engineer'},2:{'city':'vijayawada','job':'pythondev'}}
print("#nested_dic", nested_dic)

nested_dic_2={
    1:'a',
    2:{
        'b':'@'

    },
    3:'c'
}
print(nested_dic_2)

#Q1) how to reverse the key and vlue in dictionary        
'''
len= int(input())
list_1=list(map(int, input().strip().split()))
print(list_1)
n = int(input())
list_1 = list(map(int, input().strip().split()))[:n]


for _ in range(int(input())):
        name = input()
        score = float(input())



stu, sub= input().split()
print(sub,stu)
marks=[]
for i in range(int(stu)):
    mark=map(float, input().split())
    marks.append(marks)        
'''
list1=[1,2,3,4]
list2=["a","b","c","d"]
zipped= zip(list1,list2)
print("# list zipped = ",list(zipped))
#list zipped =  [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
zipped= zip(list1,list2)
print("# dic zipped =",dict(zipped))

list1=[1,2,3,4]
list2=["a","b","c","d"]
zipped= zip(list1,list2)
list3, list4 = zip(*zipped)

print(list3)  # Output: (1, 2, 3)
print(list4)  #
#print("# dic zipped =",dict(zipped))



matrix = [[3,7,8],[9,11,13],[15,16,17]]
def luckyNumbers(matrix):
    # Step 1: Find the minimum in each row
    row_mins = {min(row) for row in matrix}
    
    # Step 2: Find the maximum in each column
    col_maxs = {max(col) for col in zip(*matrix)}
    
    # Step 3: Return the intersection of row_mins and col_maxs
    return list(row_mins & col_maxs)

print(luckyNumbers(matrix))

'''
Simplify Python Dictionary Merging!


Why choose | over ** or .update()?


When merging dictionaries,
the | operator (introduced in Python 3.9)
is usually the best approach.


Here's why:


➟ Concise & Readable:

▸ Forget about clunky syntax. 

▸ merged = dict1 | dict2 is clean and intuitive.



➟ Non-Destructive:

▸ Unlike .update(), which modifies the first dictionary,
| creates a new dictionary, 
leaving your original data untouched.



➟ No Workarounds:

▸ ** unpacking works but adds verbosity.



What's your go-to method for 
merging dictionaries in Python?

'''

