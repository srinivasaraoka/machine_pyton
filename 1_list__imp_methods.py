import logging
import logger

#logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("custom_logger")
#list.index(element, start, end)
#for x in range(len(nums)-1, -1, -1) # reverse loop
#for index, value in enumerate(nums): # index and value both
#for i in range(0, len(nums), 2): # step 2      

list1=['a','b','c','d']
print(list1.index('c'))
#n, m = map(int, input().split()) #importent remmeber
#min_index = list1.index(min_value, i)

#' '.join(map(str, group_A[word])))
#return a==b
#vowel_indices = [i for i, char in enumerate(s_list) if char in vowels] if you want 
# indexes please take enumerate
#lst.count(x) 
#rotated = lst[-k:] + lst[:-k] 
#[x+y for x,y in zip(lst1, llst2)]
#is_all_positive = all(x > 0 for x in lst) # True
#is_any_negative = any(x < 0 for x in lst) # True
#is_sorted = lst == sorted(lst)
# list1.sort()
#list2= sorted(list1, key=abs) # [1, -2, -3, 4]
#list1.sort(reverse=True)
#d = dict(zip(a, b)) a, b = zip(*pairs)
#y=z.split(".")
'''
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
lst = [1, 2, 3, 4, 5]
k = 2
rotated = lst[-k:] + lst[:-k] 
'''
18. Find Duplicates
lst = [1, 2, 2, 3, 4, 4]
duplicates = list({x for x in lst if lst.count(x) > 1})
19. Convert List of Strings to Integers
lst = ['1', '2', '3']
nums = list(map(int, lst))

'''
lst=[1,2,3]
print(len(lst), lst.append([4, 51]), lst.append(5), lst.extend([6,7,8]), 'lst.extend(9) no support')
print(len(lst), lst)

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
print(s2.append(["#","!"]))
print(s2,"=s2")
print(s2.extend(["b","c"]))
print(s2,"s2")
#[1, 2, 3, 4, 5, 'w', 'a', 'b', 'c']
s2.insert(2, 2.1)
print("# s2=", s2)
# s2= ['q', 1, 2.1, 2, 3, 4, 5, 'w', 'a', 'b', 'c']

for index, value in enumerate(s2):
    print(index,'=', value, ",",end=' ')
#0 = q 1 = 1 2 = 2 3 = 3 4 = 4 5 = 5 6 = w 7 = a 8 = b 9 = c #!Hello,

list1= s.split()
for x in list1:
    print(x)

ss= ' '.join(list1)
print(ss)
#!Hello, I am srinivas, I have two friends#!

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

matrix = [[3,7,8],[9,11,13],[15,16,17]]
def luckyNumbers(matrix):
    # Step 1: Find the minimum in each row
    row_mins = {min(row) for row in matrix}
    
    # Step 2: Find the maximum in each column
    col_maxs = {max(col) for col in zip(*matrix)}
    
    # Step 3: Return the intersection of row_mins and col_maxs
    return list(row_mins & col_maxs)

print(luckyNumbers(matrix))

# def flatne_dci(input_dic, parent_key=''):
#     flattend={}

#     dic= input_dic
    
#     for key,value in dic.items():
#         # if parent_key:
#         #     new_key=f'{parent_key}.{key}'
#         # else:
#         #     new_key=key
#         new_key=f"{parent_key}.{key}" if parent_key else key
#         if isinstance(value,dict):
#             flattend.update(flatne_dci(value, new_key))
#         else:
#             flattend.update(flatne_dci(new_key, value))            
#     return flattend




# input_dic={'a':1,'b':{"c":2,"d":{'e':3}}}    
# print(flatne_dci(input_dic))

a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)
c='123'
d='123'
print(c==d)
print(c is d)
logging.info(type(a))
logging.info(type(b))


'''

Here are some advanced-level Python list coding interview questions with solutions:

1. Rotate a List by K Positions
Problem: Given a list and an integer k, rotate the list to the right by k places.

#
#
#
def rotate_list(lst, k):
    k %= len(lst)  # Handle cases where k > len(lst)
    return lst[-k:] + lst[:-k]

# Example
print(rotate_list([1, 2, 3, 4, 5], 2))  # Output: [4, 5, 1, 2, 3]
2. Find the Second Largest Element in a List
Problem: Given a list of numbers, find the second largest element.

#
#
#
def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

# Example
print(second_largest([10, 20, 4, 45, 99, 99]))  # Output: 45
3. Flatten a Nested List
Problem: Given a list with nested lists, flatten it into a single list.

#
#
#
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Example
print(flatten([1, [2, 3], [4, [5, 6], 7], 8]))  
# Output: [1, 2, 3, 4, 5, 6, 7, 8]
4. Find All Pairs That Sum to a Target
Problem: Given a list and a target sum, return all pairs that add up to the target.

