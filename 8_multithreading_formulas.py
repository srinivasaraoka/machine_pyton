
1. Import threading module:
   import threading

2. Creating a simple thread:
   t = threading.Thread(target=some_function)

3. Starting a thread:
   t.start()

4. Waiting for a thread to complete:
   t.join()

5. Creating a thread with arguments:
   t = threading.Thread(target=some_function, args=(arg1, arg2))

6. Thread with kwargs:
   t = threading.Thread(target=some_function, kwargs={'arg': val})

7. Creating multiple threads in a loop:
   threads = [threading.Thread(target=func, args=(i,)) for i in range(5)]

8. Checking if thread is alive:
   t.is_alive()

9. Thread naming:
   t = threading.Thread(name="Worker1", target=func)

10. Get current thread name:
    threading.current_thread().name

11. Using Lock:
    lock = threading.Lock()

12. Acquiring and releasing Lock:
    lock.acquire()
    # critical section
    lock.release()

13. Using Lock with context manager:
    with lock:
        # critical section

14. Using RLock (reentrant lock):
    rlock = threading.RLock()

15. Using Semaphore:
    sem = threading.Semaphore(value=3)

16. Using Event to signal threads:
    event = threading.Event()

17. Setting and clearing event:
    event.set(), event.clear()

18. Waiting for event:
    event.wait()

19. Using Timer:
    t = threading.Timer(5.0, func)

20. Thread-safe Queue:
    from queue import Queue

21. Producer-consumer pattern:
    def producer(q): q.put(item)
    def consumer(q): item = q.get()

22. Using Condition object:
    cond = threading.Condition()

23. Waiting with Condition:
    with cond:
        cond.wait()

24. Notifying with Condition:
    with cond:
        cond.notify()

25. Thread subclassing:
    class MyThread(threading.Thread):
        def run(self):
            print("Running")

26. Daemon thread:
    t.daemon = True

27. Check if daemon:
    t.isDaemon()

28. Enumerate threads:
    threading.enumerate()

29. Thread count:
    threading.active_count()

30. Naming threads manually:
    threading.current_thread().setName("MyThread")

31. Thread-local storage:
    data = threading.local()

32. Assigning thread-local variable:
    data.value = 42

33. Reading thread-local variable:
    print(data.value)

34. Use of Barrier:
    barrier = threading.Barrier(3)

35. Waiting on Barrier:
    barrier.wait()

36. Exception handling in threads:
    try: ... except Exception as e: ...

37. Setting thread priority (not directly supported in Python)

38. Joining multiple threads:
    for t in threads: t.join()

39. Using ThreadPoolExecutor:
    from concurrent.futures import ThreadPoolExecutor

40. Submitting task to pool:
    with ThreadPoolExecutor() as executor:
        executor.submit(func, arg)
