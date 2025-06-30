40 Non-Repeating Lambda Formulas in Python

1. Square a number: lambda x: x**2
2. Add two numbers: lambda a, b: a + b
3. Maximum of two numbers: lambda a, b: a if a > b else b
4. Check even number: lambda x: x % 2 == 0
5. Absolute value: lambda x: x if x >= 0 else -x
6. Multiply elements of list: lambda lst: [x*2 for x in lst]
7. Reverse a string: lambda s: s[::-1]
8. Length of string: lambda s: len(s)
9. Convert to uppercase: lambda s: s.upper()
10. Check palindrome: lambda s: s == s[::-1]
11. Factorial using reduce: lambda n: reduce(lambda x, y: x*y, range(1, n+1))
12. Count vowels: lambda s: sum(1 for c in s.lower() if c in 'aeiou')
13. Get last element: lambda lst: lst[-1]
14. Filter even numbers: lambda lst: list(filter(lambda x: x % 2 == 0, lst))
15. Map square to list: lambda lst: list(map(lambda x: x**2, lst))
16. Sum of list: lambda lst: sum(lst)
17. Sort by second element: lambda lst: sorted(lst, key=lambda x: x[1])
18. Check substring: lambda sub, s: sub in s
19. Get initials: lambda name: ''.join(word[0] for word in name.split())
20. Strip spaces: lambda s: s.strip()
21. Swap case: lambda s: s.swapcase()
22. Square root: lambda x: x**0.5
23. Cube of a number: lambda x: x**3
24. Flatten a list: lambda lst: [item for sublist in lst for item in sublist]
25. Check prime: lambda x: all(x % i != 0 for i in range(2, int(x**0.5)+1)) and x > 1
26. Repeat string n times: lambda s, n: s * n
27. Remove duplicates: lambda lst: list(dict.fromkeys(lst))
28. Join list to string: lambda lst: ''.join(lst)
29. Convert string to int: lambda s: int(s)
30. Filter strings from list: lambda lst: list(filter(lambda x: isinstance(x, str), lst))
31. Check leap year: lambda y: y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
32. Reverse list: lambda lst: lst[::-1]
33. Max in list: lambda lst: max(lst)
34. Min in list: lambda lst: min(lst)
35. Capitalize words: lambda s: s.title()
36. Count words: lambda s: len(s.split())
37. Replace spaces with hyphen: lambda s: s.replace(' ', '-')
38. Filter positive numbers: lambda lst: list(filter(lambda x: x > 0, lst))
39. Find intersection: lambda a, b: list(set(a) & set(b))
40. Merge two dicts: lambda d1, d2: {**d1, **d2}
