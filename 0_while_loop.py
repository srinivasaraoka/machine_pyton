#Auther "Srinivas"
# while loop will use when we know stopping condition
#for loop when we know how many time excute body
#abs(number)
#shifted = s[i:] + s[:i]  # Shift the string
#vowel_indices = [i for i, char in enumerate(s_list) if char in vowels] 
# if you want indexes please take enumerate 
'''
We use recursion when the problem is best solved in smaller steps and then combining those steps towards a larger solution. 
'''
import logging
import logger
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def countdown(n):
    while n > 0:
      print(n)
      n = n - 1
countdown(6)
'''
You can almost read the while statement as if it were English. It means, “While n is greater
than 0, display the value of n and then decrement n. When you get to 0, display the word
Blastoff!”
More formally, here is the flow of execution for a while statement:
1. Determine whether the condition is true or false.
2. If false, exit the while statement and continue execution at the next statement.
3. If the condition is true, run the body and then go back to step 1.

'''

def isHappy(n):
    seen_numbers = set()  # Keep track of numbers we've seen to detect loops

    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n) 
        print(seen_numbers) # Add the current number to the set
        print(n)
        n = sum_of_squares(n)  # Replace n with the sum of the squares of its digits
        print(n)
    return n == 1  # If n is 1, it's a happy number

def sum_of_squares(n):
    total = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        total += digit * digit  # Add the square of the digit to the total
        n //= 10  # Remove the last digit
    return total

# Example usage:
print(isHappy(19))  # Output: True
print(isHappy(2))   # Output: False

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        while n%2==0:
            n=n//2
        return n==1  
    
def maxPower(s: str) -> int:
    max_power = 1
    current_power = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_power += 1
        else:
            max_power = max(max_power, current_power)
            current_power = 1  
    return max(max_power, current_power)

print(maxPower('abbbbcccdddddd'))       
#powerofthree
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if  n<=0:
            return False
        while n%3==0:
            n=n//3
        return n==1        


def first_missing_positive(arr):
    # Convert the list to a set for O(1) lookups
    num_set = set(arr)
    
    # Start checking from 1 upwards
    smallest_missing = 1
    
    while smallest_missing in num_set:
        smallest_missing += 1  # Move to the next number
    
    return smallest_missing

# Test cases
print(first_missing_positive([3, 4, -1, 1]))  # Output: 2

def sequence(n):
    while n != 1:
        if n % 2 == 0: # n is even
           n = n / 2
        else: # n is odd
           n = n*3 + 1
sequence(10)          

def pad(str1):
    flag=True
    i,j=0,len(str1)
    while i<j:
        if str1[i] != str1[j-1]:
            flag=False
            break
        i += 1
        j-=1
    return flag
    

str1='malayalam'
logger.info(pad(str1))

def is_power_of_two(n):
    print(n & (n - 1))
    print(16 & 15)
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(16))  # True
def power_of_two1(n):
    for x in range(1,n//2):
        if x**2==n:
            return True
    return False
print(power_of_two1(16))  # True    


'''
Question 1
In Python, what do while loops do?
while loops tell the computer to repeatedly execute a set of instructions while a condition is true.
while loops instruct the computer to execute a piece of code a set number of times.
while loops branch execution based on whether or not a condition is true.
while loops initialize variables in Python.

Which techniques can prevent an infinite while loop? Select all that apply.


Change the value of a variable used in the while condition
Use the stop keyword
Use the break keyword
Use the continue keyword
1 point
3.
Question 3
The following code contains an infinite loop, meaning the Python interpreter does not know when to exit the loop once the task is complete. To solve the problem, you will need to:

Find the error in the code

Fix the while loop so there is an exit condition

Hint: Try running your function with the number 0 as the input and observe the result.

Note that Coursera’s code blocks will time out after 5 seconds of running an infinite loop. If you get this timeout error message, it means the infinite loop has not been fixed. 

1234781011121314151617181995620
def is_power_of_two(number):
  # This while loop checks if the "number" can be divided by two
  # without leaving a remainder. How can you change the while loop to
  # avoid a Python ZeroDivisionError?
  if number ==0:
    return False
  while number % 2 == 0:
    number = number / 2
    #break
  # If after dividing by 2 "number" equals 1, then "number" is a power

Reset
False
True
True
False
1 point
4.
Question 4
Write a function that takes an argument n and returns the sum of integers from 1 to n. For example, if n=5, your function should add up 1+2+3+4+5 and return 15. If n is less than 1, just return 0. Use a while loop to calculate this sum. 

123456789101112131415161718
def sum_of_integers(n):
  if n < 1:
    return 0


  i = 1
  sum = 0
  while i<=n:
    sum = sum + i
    i = i+1

Reset
6
10
15
1 point
5.
Question 5
Fill in the blanks to complete the function, which should output a multiplication table. The function accepts a variable “number” through its parameters. This “number” variable should be multiplied by the numbers 1 through 5, and printed in a format similar to “1x6=6” (“number” x “multiplier” = “result”). The code should also limit the “result” to not exceed 25. To satisfy these conditions, you will need to:

Initialize the “multiplier" variable with the starting value

Complete the while loop condition

Add an exit point for the loop

Increment the “multiplier" variable inside the while loop

3456789101112131415161718192021222324252627282930313233343536373839404142
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        
        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3) 

Reset
3x1=3
3x2=6
3x3=9
3x4=12
3x5=15
3x6=18
3x7=21
3x8=24
5x1=5
5x2=10
5x3=15
5x4=20
5x5=25
8x1=8
8x2=16

'''