#
#
#
def find_pairs(lst, target):
    seen = set()
    pairs = []
    for num in lst:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

# Example
print(find_pairs([1, 2, 3, 4, 5, 6], 7))  
# Output: [(3, 4), (2, 5), (1, 6)]
5. Find the Majority Element in a List
Problem: Find the element that appears more than n/2 times in a list.

#
#
#
from collections import Counter

def majority_element(lst):
    count = Counter(lst)
    n = len(lst) // 2
    for key, value in count.items():
        if value > n:
            return key
    return None

# Example
print(majority_element([3, 3, 4, 2, 4, 4, 2, 4, 4]))  # Output: 4
6. Find the Longest Consecutive Sequence
Problem: Given a list, find the length of the longest consecutive sequence.

#
#
#
def longest_consecutive(lst):
    nums = set(lst)
    longest = 0

    for num in nums:
        if num - 1 not in nums:  # Start of a new sequence
            length = 1
            while num + length in nums:
                length += 1
            longest = max(longest, length)

    return longest

# Example
print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # Output: 4 (sequence: [1,2,3,4])
7. Check If a List Is a Palindrome
Problem: Check if a list reads the same forwards and backwards.

#
#
#
def is_palindrome(lst):
    return lst == lst[::-1]

# Example
print(is_palindrome([1, 2, 3, 2, 1]))  # Output: True
8. Remove Duplicates Without Using set()
Problem: Remove duplicates from a list while maintaining the original order.

#
#
#
def remove_duplicates(lst):
    seen = {}
    return [seen.setdefault(x, x) for x in lst if x not in seen]

# Example
print(remove_duplicates([1, 3, 2, 3, 4, 1, 5]))  
# Output: [1, 3, 2, 4, 5]
9. Merge Two Sorted Lists
Problem: Given two sorted lists, merge them into one sorted list.

#
#
#
def merge_sorted_lists(lst1, lst2):
    i = j = 0
    result = []
    
    while i < len(lst1) and j < len(lst2):
        if lst1[i] < lst2[j]:
            result.append(lst1[i])
            i += 1
        else:
            result.append(lst2[j])
            j += 1
    return result + lst1[i:] + lst2[j:]

