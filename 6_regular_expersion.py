import pytest
import re
import logging
import logger
logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("custom_logger")
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
text = "Hello\nWorld!"
text = '''1one_ct_one 2two_cct_two 3three_ccat_three 4four_cat_four 5fve_cttt_five 6six_caat_six 7seven_cut_siven c8t c/t c88t c)t c,t c t c@t c#t c.t c 
t 11_elevenc+t_eleven 12_twelveca_twelve c88tt c88ct c
c ctttt
'''
try:
    logger.info(f'#functionality of * is c*t= {re.findall(r"c*t", text)}\n') # * is zero or more occurance of c before t # * means zero or more occurrences of the preceding character or group
    #functionality of * is c*t= ['ct', 't', 'cct', 't', 't', 't', 't', 't', 'ct', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'ct']
    z=re.search(r"c*t", text)#}\n') # * is zero or more occurance of c before t # * means zero or more occurrences of the preceding character or group
    if z:
       print("Matched string:", z.group(), z.group(0), z.groups()) # Matched string: ct ct ()
    else:
       print("No match found")
    matches = re.finditer(r'c*t', text)
    for match in matches:
        print("Matched:", match.group())      
    ''' 
        "ct": ("✅", "Valid: 'c' before 't'"),
        "cct": ("✅", "Valid: Multiple 'c' before 't'"),
        "ccat": ("❌", "Breaks: 'a' appears between 'c' and 't'"),
        "cat": ("❌", "Breaks: 'a' appears between 'c' and 't'"),
        "caat": ("❌", "Breaks: 'a' appears between 'c' and 't'"),
        "cut": ("❌", "Breaks: 'u' appears between 'c' and 't'"),
        "c8t": ("✅", "Valid: '8' ignored, still fits c*t"),
        "c/t": ("✅", "Valid: c* allows zero 'c', so only 't' is matched"),
        "c88t": ("✅", "Valid: '88' ignored, still fits c*t"),
        "c t": ("✅", "Valid: Space breaks 'c' sequence, so only 't' is matched"),
        "c@t": ("✅", "Valid: '@' breaks 'c' sequence, so only 't' is matched"),
        "c#t": ("✅", "Valid: '#' breaks 'c' sequence, so only 't' is matched"),
        "cttt": ("✅", "Valid: 't' repeats, still follows c*t"),
        "c.t": ("✅", "Valid: '.' breaks 'c' sequence, so only 't' is matched"),
        "c (alone)": ("❌", "Breaks: 't' is mandatory"),
        "t (alone)": ("✅", "Valid: c* allows zero 'c', so 't' is matched"),
        "c+t": ("✅", "Valid: '+' is ignored, c*t still matches")
    '''
    count= 0
    logger.info(f"#functionality of + is r'c+t' = {re.findall(r'c+t', text)}\n") # + is one or more occurance of c before t
    #functionality of + is r'c+t' = ['ct', 'cct', 'ct', 'ct']  
    
    logger.info(f"#funcionalty of '.'is r'c.t' ={re.findall(r'c.t', text)}\n") # . matches any single character
    #2 funcionalty of '.'is r'c.t' =['cct', 'cat', 'cat', 'ctt', 'cut', 'c8t', 'c/t', 'c)t', 'c,t', 'c t', 'c@t', 'c#t', 'c.t', 'c+t']

    logger.info(f"#funcionalty of '?'is ={re.findall(r'c?t', text)}\n") # ? is zero or one occurance of c before t
    # funcionalty of '?'is =['ct', 't', 'ct', 't', 't', 't', 't', 't', 't', 't', 'ct', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'ct']

    logger.info(f"#funcionalty of '.*'is ={re.findall(r'c.*t', text)}\n") # .* matches any character zero or more times between c and t
    # funcionalty of '.*'is =['cat ccat cccat ct caat cut c8t c/t c88t c t c@t c#t c.t', 'c+t']

    pattern= r"c/t"
    logger.info(f'#functionality of / is {re.findall(pattern, text)}\n')  # Corrected description for the pattern.
    #functionality of / is ['c/t']
     
    pattern= r"c\dt"
    logger.info(f'#functionality of \d is {re.findall(pattern, text)}\n')
    #functionality of \d is ['c8t']

    pattern= r"c\st"
    logger.info(f'#functionality of \s is {re.findall(pattern, text)}\n')
    #functionality of \s is ['c t']

    pattern= r"c\wt" # \w matches any word character (alphanumeric & underscore) single CHARACTER
    logger.info(f'#functionality of \w is {re.findall(pattern, text)}\n')
    #functionality of \w is ['cat', 'cat', 'cat', 'cut', 'c8t']
   
    pattern= r"c\.t" #note most improtent is to use raw string
    logger.info(f"# funcionalty of . is ={re.findall(pattern, text)}\n")
    # funcionalty of . is =['c.t']

    logger.info(f"funcionalty of '[], [cat]'is ={re.findall(r'[cat]', text)}\n") # [] matches any one of the characters inside the brackets.
    # funcionalty of '[]'is =['c', 'a', 't', 'c', 'c', 'a', 't', 'c', 'c', 'c', 'a', 't', 'c', 'a', 'a', 't', 'c', 't', 'c', 't', 'c', 't', 'c', 't', 'c', 't', 'c', 't', 'c', 't', 'c', 't', 'c', 't']

    logger.info(f"# funcionalty of () (cat)is ={re.findall(r'(cat)', text)}\n")
    # funcionalty of () is =['cat', 'cat', 'cat']
    
    pattern= r"c\d*t"
    logger.info(f'#functionality of \d* is {re.findall(pattern, text)}\n')
    #functionality of \d* is ['ct', 'ct', 'ct', 'c8t', 'c88t', 'c88t', 'ct']
    
    pattern = r"c\s*t"
    logger.info(f'#functionality of \s* is {re.findall(pattern, text)}\n') # matches 
    #functionality of \s* is ['ct', 'ct', 'ct', 'c t', 'c \nt', 'ct']
    
    pattern= r"c\w*t"
    logger.info(f'#functionality of \w* is {re.findall(pattern, text)}\n')
    
    pattern= r"c\d+t"
    logger.info(f'#functionality of \d+ is {re.findall(pattern, text)}\n')
    #functionality of \d+ is ['c8t', 'c88t']
    
    pattern= r"c\s+t"
    logger.info(f'#functionality of \s+ is {re.findall(pattern, text)}\n')
    #functionality of \s is ['c t', 'c \nt']
    
    pattern= r"c\w+t"
    logger.info(f'#functionality of \w+ is {re.findall(pattern, text)}\n')
    #functionality of \w+ is ['cat', 'ccat', 'cccat', 'caat', 'cut', 'c8t', 'c88t']
    
    pattern= r"c\d.t"
    logger.info(f'#functionality of \d. is {re.findall(pattern, text)}\n')
    #functionality of \d+ is ['c8t', 'c88t']
    
    pattern= r"c\s.t"
    logger.info(f'#functionality of \s. is {re.findall(pattern, text)}\n')
    #functionality of \s is ['c t', 'c \nt']
    
    pattern= r"c\w.t"
    logger.info(f'#functionality of \w. is {re.findall(pattern, text)}\n')
    #functionality of \w+ is ['cat', 'ccat', 'cccat', 'caat', 'cut', 'c8t', 'c88t']
    
    logger.info(f"# funcionalty of (*) = r'(c*t)' is ={re.findall(r'(c*t)', text)}\n")
    # funcionalty of (*) = r'(c*t)' is =['ct', 't', 'cct', 't', 't', 't', 't', 't', 'ct', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'ct']

    logger.info(f"# funcionalty of (+) = r'(c+t)' is ={re.findall(r'(c+t)', text)}\n")
    # funcionalty of (+) = r'(c+t)' is =['ct', 'cct', 'ct', 'ct']
    
    #logger.info(f'#functionality of *. is {re.findall(r"*.", text)}\n')  
    # ERROR - error is nothing to repeat at position 0
    logger.info(f'#functionality of .+ is {re.findall(r".+", text)}\n')   
    logger.info(f"#- funcionalty of '.?'is ={re.findall(r'c.?t', text)}\n") # .? matches any character zero or one time
    
    logger.info(f"#- funcionalty of '*?'is ={re.findall(r'c*?t', text)}\n") # *? matches zero or more occurance of c before t
     # funcionalty of '*?'is =['ct', 't', 'cct', 't', 't', 't', 't', 't', 't', 't', 'ct', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 't', 'ct']
     
    logger.info(f"#- funcionalty of '.*?'is ={re.findall(r'c.*?t', text)}\n")
    # funcionalty of '.*?'is =['ct', 'cct', 'ccat', 'c)t', 'c,t', 'cat', 'ct', 'caat', 'cut', 'c8t', 'c/t', 'c88t', 'c t', 'c@t', 'c#t', 'c.t', 'c+t', 'ca_t', 'c88t', 'c88ct']
    
    logger.info(f"#- funcionalty of '?.'is ={re.findall(r'c?.t', text)}\n") # ?. matches zero or one occurance of c before t
     # funcionalty of '?.'is =['ct', '2t', 'cct', '_t', '3t', 'cat', '_t', 'c)t', 'c,t', 'cat', 'ctt', 'at', 'cut', 'c8t', 'c/t', '8t', 'c t', 'c@t', 'c#t', 'c.t', 'c+t', '_t', '_t', '8t', 'ct']
    
    logger.info(f"# - funcionalty of '?.*'is ={re.findall(r'c?.*t', text)}\n") 
    # 9 funcionalty of '?.*'is =['1one_ct_one 2two_cct_two 3three_ccat_three c)t c,t 4four_cat_four 5fve_cttt_five 6six_caat_six 7seven_cut_siven c8t c/t c88t c t c@t c#t c.t', 't 11_elevenc+t_eleven 12_twelveca_twelve c88tt c88ct']
    
    #logger.info(f"#- funcionalty of '?*'is ={re.findall(r'c?*t', text)}\n") # ?. matches zero or one occurance of c before t
    #[01/Apr/2025 13:21:52] ERROR - error is multiple repeat at position 2
    
    #logger.info(f"# funcionalty of '?*.'is ={re.findall(r'c?*.t', text)}\n") 
    #[01/Apr/2025 13:21:52] ERROR - error is multiple repeat at position 2
    pattern = r'.*?(\(\d+(?:,\d+)*\))'
    logger.info(f"# funcionalty of pattern is ={re.findall(pattern, text)}\n") 
    logger.info(f"#- funcionalty of '?:'is ={re.findall(r'c?:t', text)}\n") # 
    logger.info(f"#- funcionalty of :? is ={re.findall(r'c:?t', text)}\n") # 
    logger.info(f"#- funcionalty of '(?:)'is ={re.findall(r'c(?:)t', text)}\n") # 
    logger.info(f"#- funcionalty of '(:?)'is ={re.findall(r'c(:?)t', text)}\n") # 
    pattern= r"c\w+{2}t" 
    pattern= r"c\w{2}t"
    logger.info(f'#functionality of \w{2} is {re.findall(pattern, text)}\n')
    
