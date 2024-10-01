from threading import *
from time import sleep

import threading
import time

'''
Multithreading in Python refers to the concurrent execution of multiple threads 
within a single process. A thread is the smallest unit of a process, and 
multithreading allows a program to perform multiple tasks simultaneously, 
improving efficiency, especially in I/O-bound applications like network requests, 
file handling, and more.
Multithreading in Python is a programming technique that allows
multiple threads (smaller units of a process) to run concurrently 
within a single process. Each thread operates independently but 
shares the same memory space. This can lead to more efficient 
execution of tasks, particularly when you need to perform I/O-bound 
operations or manage concurrent tasks.

Key Concepts of Multithreading
Thread: A thread is the smallest unit of execution within a process. 
Threads within the same process share the same memory space and 
resources but execute independently.
Concurrency: Multithreading enables concurrent execution of code, 
meaning multiple threads can make progress on tasks simultaneously.

Parallelism: In the context of multithreading, parallelism refers to 
executing multiple threads at the same time on multiple processors or 
cores. However, Python's Global Interpreter Lock (GIL) affects 
parallel execution in CPython (the standard Python implementation), 
limiting true parallelism for CPU-bound tasks.



Key Concepts of Multithreading:
Thread: A thread is a lightweight process, and multiple threads within a single process 
share the same memory space.
Concurrency: The concept of executing multiple tasks (threads) simultaneously, giving 
the illusion that they're running at the same time. In Python, due to the Global Interpreter Lock (GIL), 
only one thread can execute Python bytecode at a time, but I/O-bound tasks can benefit from threading.
Why Use Multithreading?
Multithreading is useful for:

Performing multiple I/O-bound tasks in parallel (e.g., reading/writing files, network requests).
Improving responsiveness in applications like GUIs, where you want to keep the interface responsive while handling background tasks.
Better utilization of multiple cores in some scenarios (though Python's GIL limits CPU-bound tasks).
How to Use Multithreading in Python
Python provides the threading module to work with threads. Here's a simple example:

Key Functions in the threading Module:
threading.Thread(target=function) : Creates a new thread to run the specified function.
thread.start() : Starts the thread.
thread.join() : Waits for the thread to finish execution.
threading.active_count() : Returns the number of active threads.
threading.current_thread() : Returns the current thread object.
Global Interpreter Lock (GIL)
In CPython (the default Python implementation), the GIL prevents multiple native threads from executing Python bytecodes simultaneously. This means that CPU-bound tasks (tasks that require heavy computation) may not see much improvement from multithreading. For CPU-bound tasks, multiprocessing (using multiple processes instead of threads) is often preferred.

When to Use Multithreading:
I/O-bound tasks (e.g., file I/O, network I/O): Multithreading can improve performance significantly.
Non-blocking operations: For tasks where you can allow the system to switch between threads without waiting for one to finish.
Limitations:
GIL: As mentioned, CPU-bound tasks might not benefit as much from multithreading due to the GIL.
Race conditions: Multiple threads accessing shared resources may cause unexpected behavior if proper locking mechanisms are not used (e.g., using threading.Lock).
For CPU-bound tasks, using the multiprocessing module (which uses separate processes rather than threads) is usually a better option

'''


'''
Python's Global Interpreter Lock (GIL)
In CPython, the Global Interpreter Lock (GIL) is a mutex that protects 
access to Python objects, preventing multiple native threads from 
executing Python bytecodes simultaneously. This means that while 
Python threads can be useful for I/O-bound tasks, they don't provide 
true parallelism for CPU-bound tasks. For CPU-bound tasks, 
multiprocessing or alternative implementations like Jython or 
IronPython may be more appropriate.

Using the threading Module
Python provides the threading module to facilitate multithreading. 
Here's a basic example of how to use it:


'''
# Function to be run in a thread
def print_numbers(name):
    for i in range(5):
        print(i)
        print(name)
        time.sleep(1)

# Function to be run in a thread
def print_letters(age, hight):
    for letter in 'abcde':
        print(letter)
        print("age=",age, hight)
        time.sleep(1.2)

# Create thread objects
thread1 = threading.Thread(target=print_numbers, args=('jai sri ram',))
thread2 = threading.Thread(target=print_letters, kwargs={'age':28, 'hight':5.4})

# Start the threads
thread1.setDaemon(True) #background run
thread1.start()
thread2.start()
l= enumerate()
print(l)
for t in l:
    print("t.name is",t.name, thread1.is_alive(), thread2.is_alive())
# Wait for both threads to complete
thread1.join()
thread2.join() #if thread wants wait util before thread executed
print("thread1", current_thread().ident)
l= enumerate()
print(l)
for t in l:
    print(t.name, thread1.is_alive())
    
