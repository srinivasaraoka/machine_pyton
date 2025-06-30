import logging
import logger

logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("custom_logger")

#Dictionary
"""A dictionary in Python is a built-in data structure used to store key-value pairs. It's very efficient for looking up values based on a key, """
#dict.setdefault(key, default_value)
#update(), get() 
# if we want value ,dic.get(key)
# take pervious value = dic1[key]
#list1= list(dic1.values())
#if we want assine value dic1[key]= value
#dic1.update({key:value})
#sorted_dic_by_keys= dict(sorted(dic1.items()))
#sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1]))
#Sorting in Descending Order
#sorted_by_values = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
#fuctionatilality of get() and update() in dictionary

#get() used to get the value of the key
#update() used to add new key and value to the dictionary

'''
The difference between value = dic2[ele] and value = dic2.get(key) in Python lies in how they handle missing keys in a dictionary.

1. value = dic2[ele]
This directly accesses the value associated with ele in the dictionary dic2.
If the key ele does not exist, it raises a KeyError

Key Differences:
Feature	                      dic2[ele]	          dic2.get(key)
Error on missing key	      Yes (KeyError)	  No (returns None or default value)
Performance	                  Slightly faster	  Slightly slower (due to extra function call)
Default value support	             No	          Yes (dic2.get(key, default))
When to Use What?
Use dic2[ele] only if you're sure the key exists.
Use dic2.get(key) if there's a chance the key might be missing, and you want to avoid errors.

merged = dict1 | dict2
merged = {**dict1, **dict2}

. Explain the difference between dict.get(key) and direct access dict[key].
dict.get(key) → returns None if key does not exist (or a custom default).

dict[key] → raises KeyError if key does not exist.

sorted_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

pop(key) → remove the specified key.

popitem() → remove the last inserted key-value pair (in Python 3.7+ dictionaries are ordered).

for char in s:
        count[char] = count.get(char, 0) + 1
        
for word in words:
        key = ''.join(sorted(word))
        anagrams.setdefault(key, []).append(word)        

words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
anagrams = {}
for word in words:
        key = ''.join(sorted(word))
        anagrams.setdefault(key, []).append(word)   
               
1,give me more information about the setdefault?

Of course! Let’s talk about setdefault() very clearly and in simple language:

🔵 What is setdefault() in Python dictionary?
setdefault() tries to get a value for a given key.

If the key exists, it returns the value.

If the key does NOT exist, it:

Creates the key with a default value you provide,

Then returns that default value.

🔵 Syntax:
dict.setdefault(key, default_value)
key → Key you want to find.

default_value → (Optional) If the key doesn’t exist, create it with this value.
(If you don’t give, it defaults to None.)

🔵 Example 1: When key exists

d = {'a': 100, 'b': 200}
result = d.setdefault('a', 500)
print(result)   # 100
print(d)        # {'a': 100, 'b': 200}
✅ 'a' already exists, so it just returns its value (100).
✅ Dictionary stays same.

🔵 Example 2: When key does NOT exist

d = {'a': 100, 'b': 200}
result = d.setdefault('c', 300)
print(result)   # 300
print(d)        # {'a': 100, 'b': 200, 'c': 300}
✅ 'c' was missing, so it creates 'c' with value 300.

🔵 Real-World Usage (Most important in interviews)
setdefault() is very useful when building grouped data like:

Grouping words, anagrams, frequencies, etc.
Example: Grouping fruits by first letter
'''
person = {"name": "Srinivas"}       # Initial dictionary
person['age'] = 20                  # Adds 'age': 20
value = person.setdefault("age", 25)  # Key 'age' exists, so returns 20, no update
value = person.setdefault("age", 30)  # Again, 'age' exists, so still returns 20
print(value)
print("person", person) # {'name': 'Srinivas', 'age': 20}



fruits = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
grouped = {}

for fruit in fruits:
    first_letter = fruit[0]
    grouped.setdefault(first_letter, []).append(fruit)

print(grouped)
'''
{
  'a': ['apple', 'apricot'],
  'b': ['banana', 'blueberry'],
  'c': ['cherry']
}
✅ setdefault(first_letter, []) means:

If first letter not found, create an empty list.

Then .append(fruit) into it.

🔵 Why setdefault() is powerful?

Feature	Without                             setdefault()	With setdefault()
You need to check manually if key exists	Yes	            No
Code becomes longer                       	Yes	            No
More prone to bugs	                        Yes           	No
Cleaner and safer	                         No	            Yes
🔥 Quick Comparison:
Without setdefault():
'''
# my_dict = {1:'a', 2:'b', 3:'c'}
# if key not in my_dict:
#     my_dict[key] = []
# my_dict[key].append(value)
'''
With setdefault():

my_dict.setdefault(key, []).append(value)
Much simpler!

🛑 Small Caution
If the default_value is a mutable object (like list, dict), and you reuse it across keys, it can cause bugs.

So usually use [] directly inside setdefault() without sharing between keys.

🔥 Mini Practice:
Question:
Given a list ["red", "blue", "black", "brown", "red", "blue"],
use setdefault() to group colors by their starting letter!

'''

