"""
Python threading allows you to have different parts of your, 
program run concurrently and can simplify your desig

What threads are
How to create threads and wait for them to finish
How to use a ThreadPoolExecutor
How to avoid race conditions
How to use the common tools that Python threading provides

https://realpython.com/intro-to-python-threading/

"""


import threading
import time

def print_numbers(thread_name, delay):
    """
    Function to print numbers from 1 to 5 with a delay
    """
    for i in range(1, 6):
        time.sleep(delay)
        print(f"{thread_name}: {i}")

# Create two threads
thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 1))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 0.5))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Exiting Main Thread")