print("thread1.daemon",thread1.isDaemon())    
#print("Threads have finished execution")
'''
In this example:

print_numbers and print_letters are functions that will be executed in separate 
threads.
threading.Thread is used to create thread objects, specifying the target 
functions.
start() begins the execution of the threads.
join() ensures that the main program waits for both threads to complete before 
continuing.

Thread Safety
When using threads, it"s crucial to manage shared resources to avoid race 
conditions or inconsistent states. Thread synchronization mechanisms provided by 
the threading module include:

Locks: Ensure that only one thread can access a resource at a time.
python

'''

lock = threading.Lock()

def thread_safe_function():
    with lock:
        assert lock # I writen this code for removing bug
        # Critical section of code


#Events: Allow threads to signal each other about events.
#Conditions: Allow threads to wait for certain conditions to occur.
#Semaphores: Control access to a resource with a limited number of slots.
#Example: Using a Lock

# Shared resource
shared_resource = 0

# Lock object

lock = threading.Lock()

def increment():
    global shared_resource
    with lock:
        for _ in range(1000):
            shared_resource += 1

threads = []

# Create and start threads
for _ in range(5):
    thread = threading.Thread(target=increment)
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print(f"Final value of shared_resource: {shared_resource}")

'''
Thread locks, also known simply as locks or mutexes (short for mutual exclusions), 
are synchronization primitives used in multithreaded programming to ensure 
that only one thread can access a particular piece of code or data at a time.
They are essential for preventing race conditions, where the outcome of a 
program depends on the unpredictable timing of multiple threads.

Uses of Thread Locks:
Protecting Shared Resources:

When multiple threads need to read from or write to shared resources 
(e.g., variables, files, databases), locks ensure that only one thread can 
modify the resource at a time. This prevents inconsistencies and data 
corruption.
Example: If two threads try to increment the same counter simultaneously 
without a lock, the final value might be incorrect due to race conditions.
Ensuring Data Consistency:

Locks help maintain data consistency by ensuring that complex operations on
 shared data (like updating multiple variables) are completed by one thread 
 without interference from others.
Example: In banking software, transferring money between accounts involves 
subtracting from one account and adding to another. A lock ensures that this 
operation is atomic and no other thread can intervene during the process.
Preventing Deadlock:

While locks prevent race conditions, they can also lead to deadlocks if not 
used carefully. A deadlock occurs when two or more threads are waiting for each 
other to release locks, causing them to be stuck indefinitely. Proper design 
and lock hierarchy are necessary to avoid this.
Example: Thread A locks Resource 1 and waits for Resource 2, while Thread B 
locks Resource 2 and waits for Resource 1. Both threads are stuck waiting 
for each other.

Coordination Between Threads:
Locks can be used to coordinate the execution order of threads, ensuring 
that certain operations are completed in a specific order.
Example: In a producer-consumer problem, locks ensure that the producer 
doesn’t 
overwrite data that the consumer has not yet processed.
Improving Performance:

In cases where some operations need to be serialized but others can run in 
parallel, using locks allows developers to maximize performance by locking 
only the critical sections of code, rather than the entire process.
Example: In a web server, locks can be used to control access to logging or 
session management, allowing multiple requests to be processed concurrently 
while ensuring that logs or session data are updated correctly.
'''

#import threading

# Shared resource
counter = 0

# Create a lock object
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(1000):
        # Acquire the lock before modifying the shared resource
        with lock:
            counter += 1

# Create multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")

'''
Explanation:
Lock Object: lock = threading.Lock() creates a lock object.
Critical Section: The with lock: block ensures that only one thread can execute 
the counter += 1 statement at a time.
Thread Synchronization: The join() method ensures that the main thread waits for 
all threads to finish before printing the final counter value.
Without the lock, the final counter value would likely be incorrect due to race 
conditions, as multiple threads could increment the counter simultaneously. With 
the lock, the counter increments correctly, one thread at a time.

In summary, thread locks are crucial in multithreaded programming to protect 
shared resources, ensure data consistency, coordinate thread execution, and 
improve performance while avoiding race conditions and deadlocks.
'''
#Daemon Thread    background run thread(to provide support for 
# nondeamon thred(main thread))
#EX:garbage collector
class Hello(Thread):
    def run(self):
        current_thread().setName("Hello_1 thread")
        for x in range(8):
            print("hello")
            print(current_thread().getName()) 
            sleep(1.1)

class Hi(Thread):
    def run(self):
        for x in range(5):
            print("hi")
            print(current_thread().getName()) 
            sleep(1.1)            

t1= Hello()
t2= Hi()
t1.start()
t2.start()
t1.join(10)
t2.join() # main thread will wait for to compleat t1, t2 threads
#print(current_thread().getName()) #Note: total 3 threads(t1, t2, main)
print("bye")
print(t1.getName())
print(t2.getName())