s3={1:"a",2:"b"}
print(s3.get(1))
#a
print(s3)
print(s3.update({3:"c", 4:'d'}))
logging.info(f"{s3}")
logging.info("%s", s3) 
logger.debug("%s",s3)
#{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
s3[5]='e'
logging.info("{%s},adding new value", s3)
#{1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
s3[1]='e'
print("changing value",s3)
#{1: 'e', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}

for key,value in s3.items():
    print(key,'=', value, end=' ')

#1 = e 2 = b 3 = c 4 = d 5 = e 1

for key in s3.keys():
    print(key)        
dic={'a':[1,2,3],'b':[4,5,6]}
print('# dic[b][1]=, dic[b]',dic['b'][1], dic['b'])
# dic[b][1]=, dic[b] 5 [4, 5, 6]
for k,v in dic.items():
    if v==[1,2,3]:
        print(key)
dic.update({'city': 'New York', 'job': 'Engineer'})        
#dic.update({'c':[7,5,6], 'd':[8,9,1]})
print(dic)
dic['d3']=[11,12,13]
print("#dic=", dic)

nested_dic={1:{'city':'new york','job':'engineer'},2:{'city':'vijayawada','job':'pythondev'}}
print("#nested_dic", nested_dic)

nested_dic_2={
    1:'a',
    2:{
        'b':'@'

    },
    3:'c'
}
print(nested_dic_2)

#Q1) how to reverse the key and vlue in dictionary        
dic1={'a':1,'b':2,'c':3}
dic2= {v:k for k,v in dic1.items()}
print(dic2)


'''
len= int(input())
list_1=list(map(int, input().strip().split()))
print(list_1)
n = int(input())
list_1 = list(map(int, input().strip().split()))[:n]


for _ in range(int(input())):
        name = input()
        score = float(input())



stu, sub= input().split()
print(sub,stu)
marks=[]
for i in range(int(stu)):
    mark=map(float, input().split())
    marks.append(marks)        
'''
list1=[1,2,3,4]
list2=["a","b","c","d"]
zipped= zip(list1,list2)
print("# list zipped = ",list(zipped))
#list zipped =  [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
zipped= zip(list1,list2)
print("# dic zipped =",dict(zipped))

list1=[1,2,3,4]
list2=["a","b","c","d"]
zipped= zip(list1,list2)
list3, list4 = zip(*zipped)

print(list3)  # Output: (1, 2, 3)
print(list4)  #
#print("# dic zipped =",dict(zipped))

#how to update ele in list in to key and increment value 
def second_most_frequent(nums):
    dic1={}
    value=0
    for ele in nums:
        if ele in dic1:
            value= dic1[ele]
            dic1[ele]= value+1
        else:
            dic1[ele]=1
    #dic1.sort()    
    s=[x for x in dic1.values()]
    print(s)
    s.sort()
    for key, value in dic1.items():
        if value ==s[-2]:
            return key

nums = [1, 2, 3, 4, 2, 3, 4, 3, 4, 4, 5, 5, 5, 5, 6, 6]

print(second_most_frequent(nums))
def flatne_dci(dic, parent_key=''):
    flattend={}
    
    for key,value in dic.items():
        # if parent_key:
        #     new_key=f'{parent_key}.{key}'
        # else:
        #     new_key=key
        new_key=f"{parent_key}.{key}" if parent_key else key
        if isinstance(value,dict):
            flattend.update(flatne_dci(value, new_key))
        else:
            flattend.update(flatne_dci(new_key, value))            
    return flattend

input_dic={'a':1,'b':{"c":2,"d":{'e':3}}}    
#print(flatne_dci(input_dic))

#imp
nums = [4, 3, 2, 4, 1, 3, 2,1,5]
dic2={}
for ele in nums:
    if ele in dic2:
        value=dic2[ele]
        value= value+1
        dic2[ele]=value
    else:
        dic2[ele]=1
logging.info(f"dic2{dic2}")

for key, value in dic2.items():
    if value ==1:
        logging.info(f"unque number is{key}")          

nums=[3,4,5,6]
len1=len(nums)
dic1={}
list1=[]
target=7
for key, value in enumerate(nums):
    dic1[key]=value
       
values= [value for value in dic1.values()]
print(values)
for x in values:
    print(target-x)
    if target-x in values:
        z= target-x
        break
print(z, x)

