stack =[]
#first in last out, stack is bucket 
def push():
    x= input('enter element')
    stack.append(x)
    print(stack)

def pop():
    if not stack:
        print('stack empty')
    else:    
        stack.pop()
        print(stack)    
while True:
    choice=input("enter1,2,3")  
    if choice=='1':
        push()
    elif choice=='2':
        pop()
    else:
        break       
    
'''
 1. Evaluate Reverse Polish Notation (Postfix Expression)
Problem Statement:
Evaluate an arithmetic expression in Reverse Polish Notation (postfix), where operators follow their operands.

Example:


Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
🔧 Solution in Python:
'''
def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                # Truncate towards zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))
    return stack[0]

# Test
print(evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
'''
🧠 Explanation:
Use a stack to push operands.

When an operator is encountered, pop the last two numbers, perform the operation, and push the result back.

Final result is the only value left in the stack.

Next Question: Valid Parentheses Checker?


It seems like I can’t do more advanced data analysis right now. Please try again later.

For now, I can continue giving you each stack question and its Python solution here one by one in text format. Once the tools are back up, I can compile them all into a PDF for you.

Would you like to continue with the second question: Valid Parentheses Checker? ​​



✅ 2. Valid Parentheses Checker
Problem Statement:
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

A string is valid if:

Open brackets are closed by the same type of brackets.

Open brackets are closed in the correct order.

Input: "()[]{}"
Output: True

Input: "(]"
Output: False

'''
def isValid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():  # opening brackets
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False  # invalid character
    return not stack

# Test cases
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))      # Output: False
'''
🧠 Explanation:
Use a stack to store opening brackets.

For every closing bracket, check if it matches the top of the stack.

If mismatched or stack is empty when it shouldn't be, return False.

At the end, if the stack is empty, it's valid.

Would you like to move on to Question 3: Min Stack?



✅ 3. Min Stack
Problem Statement:
Design a stack that supports the following operations in O(1) time:

push(x)

pop()

top()

getMin() → Retrieve the minimum element in the stack.

📌 Approach
Use two stacks:

One for the actual stack.

Another to track the current minimum value.
'''
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Push the new min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack and val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Test
s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.getMin())  # Output: -3
s.pop()
print(s.top())     # Output: 0
print(s.getMin())  # Output: -2
'''
🧠 Explanation:
When pushing, track the new minimum.

When popping, remove it from both stacks if needed.

This ensures getMin() always returns the current minimum in constant time.

Would you like to continue with Question 4: Largest Rectangle in Histogram?


✅ 4. Largest Rectangle in Histogram
Problem Statement:
Given an array of integers representing the heights of bars in a histogram, return the area of the largest rectangle that can be formed within the bounds of the histogram.

🔢 Example
python
Copy
Edit
Input: [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: Rectangle formed by heights 5 and 6 gives 5×2 = 10.
📌 Approach
Use a monotonic increasing stack:

Track indices of bars.

When you encounter a lower height, pop from the stack and calculate the area.

'''
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel value to flush the stack

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else (i - stack[-1] - 1)
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

# Test
print(largestRectangleArea([2, 1, 5, 6, 2, 3]))  # Output: 10
'''
🧠 Explanation:
Keep pushing increasing bars into the stack.

When a smaller height is found, we pop and calculate area using the popped height.

Width is calculated using the current index and index left in the stack.

Would you like to proceed with Question 5: Daily Temperatures?


✅ 5. Daily Temperatures
Problem Statement:
Given a list of daily temperatures, return a list where each element is the number of days you have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

🔢 Example

Input: [73, 74, 75, 71, 69, 72, 76, 73]
Output: [1, 1, 4, 2, 1, 1, 0, 0]
📌 Approach
Use a stack to track indices of temperatures. For each temperature, check if it’s greater than the temperature at the top of the stack and calculate the waiting days.

'''
def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    
    return result

