'''  Auther: Srinivas 
str.strip() # main ipmportant to remove the space in string
str.split() #y=z.split(".")
str.capitalize()
str.isupper()
str.islower()
str.isalpha()
ch.isdigit() 
str1.remove = str.replace("-","") #delete pariticular string
shifted = s[i:] + s[:i]  # Shift the string
word.replace(".", "").isdigit(): it will remove the . in string and check for digit only 
list1= list(str1) if you want get ele by ele in string, please convert the string to list
longest = max(s.split(), key=len) # 'powerful'
s = "swiss"
first_unique = next((ch for ch in s if s.count(ch) == 1), None) # 'w'

a = "abcde"
b = "deabc"
is_rotation = len(a) == len(b) and b in a + a #

for char in s:
        freq[char] = freq.get(char, 0) + 1

def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

'''
str1='I love python'
list1=list(str1)
print(list1)
list2= list(map(str, str1.split()))
print(list2)
str1='abcd'
print(str1.capitalize())
word='USA'
s='#!Hello, I am srinivas, I have two friends#! '
print(s.split())
#['Hello,', 'I', 'am', 'srinivas,', 'I', 'have', 'two', 'friends']
print(s.strip('#! '))
#Hello, I am srinivas, I have two friends

def detectCapitalUse(word: str) -> bool:
    # Case 1: All letters are capitals
    if word.isupper():
        return True
    # Case 2: All letters are not capitals (lowercase)
    elif word.islower():
        return True
    # Case 3: Only the first letter is capital and the rest are lowercase
    elif word[0].isupper() and word[1:].islower():
        return True
    # If none of the cases match, return False
    else:
        return False

# Test cases
print(detectCapitalUse("USA"))       # True
print(detectCapitalUse("leetcode"))  # True
print(detectCapitalUse("Google"))    # True
print(detectCapitalUse("FlaG"))      # False

def extract_error_ips(logs):
    error_ips = []
    
    for line in logs.split("\n"):
        if "ERROR" in line:  # Check if the line contains "ERROR"
            words = line.split()  # Split by spaces
            for word in words:
                if "." in word and word.replace(".", "").isdigit():  # Simple IP detection
                    error_ips.append(word)  
    return error_ips

# Example Log Data
log_data = """[2025-03-11 14:25:36] ERROR: Connection timeout from 192.168.1.10
[2025-03-11 14:26:10] INFO: User admin logged in from 10.0.0.5
[2025-03-11 14:27:45] WARNING: Disk space low on server-12
[2025-03-11 14:29:12] ERROR: Authentication failed from 172.16.0.2"""

# Extract IPs from ERROR lines
error_ips = extract_error_ips(log_data)
print(error_ips)
class Solution:
    def letterCombinations(self, digits: str):
        dic1 = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        list1 = [i for i in digits]  
        len1 = len(list1)
        list4 = []      
        for x in range(0, len1):
            z = list1[x]
            value = dic1.get(z, '')  # Use empty string if key not found
            list4.append(value)
        if not digits:
            return []
        result = []
        # Alternative backtracking using string concatenation (no pop/append)
        print(len1, list4)
        def backtrack(index, current_string):
            if index == len1:
                result.append(current_string)
                print(index, current_string, result)
                return
            
            for char in list4[index]:
                #print(index, char, current_string)
                backtrack(index + 1, current_string + char)  # String concatenation
                print(index, char, current_string)
            print(current_string, result)

        backtrack(0, "")
        return result

# Example usage:
sol = Solution()
print(sol.letterCombinations("23"))
#y=z.split(".")

'''
1. Reverse a String
s = "hello"
rev = s[::-1] # 'olleh'
2. Check for Palindrome
s = "madam"
is_palindrome = s == s[::-1] # True
3. Count Character Frequencies
s = "banana"
freq = {ch: s.count(ch) for ch in set(s)} # {'b': 1, 'a': 3, 'n': 2}
4. Remove Duplicates (Keep Order)
s = "banana"
unique = ''.join(dict.fromkeys(s)) # 'ban'
5. Find All Vowels in a String
s = "hello world"
vowels = [ch for ch in s if ch in 'aeiou'] # ['e', 'o', 'o']
6. Check if Two Strings are Anagrams
a = "listen"
b = "silent"
is_anagram = sorted(a) == sorted(b) # True
7. Longest Word in a Sentence
s = "Python is powerful and fun"
longest = max(s.split(), key=len) # 'powerful'
8. Capitalize First Letter of Each Word
s = "hello world"
capitalized = ' '.join(word.capitalize() for word in s.split()) # 'Hello World'
9. First Non-Repeating Character
s = "swiss"
first_unique = next((ch for ch in s if s.count(ch) == 1), None) # 'w'
10. Compress String (RLE)
s = "aaabbcc"
_____________________________________________________________

#Advanced Python String Logical Formulas
___________________________________________________________________
'''
compressed = ""
prev = s[0]
count = 1
for ch in s[1:]:
  if ch == prev:
    count += 1
  else:
    compressed += prev + str(count)
  prev = ch
  count = 1
compressed += prev + str(count) # 'a3b2c2'

#11. Swap Case Without Using .swapcase()
s = "HeLLo"
swapped = ''.join([ch.lower() if ch.isupper() else ch.upper() for ch in s]) # 'hEllO'

#12. Check String Rotation
a = "abcde"
b = "deabc"
is_rotation = len(a) == len(b) and b in a + a # True

#13. Count Words Without Using .split()
s = "Python is fun"
count = sum(1 for ch in range(len(s)) if (s[ch] != ' ' and (ch == 0 or s[ch-1] == ' ')))
 # 3
#14. Group Characters by Frequency
s = "aabbccdde"
from collections import Counter
grouped = {}
for ch, freq in Counter(s).items():
    grouped.setdefault(freq, []).append(ch)
# {2: ['a', 'b', 'c', 'd'], 1: ['e']}
#15. Check Repeated Pattern
s = "abcabcabc"
is_repeated = s in (s + s)[1:-1] # True

'''
s = "swiss"
first_unique = next((ch for ch in s if s.count(ch) == 1), None) # 'w'
print(first_unique)

s = "Python is fun"
count = sum(1 for ch in range(len(s)) if (s[ch] != ' ' and (ch == 0 or s[ch-1] == ' ')))
for x in range(len(s)):
    print(x)
    if (s[x] != ' ' and (x == 0 or s[x-1] == ' ')):
        count += 1
count = sum(1 for x in range(len(s)) if (s[x] != ' ' and (x == 0 or s[x-1] == ' ')))  # 3
'''

def longest_unique_substring(s):
    seen = {}
    start = max_len = 0
    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = i
        max_len = max(max_len, i - start + 1)
    return max_len

# Example:
print(longest_unique_substring("abcabcbb"))  # 3 ("abc")

def custom_replace(s, old, new):
    result = ''
    i = 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result =result+ new
            i =i+ len(old)
            print("result_1", result)
        else:
            result =result+ s[i]
            i += 1
            print("result_2", result)
    return result

# Example:
print(custom_replace("abghfjhabab", "ab", "xy"))  # "xyxyxy"

def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            print(result)
            count = 1
    result.append(s[-1] + str(count))
    #print(result)
    return ''.join(result)

print(compress_string("aacabcc"))  # Output: "a3b1c2"
