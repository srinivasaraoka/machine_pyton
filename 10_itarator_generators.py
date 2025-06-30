'''  Auther: Srinivas '''
#genertor is like a list or tupple
'''
A generator is a special type of iterator that is defined using a function.
Instead of returning all values at once, it yields values one at a time, 
pausing execution and preserving the function’s state for each successive call.
This makes generators more memory-efficient when working with large datasets.

Generators are created using the yield keyword, which is similar to 
return but allows the function to be resumed later.

When a generator is called, it returns an iterator object that can be used to iterate 
over the values it yields.

Generators can be used in for loops, list comprehensions, and other contexts where iterators
are accepted.

They are particularly useful for processing large amounts of data or when you need to 
generate values on-the-fly.


An iterator in Python is an object that represents a stream of data — it returns one value at a time when you call next() on it.

A generator in Python is a special type of function or expression that returns an iterator,
which can be iterated one value at a time, using yield instead of return.

ITERATOR
● An iterator is an object which contains a countable number of values and it 
is used to iterate over iterable objects like list, tuples, sets, etc.
● Iterators are used mostly to iterate or convert other objects to an iterator using iter() function.
● Iterator uses iter() and next() functions.
● Every iterator is not a generator
● An iterator is an object which contains a countable number of values and it is 
used to iterate over iterable objects like list, tuples, sets, etc.
● Iterators are used mostly to iterate or convert other objects to an iterator 
using iter() function.
● Iterator uses iter() and next() functions.
● Every iterator is not a generator.
GENERATOR
● Generators are iterators which can execute only once.
● Generator uses “yield” keyword.
● Generators are mostly used in loops to generate an
iterator by returning all the values in the loop without
affecting the iteration of the loop.
● Every Generator is an iterator
 
EXAMPLE:
def sqr(n):
for i in range(1, n+1):
yield i*i a = sqr(3)
print(next(a)) print(next(a)) print(next(a))
Output:
1 4 9
ITERATOR

'''

def fabi():
    a, b= 0,1  
    while 1==1:
        yield a
        a, b= b, a+b
    
gen= fabi()
for x in range(10):
    print(next(gen))
    #print(next(fabi()))

list1=[1,2,3,4]
z=iter(list1)
print(z)
print(next(z))
print(next(z))

my_list = [1, 2, 3, 4, 5] 
# Create an iterator from the list 
iterator = iter(my_list) 
# Use the iterator to retrieve elements 
print(next(iterator) ) # Output : 1 
print(next(iterator) ) # Output : 2

def generator():
    yield 1
    yield 2
    yield 3

y=generator()
print(y)
print(next(y))  
print(next(y))  
def counter(max_value):
    counte=1
    while counte<=max_value:
        yield counte
        counte +=1
for number in counter(5):
    print("number",number)        
    
    
def read_large_file(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            yield line.strip()

# Example usage
for line in read_large_file('huge_log_file.txt'):
    print(line)  # or process line
    
def filter_even(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

# Example usage
nums = range(1, 1000000)
evens = filter_even(nums)

for e in evens:
    print(e)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_generator():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

# Example usage
gen = prime_generator()
for _ in range(10):
    print(next(gen))
    

def even_numbers(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)
    
    
    