import pytest
import re
'''
re.compile()
re.finditer()
re.match()
re.search()
re.findall()
re.sub()
re.subn()
re.split()
'''

pattern = re.compile("ab")
print("#pattern", pattern, type(pattern))
#matcher= pattern.finditer("abcccccccccab")


matcher= re.compile("ab").finditer("abcccccccccabab")
matcher= re.finditer("ab","abcccccccccabab")
count=0
for match in matcher:
    count+=1
    print("#match", match.start(), match.end(),match.group(), count)
print("#match_2", match.start(), match.end(),match.group(), count)
#match_2 13 15 ab 3
matcher=re.finditer("[A-Z]",'AHHJHJgfhfgh67767ABBA')
for m in matcher:
    print(m.start(),"#m.group is",m.group())


s="103e+123"
pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
#^[+-]?: The number can optionally start with a sign (+ or -).    
# Match the string s against the pattern
print("#valid=",bool(re.match(pattern, s.strip())))
print(re.findall(pattern,s.strip()))

'''
A regular expression is a sequence of characters that defines a search pattern, 
typically used for string matching. It can be used to search, edit, or manipulate 
text based on specific patterns.

Basic Syntax of Regular Expressions
.: Matches any character except a newline.
^: Matches the start of a string.
$: Matches the end of a string.
*: Matches 0 or more repetitions of the preceding pattern.
+: Matches 1 or more repetitions of the preceding pattern.
?: Matches 0 or 1 repetition of the preceding pattern.
{n}: Matches exactly n repetitions of the preceding pattern.
{n,}: Matches n or more repetitions of the preceding pattern.
{n,m}: Matches between n and m repetitions of the preceding pattern.
[]: Matches any one of the characters inside the brackets.
|: Acts as an OR operator between patterns.
(): Groups patterns together.

Examples
r'\d{2,4}': Matches 2 to 4 digits.
r'[A-Za-z]': Matches any single letter.
r'\bword\b': Matches the word "word" as a whole word (using word boundaries).

'''


str_1= "srinivasarao.043@gmail.com 8309895383 192.168.1.3 90.90.90.90.90"
assert re.findall(r'[a-zA-Z0-9+.]+@[a-zA-Z]+\.[a-z]{2,}', str_1)
print(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', str_1))
print(re.findall(r'[0-9]{10}', str_1))
print(re.findall(r' (?:[0-9.]{1,3}\.) {3}+[0-9]{1,3}', str_1))
print(re.findall(r'\b(?:[0-9.]{1,3}\.){3}+[0-9]{1,3}\b', str_1))
#? Matches 0 or 1 repetition of the preceding pattern.
#(?:[0-9]{1,3}\.){3}:
#(?:...): This is a non-capturing group. Inside it, [0-9]{1,3}\. matches a 
# number with 1 to 3 digits followed by a dot (.).
'''
2. Non-Capturing Groups
Sometimes, you want to group parts of a pattern but don't need to capture the match. 
For this, you can use a non-capturing group with (?:...). This is useful when you 
want to apply operators (like *, +, or ?) to a group of patterns without capturing 
the matched text.

Example:

import re

pattern = r'(?:cat|dog)s?'
text = 'cats and dogs'

matches = re.findall(pattern, text)
print(matches)  # Output: ['cats', 'dogs']
Here, (?:cat|dog) groups "cat" or "dog" but does not capture the result. The s? makes the "s" optional, so it matches both singular and plural forms of the words.

'''



# when you want replace more ch to space you will use regular 
# expertion

s1 = "A man, a plan, a canal: Panama"
str1= re.sub(r"[^A-Za-z0-9]",'', s1)
print('#str1',str1)
#str1 AmanaplanacanalPanama
str2= str1.lower()
print(str2)
if str2== str2[::-1]:
    print('paraladrum')
else:
    print('not a paraladrum')  


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
import re
for _ in range(int(input())):
    n=input().strip()
    z=re.compile(r'^[+-]?[0-9]*\.[0-9]+$')
    if re.fullmatch(z,n):
        print(True)
    else:
        print(False) 
'''           

#4
#4.0O0
#-1.00
#+4.54
#SomeRandomStuff            
str1= "SR-WLC1#show ap name APCC9C.3EF1.2B70 config general Cisco AP Name   : APCC9C.3EF1.2B70 Cisco AP Identifier                             : 10f9.20fe.a560 Country Code                                    : US Regulatory Domain Allowed by Country            : 802.11bg:-A   802.11a:-AB   802.11 6GHz:-B Radio Authority IDs                             : None AP Country Code                                 : US  - United StatesAP Regulatory Domain  802.11bg                                      : -A  802.11a                                       : -B  802.11 6GHz                                   : -BMAC Address                                     : cc9c.3ef1.2b70IP Address Configuration                        : DHCPIP Address                                      : 199.168.10.115IP Netmask                                      : 255.255.255.0 Gateway IP Address                              : 199.168.10.254"
ap_name=re.search(r"Cisco AP Name\s*:\s*(\w+.\w+.\w+)",str1)
print(ap_name.group(0))
country_code=re.search(r'Country Code\s*:\s*(\w+)',str1)
country_code=re.search(r'Country Code\s*:\s*(\w+)',str1)
print("#country_code.group(1)",country_code.group(1))
#country_code.group(1) US
country_code_1=re.findall(r'Country Code\s*:\s*(\w+)',str1)
print("#country_code_1",country_code_1)