for key, value in dic1.items():
    if value==z:
        list1.append(key)
    elif value == x:
        list1.append(key)  

logger.info(list1)        

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}
dic3={}
for key, value in dict1.items():
    for key2,value2 in dict2.items():
        if key==key2:
            value3=dict1[key]+dict2[key2]
            print(value3, key, key2)
            dic3[key]=value3
        if key2 not in dict1:
            dic3[key2]= value2   
    if key not in dict2:
        dic3[key]= value
logger.info(dic3)                
s= dic2.values()
print(s)

dic1={1:'a',2:'b',3:'c'}
list1= list(dic1.keys())
list2= list(dic1.values())
dic3={}
for i, j in zip(list1,list2):
    print(i,j)
    dic3[j]= i
print(dic3)    
    
    
def is_balanced(expr):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in expr:
        print("1 char",char)
        if char in mapping.values():
            print("2 char",char)
            stack.append(char)
            print("2.1 stack",stack)
        elif char in mapping:
            print("3 char",char)
            if not stack:
                print("3.1stack nor empty", stack)
                return False
            
            z= stack.pop()
            print("3.1.1 stack ",stack, "mapping ch", mapping[char], "z",z)
            if z != mapping[char]:
                print("3.2mapping char",mapping[char])
                print("3.3 stack",stack)
                return False
            print("3.3.3 stack mapping",stack, mapping[char])  
    return not stack

print(is_balanced("({[}])"))    
# when we get closeing brakets pop the open brackts from stack and check the mapping is correct or not
def valid_brackts(str1):
    stack=[]
    dic1={'}':'{',']':'[',')':'('}
    for ch in str1:
        if ch in dic1.values():
            stack.append(ch)
            print("1 adding the opening brackts in stack", stack)
        elif ch in dic1.keys():
            print("2closing brackts operation")
            if not stack:
                print("closing brackets came so we must check stack not empty, filed with open brackets")
                return False
            else:
                z= stack.pop()
                print("3taking the opening brackets form stack",z)
                if z != dic1[ch]:
                   print("4 here we are checking the openg bracket and closing the bracket", z, dic1[ch])
                   return False
    return not stack
print(valid_brackts("({[}])")) 

def remove_duplicates(input_list): 
    unique_items = list(dict.fromkeys(input_list)) 
    return unique_items 
# Example 
input_list = [1, 2, 2, 3, 4, 4, 5] 
output = remove_duplicates(input_list) 
print(output) # [1, 2, 3, 4, 5]

'''
Method | Use Case | Raises Error if Key Missing
del | Delete specific key | Yes
pop() | Delete and return value | No (if default is provided)
Comprehension | Delete conditionally | No


'''

