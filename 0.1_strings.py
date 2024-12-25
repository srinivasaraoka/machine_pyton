'''  Auther: Srinivas 
str.strip()
str.split()
str.capitalize()
str.isupper()
str.islower()
str.isalpha()
str1.remove = str.replace("-","") #delete pariticular string
shifted = s[i:] + s[:i]  # Shift the string
list1= list(str1) if you want get ele by ele in string, please convert the string to list
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

