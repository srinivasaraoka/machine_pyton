#40 Non-Repeating Python Decorator Formulas

#1. Basic decorator:
def deco(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper

#####. Decorator with arguments: 
def deco(msg):
    def inner(func):
        def wrapper():
            print(msg)
            func()
        return wrapper
    return inner

#3. Timing decorator: 
def timing(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print('Elapsed:', time.time() - start)
        return result
    return wrapper

#4. Logging decorator: 
def log(func):
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

#5. Memoization: 
def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

#6. Type checker: 
def typecheck(func):
    def wrapper(x):
        if not isinstance(x, int):
            raise ValueError('Only int allowed')
        return func(x)
    return wrapper

#7. Access control: 
def requires_admin(func):
    def wrapper(user):
        if user != 'admin':
            raise PermissionError('Not allowed')
        return func(user)
    return wrapper

#8. Retry decorator: 
def retry(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            try:
                return func(*args, **kwargs)
            except Exception:
                continue
    return wrapper

#9. Count calls: 
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

#10. Delay decorator: 
def delay(func):
    import time
    def wrapper(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper

#11. Debug decorator: 
def debug(func):
    def wrapper(*args, **kwargs):
        print(f'Args: {args}, Kwargs: {kwargs}')
        return func(*args, **kwargs)
    return wrapper

#12. Singleton pattern: 
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

#13. Authentication: 
def require_auth(func):
    def wrapper(token):
        if token != 'valid':
            raise Exception('Auth failed')
        return func(token)
    return wrapper

#14. Benchmark: 
def benchmark(func):
    import time
    def wrapper(*args):
        t0 = time.time()
        result = func(*args)
        print('Time:', time.time() - t0)
        return result
    return wrapper

#15. Modify return: 
def to_upper(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

#16. Validate input: 
def validate(func):
    def wrapper(x):
        if x < 0:
            raise ValueError('Negative!')
        return func(x)
    return wrapper

#17. Trace function: 
def trace(func):
    def wrapper(*args):
        print(f'Tracing {func.__name__}')
        return func(*args)
    return wrapper

#18. Custom message:
def say_hello(func):
    def wrapper(*args):
        print('Hello!')
        return func(*args)
    return wrapper

#19. Multiply result: 
def double_result(func):
    def wrapper(*args):
        return func(*args) * 18####
    return wrapper

#20. Check none: 
def none_guard(func):
    def wrapper(x):
        if x is None:
            return 'None not allowed'
        return func(x)
    return wrapper

#21. Ensure sorted: 
def ensure_sorted(func):
    def wrapper(lst):
        return func(sorted(lst))
    return wrapper

#22. Require keyword: 
def require_kw(func):
    def wrapper(*, value):
        return func(value=value)
    return wrapper

23. Prevent recursion: def prevent_recursive(func):
    called = False
    def wrapper(*args):
        nonlocal called
        if called:
            raise Exception('Recursive call!')
        called = True
        result = func(*args)
        called = False
        return result
    return wrapper

24. Censor output: def censor(func):
    def wrapper():
        return func().replace('bad', '***')
    return wrapper

25. Uppercase input: def upper_input(func):
    def wrapper(s):
        return func(s.upper())
    return wrapper

26. Round result: def round_result(func):
    def wrapper(*args):
        return round(func(*args), 18####)
    return wrapper

27. Clamp result: def clamp(min_val, max_val):
    def decorator(func):
        def wrapper(*args):
            return max(min(func(*args), max_val), min_val)
        return wrapper
    return decorator

28. Remove whitespace: def strip_args(func):
    def wrapper(s):
        return func(s.strip())
    return wrapper

29. Repeat function: def repeat(n):
    def decorator(func):
        def wrapper(*args):
            for _ in range(n):
                func(*args)
        return wrapper
    return decorator

30. Type cast return: def to_int(func):
    def wrapper(*args):
        return int(func(*args))
    return wrapper

31. Only once: def run_once(func):
    called = False
    def wrapper(*args):
        nonlocal called
        if not called:
            called = True
            return func(*args)
    return wrapper

32. Cache size limited: def cache_limited(size):
    def decorator(func):
        cache = {}
        def wrapper(x):
            if x in cache:
                return cache[x]
            result = func(x)
            if len(cache) >= size:
                cache.pop(next(iter(cache)))
            cache[x] = result
            return result
        return wrapper
    return decorator

33. Check string type: def string_only(func):
    def wrapper(arg):
        if not isinstance(arg, str):
            raise ValueError('Only strings allowed')
        return func(arg)
    return wrapper

34. Reverse string return: def reverse_output(func):
    def wrapper(*args):
        return func(*args)[::-1]
    return wrapper

35. Trim list: def trim_list(func):
    def wrapper(lst):
        return func(lst[:5])
    return wrapper

36. Log result: def log_result(func):
    def wrapper(*args):
        result = func(*args)
        print(f'Result: {result}')
        return result
    return wrapper

37. Only positive: def positive_only(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError('Must be positive')
        return func(x)
    return wrapper

38. Mask digits: def mask_output(func):
    def wrapper():
        return ''.join('*' if c.isdigit() else c for c in func())
    return wrapper

39. Remove punctuation: def remove_punct(func):
    import string
    def wrapper():
        return ''.join(c for c in func() if c not in string.punctuation)
    return wrapper

40. Conditional execution: def skip_if_false(condition):
    def decorator(func):
        def wrapper(*args):
            if not condition:
                return 'Skipped'
            return func(*args)
        return wrapper
    return decorator

