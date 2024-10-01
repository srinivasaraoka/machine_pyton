'''  Auther: Srinivas '''
#genertor is like a list or tupple
'''

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



list1=[1,2,3,4]
z=iter(list1)
print(z)
print(next(z))
print(next(z))
'''
A generator is a special type of iterator that is defined using a function.
Instead of returning all values at once, it yields values one at a time, 
pausing execution and preserving the function’s state for each successive call.
This makes generators more memory-efficient when working with large datasets.
'''
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