dic1 =  {'version': {'xe_version': '17.18.01prd9', 'version_short': '17.18', 'platform': 'C9800', 'version': '17.18.1prd9', 'image_id': 'C9800_IOSXE-K9', 'label': 'RELEASE SOFTWARE (fc1)', 'os': 'IOS-XE', 'location': 'IOSXE', 'image_type': 'production image', 'copyright_years': '1986-2025', 'compiled_date': 'Fri 23-May-25 09:59', 'compiled_by': 'mcpre', 'rom': '17.7(3r)', 'hostname': 'WLC', 'uptime': '3 days, 7 hours, 30 minutes', 'uptime_this_cp': '3 days, 7 hours, 32 minutes', 'returned_to_rom_by': 'Image Install ', 'returned_to_rom_at': '06:40:57 UTC Wed May 21 2025', 'system_restarted_at': '23:36:56 UTC Fri May 23 2025', 'system_image': 'bootflash:packages.conf', 'last_reload_reason': 'Image Install', 'license_type': 'Smart License is permanent', 'license_level': 'adventerprise', 'next_reload_license_level': 'adventerprise', 'air_license_level': 'AIR Network Advantage addon AIR DNA Advantage', 'chassis': 'C9800-40-K9', 'main_mem': '3280895', 'processor_type': '1GL', 'rtr_type': 'C9800-40-K9', 'chassis_sn': 'TTM261805WY', 'router_operating_mode': 'Autonomous', 'number_of_intfs': {'Virtual Ethernet': '3', 'Ten Gigabit Ethernet': '4'}, 'mem_size': {'non-volatile configuration': '32768', 'physical': '33554432'}, 'disks': {'bootflash:.': {'disk_size': '26763263', 'type_of_disk': 'eUSB flash'}, 'harddisk:.': {'disk_size': '234365527', 'type_of_disk': 'SATA hard disk'}, 'cloudfs:.': {'disk_size': '0', 'type_of_disk': 'Cloud S3 Storage'}}, 'installation_mode': 'INSTALL', 'curr_config_register': '0x2002', 'switch_num': {'1': {'mac_address': '3C:8B:7F:F4:82:E0'}}}}
dic1={'AP6849.925C.F1F0': {'AP Name': 'AP6849.925C.F1F0', 'Mac Address': '345d.a866.1820', 'Slot': '2', 'Admin State': 'Enabled', 'Oper State': 'Down', 'Width': '20', 'Txpwr': '1(*)', 'Channel': '(133)*', 'Mode': 'Local'}, 'AP6849.92D9.C540': {'AP Name': 'AP6849.92D9.C540', 'Mac Address': '345d.a8a5.b7e0', 'Slot': '2', 'Admin State': 'Enabled', 'Oper State': 'Up', 'Width': '20', 'Txpwr': '~(*)', 'Channel': '(21)', 'Mode': 'Local'}, 'APBC33.4042.2EC0': {'AP Name': 'APBC33.4042.2EC0', 'Mac Address': '8c1e.8007.e7e0', 'Slot': '2', 'Admin State': 'Enabled', 'Oper State': 'Down', 'Width': '20', 'Txpwr': '1(*)', 'Channel': '(5)*', 'Mode': 'Local'}, 'APC414.A26F.66F0': {'AP Name': 'APC414.A26F.66F0', 'Mac Address': 'c414.a26f.6700', 'Slot': '3', 'Admin State': 'Enabled', 'Oper State': 'Down', 'Width': '20', 'Txpwr': '1(*)', 'Channel': '(85)*', 'Mode': 'Local'}, 'APC828.E5E2.03CC': {'AP Name': 'APC828.E5E2.03CC', 'Mac Address': 'c828.e5ee.33f0', 'Slot': '3', 'Admin State': 'Enabled', 'Oper State': 'Down', 'Width': '20', 'Txpwr': '1(*)', 'Channel': '(21)*', 'Mode': 'Local'}, 'AP8C88.8155.F3F0': {'AP Name': 'AP8C88.8155.F3F0', 'Mac Address': 'ecf4.0cb2.c940', 'Slot': '2', 'Admin State': 'Enabled', 'Oper State': 'Down', 'Width': '20', 'Txpwr': '1(*)', 'Channel': '(37)*', 'Mode': 'Local'}}
#print(dic1['version']['version_short'])
data = {
    'AP6849.925C.F1F0': {'AP Name': 'AP6849.925C.F1F0', 'Mac Address': '345d.a866.1820', 'Slot': '2', 'Admin State': 'Enabled', 'Oper State': 'Down', 'Width': '20', 'Txpwr': '1(*)', 'Channel': '(133)*', 'Mode': 'Local'},
    'AP6849.92D9.C540': {'AP Name': 'AP6849.92D9.C540', 'Mac Address': '345d.a8a5.b7e0', 'Slot': '2', 'Admin State': 'Enabled', 'Oper State': 'Up', 'Width': '20', 'Txpwr': '~(*)', 'Channel': '(21)', 'Mode': 'Local'},
    'APBC33.4042.2EC0': {'AP Name': 'APBC33.4042.2EC0', 'Mac Address': '8c1e.8007.e7e0', 'Slot': '2', 'Admin State': 'Enabled', 'Oper State': 'Down', 'Width': '20', 'Txpwr': '1(*)', 'Channel': '(5)*', 'Mode': 'Local'},
    'APC414.A26F.66F0': {'AP Name': 'APC414.A26F.66F0', 'Mac Address': 'c414.a26f.6700', 'Slot': '3', 'Admin State': 'Enabled', 'Oper State': 'Down', 'Width': '20', 'Txpwr': '1(*)', 'Channel': '(85)*', 'Mode': 'Local'},
    'APC828.E5E2.03CC': {'AP Name': 'APC828.E5E2.03CC', 'Mac Address': 'c828.e5ee.33f0', 'Slot': '3', 'Admin State': 'Enabled', 'Oper State': 'Down', 'Width': '20', 'Txpwr': '1(*)', 'Channel': '(21)*', 'Mode': 'Local'},
    'AP8C88.8155.F3F0': {'AP Name': 'AP8C88.8155.F3F0', 'Mac Address': 'ecf4.0cb2.c940', 'Slot': '2', 'Admin State': 'Enabled', 'Oper State': 'Down', 'Width': '20', 'Txpwr': '1(*)', 'Channel': '(37)*', 'Mode': 'Local'}
}

ap_name = 'AP6849.92D9.C540'
if ap_name in data:
    ap_info = data[ap_name]
    width = ap_info.get('Width')
    txpwr = ap_info.get('Txpwr')
    channel = ap_info.get('Channel')
    print(f"Width: {width}, Txpwr: {txpwr}, Channel: {channel}")
else:
    print("AP not found")

                                    