# Test
print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # Output: [1, 1, 4, 2, 1, 1, 0, 0]
'''
🧠 Explanation:
As we go through each temperature, we check if the current temperature is greater than the one at the top of the stack.

If so, pop and calculate the number of days (difference of indices).

✅ 6. Next Greater Element
Problem Statement:
Given an array, find the next greater element for each element of the array.


Input: [4, 5, 2, 10]
Output: [5, 10, 10, -1]
📌 Approach
Use a stack to keep track of the next greater element for each number.

'''
def nextGreaterElements(nums):
    stack = []
    result = [-1] * len(nums) # result is 

    for i in range(2 * len(nums)):
        while stack and nums[stack[-1]] < nums[i % len(nums)]:
            idx = stack.pop()
            result[idx] = nums[i % len(nums)]
        stack.append(i % len(nums))
    
    return result

# Test
print(nextGreaterElements([4, 5, 2, 10]))  # Output: [5, 10, 10, -1]
'''
🧠 Explanation:
Traverse the array twice to simulate a circular array.

For each element, if it's greater than the one in the stack, update the result.

✅ 7. Remove K Digits
Problem Statement:
Given a number represented as a string, remove k digits to make the number as small as possible.


Input: num = "1432219", k = 3
Output: "1219"
📌 Approach
Use a stack to keep digits in order, removing digits when a smaller one is found.

'''
def removeKdigits(num, k):
    stack = []
    
    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # If k > 0, remove remaining digits from the end
    stack = stack[:-k] if k else stack
    
    # Remove leading zeros
    return ''.join(stack).lstrip('0') or '0'

# Test
print(removeKdigits("1432219", 3))  # Output: "1219"
'''
🧠 Explanation:
Traverse digits, pushing them to the stack.

Remove larger digits before smaller ones to ensure the smallest number.

✅ 8. Asteroid Collision
Problem Statement:
Simulate the motion of asteroids moving in a straight line, where positive numbers represent asteroids moving right and negative numbers represent asteroids moving left.

Input: [5, 10, -5]
Output: [5, 10]
📌 Approach
Use a stack to track surviving asteroids. When a new asteroid enters, compare with the top of the stack.

'''
def asteroidCollision(asteroids):
    stack = []
    
    for a in asteroids:
        while stack and a < 0 < stack[-1]:
            if stack[-1] > -a:
                break
            elif stack[-1] == -a:
                stack.pop()
                break
            else:
                stack.pop()
        else:
            stack.append(a)
    
    return stack

# Test
print(asteroidCollision([5, 10, -5]))  # Output: [5, 10]
'''
🧠 Explanation:
When a left-moving asteroid collides with a right-moving one, the larger one survives.

Keep the stack updated with surviving asteroids.

✅ 9. Decode String
Problem Statement:
Decode a string encoded in the form "3[a2[c]]" to "accaccacc".

🔢 Example
Input: "3[a2[c]]"
Output: "accaccacc"
📌 Approach
Use a stack to decode the string by processing digits and characters.

🧪 Python Code
'''
def decodeString(s):
    stack = []
    current_num = 0
    current_str = ""
    
    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == "[":
            stack.append((current_num, current_str))
            current_num, current_str = 0, ""
        elif char == "]":
            prev_num, prev_str = stack.pop()
            current_str = prev_str + current_str * prev_num
        else:
            current_str += char
    
    return current_str

# Test
print(decodeString("3[a2[c]]"))  # Output: "accaccacc"
'''
🧠 Explanation:
Use a stack to push the number and string at the start of each [ and build the string as we go.



✅ 10. Basic Calculator II
Problem Statement:
Implement a basic calculator to evaluate a simple expression string containing non-negative integers and operators +, -, *, and /.

🔢 Example
Input: "3+2*2"
Output: 7
📌 Approach
Use a stack to handle operator precedence:

Push numbers directly for + and -.

For * and /, pop the previous number and apply the operation.

🧪 Python Code
'''
def calculate(s):
    stack = []
    num = 0
    sign = '+'
    
    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)
        if c in '+-*/' or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))
            num = 0
            sign = c
    
    return sum(stack)

