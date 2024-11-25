
#abs(number)

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
