''' 

 List comprehension is a concise way to create lists in Python based on 
existing lists or other iterables. It combines the creation of a new list with a 
loop and optional conditional statements  

'''
'''
List comprehensions in Python provide a concise way to create lists. 
They offer a syntactically elegant way to generate lists using a 
single line of code, applying an expression to each item in an 
iterable, optionally filtering elements with a condition.
'''
z = [x for x in range(10)]
print("#",z)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

square= [x*x for x in z]
print("#", square)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

even_squres= [x*x for x in z if x%2==0]
print("#",even_squres)
# [0, 4, 16, 36, 64]

y = [[1,2,3],[ 4,5,6],[7,8,9]]

flat_list= [item for sub_list in y for item in sub_list]
print("# flat_list =", flat_list)
# flat_list  = [1, 2, 3, 4, 5, 6, 7, 8, 9]

dict_1 = {x:x*x for x in range(10)}
print("# dict_1",dict_1)
# dict_1 {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

square_set= {x*x for x in range(10)}
print("# square_set",square_set)
# square_set {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

numbers = [1, 2, 3, 4, 5]
result = ['Even' if x % 2 == 0 else 'Odd' for x in numbers]
# Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

numbers = [1,2,2,3,4,5,5]
uniq_list= [x for i, x in enumerate(numbers) if x not in numbers[:i]]
print(uniq_list)

numbers = [1, 2, 2, 3, 4, 4, 5, 6]
unique_evens = [x for i, x in enumerate(numbers) if x not in numbers[:i] and x % 2 == 0]
# Output: [2, 4, 6]


pairs=[(x, y) for x in range(3) for y in range(3)]
print("#",pairs)
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(transposed)

'''
Key Points:
Keys must be immutable: Data types like strings, numbers, and tuples can be used as 
keys, but lists and other dictionaries cannot.
Dictionary keys are unique: If you add a duplicate key, the last value associated 
with that key will overwrite the previous value.

'''