except Exception as e:
    logger.error(f'error is {e}')
    print(f'error is {e}') 

pattern = re.compile("ab")
print("#pattern", pattern, type(pattern))
#matcher= pattern.finditer("abcccccccccab")
reg= 'abdccsjdabcgfdfsgfdshj23123456@@@###- version: 12123  State :  Onboarded fdfch fgdfd'

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


Common Regex Symbols
Symbol	Meaning	Example	Matches
.	Any character except newline	a.b	acb, axb, a1b (but not ab or acdb)
^	Start of string	^abc	Matches if the string starts with abc
$	End of string	xyz$	Matches if the string ends with xyz
*	0 or more occurrences	a*	Matches a, aa, aaa, or "" (empty)
+	1 or more occurrences	a+	Matches a, aa, aaa, but not ""
?	0 or 1 occurrence	a?	Matches a or ""
{n}	Exactly n occurrences	a{3}	Matches aaa
{n,}	At least n occurrences	a{2,}	Matches aa, aaa, aaaa...
{n,m}	Between n and m occurrences	a{2,4}	Matches aa, aaa, or aaaa
[]	Character set	[abc]	Matches a, b, or c
`	`	OR operator	`a
()	Grouping	(ab)+	Matches ab, abab, ababab
\	Escape special characters	\.	Matches a literal .
2. Character Classes
Character Class	Meaning	Example	Matches
\d	Any digit (0-9)	\d+	123, 4567
\D	Non-digit characters	\D+	abc, xyz
\w	Any word character (a-z, A-Z, 0-9, _)	\w+	hello123, A_B_C
\W	Non-word characters	\W+	!@#, ?
\s	Whitespace (space, tab, newline)	\s+	Matches spaces and tabs
\S	Non-whitespace characters	\S+	Matches any non-space character
3. Anchors and Boundaries
| Anchor | Meaning | Example | Matches | |-----|-----|-----| | ^ | Start of string | ^hello | Matches if the string starts with hello | | $ | End of string | world$ | Matches if the string ends with world | | \b | Word boundary | \bword\b | Matches word but not sword or wording | | \B | Non-word boundary | \Bword\B | Matches inside a word like swordfish |

4. Lookaheads and Lookbehinds
Type	Syntax	Example	Meaning
Positive Lookahead	?=pattern	q(?=u)	Matches q only if followed by u
Negative Lookahead	?!pattern	q(?!u)	Matches q only if NOT followed by u
Positive Lookbehind	?<=pattern	(?<=\$)\d+	Matches digits preceded by $
Negative Lookbehind	?<!pattern	(?<!\$)\d+	Matches digits NOT preceded by $
Examples
r'\d{2,4}': Matches 2 to 4 digits.
r'[A-Za-z]': Matches any single letter.
r'\bword\b': Matches the word "word" as a whole word (using word boundaries).
re.search('(.*) BI=([0-9]+), (.*)', bcn)
'''
str_1= "srinivasarao.043@gmail.com 8309895383 192.168.1.3 90.90.90.90.90"
assert re.findall(r'[a-zA-Z0-9+.]+@[a-zA-Z]+\.[a-z]{2,}', str_1)
print(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', str_1))

pattern = r'\b(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.|$)){4}\b'

print(re.findall(r'[0-9]{10}', str_1))
print(re.findall(r' (?:[0-9.]{1,3}\.) {3}+[0-9]{1,3}', str_1))
print(re.findall(r'\b(?:[0-9.]{1,3}\.){3}+[0-9]{1,3}\b', str_1))

ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str_1)
if ip:    
    print("hgfhdghfdgg---------------->",ip.group())
    z= ip.group()
    y=z.split(".")
    print(y)
    for x in y:
        if int(x)>255:
            print("invalid ip address")      
else:     
    print("No IP found")

#? Matches 0 or 1 repetition of the preceding pattern.
#(?:[0-9]{1,3}\.){3}:
#(?:...): This is a non-capturing group. Inside it, [0-9.]{1,3}\. matches a 
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

''''
Regular expressions define search patterns using a combination of literals and special symbols.
'''
'''
lag_status = re.findall('(ap_name)*.+(Lag status modified)', lag)
res = re.search('[0-9] \s+ ([a-zA-Z0-9]+) \s+ ([a-zA-Z0-9:]+)(.*) \s+ .*', line) 
ping_res = re.search(r'Success rate is ([\d]+) percent', ping_out)
re.findall(r'(916[234]|917[26])', ap_model)
re.findall(re.compile(r'Slot ID\s*:\s*(\d+)'), output)]
re.findall(r"\s+(\d+)\s+(\d+)\s+\w+",return_res)
re.findall('5\d+MHz\(\s+\d+\)|5\d+MHz\(\d+\)', ap_out)

lag = self.execute("show wireless stats ap history")
logger.info(lag)
lag_status = re.findall('(ap_name)*.+(Lag status modified)', lag)
logger.info(lag_status)
        
res = re.search('[0-9] \s+ ([a-zA-Z0-9]+) \s+ ([a-zA-Z0-9:]+)(.*) \s+ .*', line)        

ping_out = self.execute(ping_cmd, target=chassis, timeout=300)
ping_res = re.search(r'Success rate is ([\d]+) percent', ping_out)
                
ping_res = re.findall(r'Reply to request [0-9] from ([0-9\.]*), [0-9]+ ms', ping_out)
            return_dict['reachable_host'] = ping_res
            
output = self.execute("show ap name {} channel".format(ap_name), timeout=60)
        return [int(x) for x in re.findall(re.compile(r'Slot ID\s*:\s*(\d+)'), output)]                        

return_res = self.execute('show flexconnect wlan vlan')
chck=re.findall(r"\s+(\d+)\s+(\d+)\s+\w+",return_res)
        for i in chck:
            result.update({i[0]:i[1]})
output = self.execute('show client summary')
output_1=re.findall("{}.*".format(client_mac),output)            

ap_out = self.execute('show controllers dot11Radio {}'.format(slot))
            dfs_channel_freq = re.findall('5\d+MHz\(\s+\d+\)|5\d+MHz\(\d+\)', ap_out)
            out.append(dfs_channel_freq)
            temp = re.findall('(5\d+)MHz', str(dfs_channel_freq))
            out.append(temp)
 
 pattern = '802.11\w\s+(.*M)\s+Rate:\s+(Mandatory|Supported|Unsupported)'
        match = re.findall(pattern, rate_string)
        
output = ctrl.execute('show wlan summary')
    match = re.findall(r'[0-9]+ +([0-9a-zA-Z-_]+) +[0-9a-zA-Z]+', output)
    if match == None:
        return 0
    for wlan in match:
        ctrl.configure('no wlan {wlan}'.format(wlan=wlan))        

'''
# str1="
# [2025-03-11 14:25:36] ERROR: Connection timeout from 192.168.1.10  
# [2025-03-11 14:26:10] INFO: User admin logged in from 10.0.0.5 
# [2025-03-11 14:27:45] WARNING: Disk space low on server-12
# [2025-03-11 14:29:12] ERROR: Authentication failed from 172.16.0.2  
# "
# logger.info(str1)

import re
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP == "256.256.256.256":
                return ("Neither")
            
        z= re.findall(r'(?:[1-9.]{1,3}\.){3}+[1-9]{1,3}', queryIP)
        y= re.findall(r'\b([A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b', queryIP)
                     #r'([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'
        print(y)
        if z and y:  
            return ("IPv4")
        elif y:
            if ":" in y:
                return "Neither"
            else:
                 return ("IPv6")              
        else:
            return "Neither"
        
# Example Usage:
solution = Solution()
# print(solution.validIPAddress("172.16.254.1"))  # Output: "IPv4"
# print(solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))  # Output: "IPv6"
# print(solution.validIPAddress("256.256.256.256"))  # Output: "Neither"
# print(solution.validIPAddress("02001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Output: "Neither"

str1= """
DB10-Indoor-ExtGPS                ecf4.0cce.12e0  3       Enabled        Up            160      2/8 (12 dBm)    (5,1,9,13,17,21,25,29)              Local   
DB10-Outdoor-IntGPS               ecf4.0cce.1480  3       Enabled        Down          160      ~8/8 (-3 dBm)   (21,17,25,29,1,5,9,13)              Local         """
ap_model = "DB10-Indoor-ExtGPS"
pattern1 = re.search(r'Up\s*\d*', str1)
# Regex pattern to find the required bracketed numbers for the given AP model
pattern = rf"{ap_model}.*?(\(\d+(?:,\d+)*\))"
pattern = r".*?(\(\d+(?:,\d+)*\))"
# pattern = r"(\(\d+(?:,\d+)*\))"
# pattern = r"\(\d+(?:,\d+)*\)"
# pattern = r"\(\d+(?:,\d+)*\)"
# pattern = r"\d+(?:,\d+)*"
# pattern = r"(?:,\d+)*"
channel= 5
# Search for the pattern in the string
#match = re.search(pattern, str1)
match = re.findall(pattern, str1)
print("-!",match)
# if match:
#     extracted_string = match.group(0)
#     print(extracted_string)
#     if str(channel) in extracted_string:
#         print("channel is present")
print(pattern1)

str1= """
AP8C88.8176.CC30                  ecf4.0cce.0780  3       Enabled        Up            40       ~1/8 (20 dBm)   (5,1)                               Local      

"""
width= 20
channel= 5
pattern= r'Up\s*\d*'
# match = re.search(pattern, str1)
# logger.info(f"match: {match}")
# if str(width) in match.group(0):
#     logger.info(f"change channel width")
#     print(channel, width )

text = "cat 123 dog"
pattern = r"(\w+) (\d+) (\w+)"
match = re.search(pattern, text)
print(match)
if match:
    print(match.group(0))  # Output: 'cat 123 dog' (full match)
    print(match.group(1))  # Output: 'cat' (first captured group)
    print(match.group(2))  # Output: '123' (second captured group)
    print(match.group(3))  # Output: 'dog' (third captured group)
    
match = re.findall(pattern, text)
print(match)
'''
Why use findall: You want to extract both names and ages, and get them in a list of tuples.

Summary of Differences:
Function	What it returns	When to use it	Example Use Case
re.search()	Match object (first match)	When you need the first match or if you want to check if a pattern exists	Find if a specific word exists in a string and extract it (first match).
re.findall()	List of matches (all matches)	When you want all matches in a string (as a list of strings or tuples)	Extract all occurrences of a word or pattern from a text.
When to use which:
Use re.search() if:

You only need to check for the first match of the pattern.

You're interested in getting the first match object and working with it.

You're checking for existence (i.e., if the pattern matches or not).

Use re.findall() if:

You need to find all matches in the string and return them as a list.

You want to capture multiple groups and return them as a list of tuples.

You need to extract all occurrences of a pattern (not just the first).


'''
output = '''   
Cisco IOS XE Software, Version BLD_POLARIS_DEV_LATEST_20250401_002324
Cisco IOS Software [IOSXE], C9800 Software (C9800_IOSXE-K9), Experimental Version 17.18.20250401:013416 [BLD_POLARIS_DEV_LATEST_20250401_002324:/nobackup/mcpre/s2c-build-ws 102]
Copyright (c) 1986-2025 by Cisco Systems, Inc.
Compiled Mon 31-Mar-25 18:38 by mcpre


'''
match = re.search(r'Experimental Version\s*(\d+.\d+)', output)
match1 = re.search(r'Experimental Version\s\d.*', output)
match2 = re.search(r'Experimental Versions\s[0-9.]', output)
print(match.group())
# print(match1.group())
# print(match2.group())       
if '17.17' <= match.group(1):
    print("upgrade is required")
else:
    print("upgrade is not required")    
    
str1="""
AP8C88.8176.CC30                  ecf4.0cce.0780  3       Enabled        Up            40       ~2/8 (14 dBm)   (125,121)                           Local      

"""    
pattern = r'Up\s*(\d*)'
match = re.search(pattern, str1)
print(match.group())
if match:
    print(type(match.group(1)))  # Output: 'cat' (first captured group)

str2='''
AP8C88.8176.CC30                  ecf4.0cce.0780  3       Enabled        Up            40       ~3/8 (11 dBm)   (125,121)                           Local

'''
pattern= r'~\d+'
match = re.search(pattern, str2)
z = re.findall(r'~(\d+)', str2)
print(z)
power=3
pattern = r'~(\d+)'
match = re.findall(pattern,str2)  
if str(power) == match[0]:
    logger.info(f"ap tx power is asserted")
else:
    logger.info(f"ap tx power is not asserted")
import re
param1='AP8C88.8176.B980                  ecf4.0ccd.c9e0  3       Disabled       Down          40       *1/7 (13 dBm)   (5,1)                               Local  '
param= 'AP8C88.8176.CC30                  ecf4.0cce.0780  3       Enabled        Up            40       ~3/8 (11 dBm)   (125,121)                           Local'
pattern =     r'[*~](\d+)'

match = re.search(pattern, param1)
print(match.group(1))  

pattern  = r'(Up|Down)\s+(\d+)'

match = re.search(pattern, param)
if match:
    default_width = match.group(2)  
    print(f"default_width: {default_width}")
else:
    print("No match found")
    
import ipaddress

def is_valid_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except ValueError:
        return False

print(is_valid_ipv4("256.100.50.25"))  # False

import re

str1 = 'my bluetooth 11:22:33:44:55 eng'
match = re.search(r'(\d{2}:\d{2}:\d{2}:\d{2}:\d{2})', str1)

if match:
    print(match.group(1))  # Output: 11:22:33:44
else:
    print("No match found")

    