# Test
print(calculate("3+2*2"))  # Output: 7
'''
🧠 Explanation:
Keep track of numbers and operators.

Use a stack to apply multiplication/division immediately, and defer addition/subtraction.

✅ 11. Implement Stack using Queues
Problem Statement:
Implement a stack using only queue operations.

🧪 Python Code
'''
from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return not self.q

# Test
s = MyStack()
s.push(1)
s.push(2)
print(s.top())   # Output: 2
print(s.pop())   # Output: 2
print(s.empty()) # Output: False
'''
🧠 Explanation:
Simulate LIFO by rotating the queue after each push to bring the new element to the front.

✅ 12. Implement Queue using Stacks
Problem Statement:
Implement a queue using two stacks.

🧪 Python Code
'''
class MyQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack

# Test
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())  # Output: 1
print(q.pop())   # Output: 1
print(q.empty()) # Output: False
'''


✅ 13. Evaluate Reverse Polish Notation
Problem Statement:
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

🔢 Example

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
🧪 Python Code
'''
def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token not in "+-*/":
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            else: stack.append(int(a / b))  # Truncate toward zero
    return stack[0]

# Test
print(evalRPN(["2", "1", "+", "3", "*"]))  # Output: 9
'''
✅ 14. Longest Valid Parentheses
Problem Statement:
Given a string containing only '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

🧪 Python Code
'''
def longestValidParentheses(s):
    stack = [-1]
    max_len = 0
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len