# Example
print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  
# Output: [1, 2, 3, 4, 5, 6]
10. Find the Subarray with Maximum Sum (Kadane's Algorithm)
Problem: Find the contiguous subarray with the largest sum.

#
#
#
def max_subarray_sum(lst):
    max_sum = curr_sum = lst[0]
    
    for num in lst[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

# Example
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  
# Output: 6 ([4, -1, 2, 1])
Bonus: List Comprehension Challenge
Problem: Given a list, create a new list that contains only the even numbers squared.

#
#
#
lst = [1, 2, 3, 4, 5, 6, 7, 8]
result = [x**2 for x in lst if x % 2 == 0]
print(result)  # Output: [4, 16, 36, 64]
Summary
#	Question	Concept Covered
1	Rotate List	List Slicing
2	Second Largest Element	Sorting & Set
3	Flatten Nested List	Recursion
4	Find Pairs for Sum	Hashing
5	Majority Element	Hashing (Counter)
6	Longest Consecutive Sequence	Set Operations
7	Check Palindrome	Slicing
8	Remove Duplicates	Dictionary (Order Preservation)
9	Merge Sorted Lists	Two-Pointer Technique
10	Max Subarray Sum	Kadane’s Algorithm
These questions will test your Python skills in list manipulation, algorithms, and efficiency. Let me know if you need more practice! 🚀

'''

def subsets(nums):
    result = [[]]
    for num in nums:
        print("num",num)
        
        result += [item + [num] for item in result]
        for iteam in result:
            print("iteam", iteam)
        print(result)
    return result

print(subsets([1, 2]))  # Output: [[], [1], [2], [1, 2]]




'''
1. Square of Even Numbers
squares = [x**2 for x in range(10) if x % 2 == 0]
2. Flatten a 2D List
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [item for row in matrix for item in row]
3. Remove Duplicates While Preserving Order
lst = [1, 2, 2, 3, 1]
unique = list(dict.fromkeys(lst)) # [1, 2, 3]
4. Intersection of Two Lists
a = [1, 2, 3]
b = [2, 3, 4]
common = list(set(a) & set(b)) # [2, 3]
5. Element-wise Addition Using zip()
a = [1, 2, 3]
b = [4, 5, 6]
sum_list = [x + y for x, y in zip(a, b)]
6. All Elements Positive
lst = [1, 2, 3]
is_all_positive = all(x > 0 for x in lst) # True
7. Any Element is Negative
lst = [1, -2, 3]
is_any_negative = any(x < 0 for x in lst) # True
8. Count Occurrences of Elements
lst = [1, 2, 2, 3, 3, 3]
counts = {x: lst.count(x) for x in set(lst)}
9. Sort List by Absolute Value
lst = [-3, 1, -2, 4]
sorted_list = sorted(lst, key=abs) # [1, -2, -3, 4]
10. Filter Only Integers
lst = [1, 'a', 2.5, 3]
Advanced Python String Logical Formulas
only_ints = [x for x in lst if isinstance(x, int)]
11. Nested List Comprehension (3x3 Matrix)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
12. Rotate List by k Steps
lst = [1, 2, 3, 4, 5]
k = 2
rotated = lst[-k:] + lst[:-k] # [4, 5, 1, 2, 3]
13. Flatten and Filter Even
lst = [[1, 2], [3, 4], [5, 6]]
evens = [x for sub in lst for x in sub if x % 2 == 0]
14. Running Sum
lst = [1, 2, 3, 4]
running_sum = [sum(lst[:i+1]) for i in range(len(lst))]
15. Remove None or Empty Strings
lst = [None, 'Python', '', 'AI']
cleaned = [x for x in lst if x]
16. Remove All Occurrences of a Specific Element
lst = [1, 2, 3, 2, 4]
lst = [x for x in lst if x != 2]
17. Check If List is Sorted
lst = [1, 2, 3]
is_sorted = lst == sorted(lst)
18. Find Duplicates
lst = [1, 2, 2, 3, 4, 4]
duplicates = list({x for x in lst if lst.count(x) > 1})
19. Convert List of Strings to Integers
lst = ['1', '2', '3']
nums = list(map(int, lst))
20. Filter Prime Numbers
Advanced Python String Logical Formulas
lst = list(range(2, 20))
primes = [x for x in lst if all(x % i != 0 for i in range(2, int(x**0.5)+1))]
21. Reverse List
lst = [1, 2, 3]
reversed_list = lst[::-1]
22. Zip Two Lists into Dictionary
a = [1, 2, 3]
b = ['a', 'b', 'c']
d = dict(zip(a, b))
23. Unzip List of Tuples
pairs = [(1, 'a'), (2, 'b')]
a, b = zip(*pairs)
24. Find Min and Max Without min()/max()
lst = [1, 4, 2]
min_val = sorted(lst)[0]
max_val = sorted(lst)[-1]
25. Check if All Elements are Same
lst = [1, 1, 1]
is_same = all(x == lst[0] for x in lst)
26. Remove Negative Numbers
lst = [-1, 2, -3, 4]
positives = [x for x in lst if x >= 0]
27. Pairwise Sum
lst = [1, 2, 3, 4]
pairs = [lst[i] + lst[i+1] for i in range(len(lst)-1)]
28. Transpose a Matrix
matrix = [[1, 2], [3, 4]]
transposed = [list(row) for row in zip(*matrix)]
29. Chunk List into Sublists
lst = [1,2,3,4,5,6]
chunked = [lst[i:i+2] for i in range(0, len(lst), 2)]
Advanced Python String Logical Formulas
30. Filter Palindrome Strings
lst = ['madam', 'apple', 'noon']
palindromes = [x for x in lst if x == x[::-1]]
31. Generate List of Factorials
import math
factorials = [math.factorial(x) for x in range(6)]
32. Difference Between Two Lists
a = [1, 2, 3]
b = [2, 4]
diff = list(set(a) - set(b))
33. List of Squares Using map
lst = [1, 2, 3]
squares = list(map(lambda x: x**2, lst))
34. Filter Unique Elements Only
lst = [1, 2, 2, 3, 3, 3]
unique = [x for x in lst if lst.count(x) == 1]
35. Multiply All Items
import math
lst = [1, 2, 3]
product = math.prod(lst)
36. Replace Specific Value
lst = [1, 2, 3]
lst = [0 if x == 2 else x for x in lst]
37. Create List with Range Steps
stepped = list(range(0, 20, 5))
38. Convert Nested List to Flat Set
lst = [[1,2],[2,3]]
flat_set = set(x for sub in lst for x in sub)
39. Get Index of All Matching Elements
lst = [1, 2, 3, 2]
Advanced Python String Logical Formulas
indices = [i for i, x in enumerate(lst) if x == 2]
40. Filter and Square Odd Numbers
lst = [1, 2, 3, 4, 5]
odds_squared = [x**2 for x in lst if x % 2 != 0]


'''
def merge_sorted(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    result += a[i:] + b[j:]
    return result

print(merge_sorted([1, 3, 5], [2, 4, 6]))  # [1, 2, 3, 4, 5, 6]
nums = [5, 3, 1]
new_list = sorted(nums)  # [1, 3, 5]
nums = [5, 3, 1]
nums.sort()  # nums becomes [1, 3, 5]
sorted(nums, reverse=True)
nums.sort(reverse=True)
lsit1=['a','b','c','d']
lsit1[3]= list1[2]
print(lsit1)