# Test
print(longestValidParentheses(")()())"))  # Output: 4
'''
✅ 15. Remove All Adjacent Duplicates in String
Problem Statement:
Remove all adjacent duplicates in the string until no duplicates remain.

🧪 Python Code
'''
def removeDuplicates(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return ''.join(stack)

# Test
print(removeDuplicates("abbaca"))  # Output: "ca"
'''
✅ 16. Score of Parentheses
Problem Statement:
Compute the score of a balanced parentheses string based on:

() has score 1.

AB has score A + B.

(A) has score 2 * A.

🧪 Python Code
'''
def scoreOfParentheses(S):
    stack = [0]
    for ch in S:
        if ch == '(':
            stack.append(0)
        else:
            v = stack.pop()
            stack[-1] += max(2 * v, 1)
    return stack[0]

# Test
print(scoreOfParentheses("(()(()))"))  # Output: 6
'''
✅ 17. Simplify Path (Linux Style Path)
Problem Statement:
Simplify a Unix-style absolute file path.

🧪 Python Code
'''
def simplifyPath(path):
    stack = []
    for part in path.split("/"):
        if part == "..":
            if stack:
                stack.pop()
        elif part and part != ".":
            stack.append(part)
    return "/" + "/".join(stack)

# Test
print(simplifyPath("/a/./b/../../c/"))  # Output: "/c"
'''
✅ 18. Remove K Adjacent Duplicates in String
Problem Statement:
Remove every group of k adjacent, equal letters from the string until no more such groups exist.

🧪 Python Code
'''
def removeDuplicatesK(s, k):
    stack = []
    for ch in s:
        if stack and stack[-1][0] == ch:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([ch, 1])
    return ''.join(ch * cnt for ch, cnt in stack)

# Test
print(removeDuplicatesK("deeedbbcccbdaa", 3))  # Output: "aa"
'''
✅ 19. Maximal Rectangle (in Binary Matrix)
Problem Statement:
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's.

🧪 Python Code
'''
def maximalRectangle(matrix):
    if not matrix:
        return 0
    n = len(matrix[0])
    heights = [0] * n
    max_area = 0

    def largestRectangleArea(heights):
        stack = []
        max_area = 0
        heights.append(0)
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        heights.pop()
        return max_area

    for row in matrix:
        for i in range(n):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        max_area = max(max_area, largestRectangleArea(heights))
    return max_area

# Test
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
print(maximalRectangle(matrix))  # Output: 6
'''

✅ 20. Remove All Adjacent Duplicates in String II (with K)
Problem Statement:
Remove all adjacent duplicates in string where a group of exactly k characters are removed.

🧪 Python Code
'''
def removeDuplicates(s, k):
    stack = []
    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([char, 1])
    return ''.join(ch * cnt for ch, cnt in stack)

# Test
print(removeDuplicates("pbbcggttciiippooaais", 2))  # Output: "ps"
'''
✅ 21. Next Greater Element II (Circular Array)
Problem Statement:
Find the next greater number for every element in a circular array.

🧪 Python Code
python
Copy
Edit
'''
def nextGreaterElements(nums):
    n = len(nums)
    res = [-1] * n
    stack = []

    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            res[stack.pop()] = nums[i % n]
        if i < n:
            stack.append(i)
    return res

# Test
print(nextGreaterElements([1, 2, 1]))  # Output: [2, -1, 2]
'''
✅ 22. Minimum Add to Make Parentheses Valid
Problem Statement:
Given a string of '(' and ')', return the minimum number of parentheses additions to make it valid.

🧪 Python Code
'''
def minAddToMakeValid(s):
    res = 0
    balance = 0
    for ch in s:
        if ch == '(':
            balance += 1
        else:
            if balance == 0:
                res += 1
            else:
                balance -= 1
    return res + balance

# Test
print(minAddToMakeValid("()))(("))  # Output: 4
'''
✅ 23. Decode String
Problem Statement:
Decode the encoded string where encoding rule is k[encoded_string].

🧪 Python Code
'''
def decodeString(s):
    stack = []
    curr_num = 0
    curr_str = ''
    
    for ch in s:
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        elif ch == '[':
            stack.append((curr_str, curr_num))
            curr_str = ''
            curr_num = 0
        elif ch == ']':
            prev_str, num = stack.pop()
            curr_str = prev_str + num * curr_str
        else:
            curr_str += ch
    return curr_str

# Test
print(decodeString("3[a2[c]]"))  # Output: "accaccacc"
'''
✅ 24. Remove Outermost Parentheses
Problem Statement:
Remove the outermost parentheses of every primitive string in the input.

🧪 Python Code
'''
def removeOuterParentheses(s):
    res = ''
    opened = 0
    for ch in s:
        if ch == '(':
            if opened > 0:
                res += '('
            opened += 1
        else:
            opened -= 1
            if opened > 0:
                res += ')'
    return res

# Test
print(removeOuterParentheses("(()())(())"))  # Output: "()()()"
'''
✅ 25. Daily Temperatures
Problem Statement:
Given a list of daily temperatures, return a list where each element tells how many days you would have to wait until a warmer temperature.

🧪 Python Code
'''
def dailyTemperatures(temperatures):
    stack = []
    res = [0] * len(temperatures)
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            idx = stack.pop()
            res[idx] = i - idx
        stack.append(i)
    
    return res

# Test
print(dailyTemperatures([73,74,75,71,69,72,76,73]))  # Output: [1,1,4,2,1,1,0,0]
'''
✅ All 25 advanced stack problems are now completed.

📄 Generating a PDF with all questions and answers now...

Your PDF with 25 Advanced Python Stack Interview Questions and Solutions is ready for download:

📄 Click here to download the PDF

Let me know if you'd like a version with formatting, diagrams, or a cover page. 

1. How would you implement a stack using Python lists? What are the time complexities of push and
pop operations?
Answer: You can use Python lists where `append()` is push and `pop()` is pop. Both operations are O(1)
average case.
2. Implement a stack using two queues. What is the time complexity of each operation?
Answer: Use two `queue.Queue` objects. Push: O(n), Pop: O(1) or vice versa depending on the approach.
3. How can you implement a queue using two stacks in Python?
Answer: Use two stacks: one for enqueue, one for dequeue. Transfer elements as needed. Amortized O(1)
per operation.
4. Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Answer: Use two stacks: one for all elements, one for tracking minimums. Push/pop both stacks accordingly.
5. What are the trade-offs between using a list and a collections.deque for implementing a stack?
Answer: `list` is faster for append/pop at the end. `deque` is optimized for appends/pops at both ends and is
thread-safe.
6. Explain how recursion uses an implicit stack. Give a Python example.
Answer: Each recursive call pushes a frame on the call stack. Python manages it automatically. Example:
factorial function.
7. How would you detect and resolve stack overflow in a recursive Python function?
Answer: Use try-except on `RecursionError`, increase recursion limit if needed (`sys.setrecursionlimit()`), or
convert to iteration.
8. How do you evaluate a postfix (Reverse Polish Notation) expression using a stack in Python?
Answer: Iterate over tokens, push numbers, pop two for operations, push result back. Stack stores
intermediate results.
9. Write a Python function to check if a given string of brackets is balanced using a stack.
Answer: Use a stack to push opening brackets, pop when a matching closing bracket appears. Check stack
is empty at the end.
10. What is the use of inspect.stack() in debugging recursive functions or tracing execution?
Answer: It returns the current call stack. Useful for tracing function calls and debugging recursion issues.
11. Design a stack class in Python that also returns the maximum element in constant time.
Answer: Use an auxiliary stack to track max values. Push new max when needed, pop both stacks.
12. How can you use a stack to reverse a string or list in Python?
Answer: Push all characters/items onto a stack, then pop and append to new list/string.
13. Implement a browser back-button functionality using two stacks.
Answer: Use one stack for back history, another for forward. Move pages between stacks on navigation.
14. Simulate a call stack using Python data structures.
Answer: Use a list to simulate function call stack: push function name on call, pop on return.
15. Describe how depth-first search (DFS) uses a stack, and implement DFS using a stack in Python.
Answer: DFS uses a stack to track the path. Use an explicit list stack to implement iterative DFS.
16. Explain stack frame management in Python function calls.
Answer: Each function call creates a frame on the stack with local variables, instruction pointer, and return
address.
17. Can you explain how Python's exception handling uses a stack?
Answer: Exceptions bubble up through the call stack until caught. The stack unwinds in the process.
18. Write a Python function to convert an infix expression to postfix using a stack.
Answer: Use a precedence dictionary, push operators to stack, output operands. Handle parentheses
carefully.
19. Implement a custom Stack class with dynamic resizing (similar to ArrayList behavior).
Answer: Python lists resize dynamically. Wrap list with push, pop, peek, and check size/capacity.
20. What is a monotonic stack? Write Python code to solve the 'Next Greater Element' problem.
Answer: Monotonic stack is increasing/decreasing stack. Use it to efficiently find next greater/smaller
elements.
21. How would you implement a stack with O(1) time for getMin() and getMax() operations?
Answer: Use two extra stacks for min and max values. Update them during push and pop.
22. Explain tail recursion optimization and why Python doesn't support it with respect to the call
stack.
Answer: Tail recursion optimization reuses the stack frame. Python doesn't do this to keep stack traces
simple and clear.
23. What is the difference between recursion and using an explicit stack in Python?
Answer: Recursion uses implicit stack; explicit stack is managed by user code. Explicit avoids recursion
limits.
24. Create a Python decorator that logs stack depth of a function call using the sys module.
Answer: Use `sys._getframe()` to measure depth. Log info before calling the function inside decorator.
25. How do you use a stack to simulate backtracking in Python (e.g., N-Queens or Sudoku)?
Answer: Push states/choices onto the stack. Pop to backtrack when constraints are violated.


'''     

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for ele in operations:
           
            
            if ele=="C":
                stack.pop()
            elif ele=='D':
                z =stack[-1]
                z=z*2
                stack.append(int(z))
            elif ele=='+': 
                count=int(stack[-1])+int(stack[-2])  
                stack.append(count)
            else:
                stack.append(int(ele))   
        count=0
        print(stack)
        for x in stack:
            count= count+int(x)    
        return count            

      