"""
    Running several threads is similar to running several different programs concurrently, by providing below benefits -

        Multiple threads within a process share the same data space with the main thread and
        can therefore share information or communicate with each other more easily than if they were separate processes.

        Threads sometimes called light-weight processes and they do not require much memory overhead.
        They are cheaper than processes.

        A thread has a beginning, an execution sequence, and a conclusion.
        It has an instruction pointer that keeps track of where within its context it is currently running.

        It can be pre-empted (interrupted). It can temporarily be put on hold (also known as sleeping) while other
        threads are running - this is called yielding.


        The threading module provided with Python includes a simple-to-implement locking mechanism that allows you to
        synchronize threads. A new lock is created by calling the Lock() method, which returns the new lock.
        The acquire(blocking) method of the new lock object is used to force threads to run synchronously.
        The optional blocking parameter enables you to control whether the thread waits to acquire the lock.
        If blocking is set to 0, the thread returns immediately with a 0 value if the lock cannot be acquired
        and with a 1 if the lock was acquired. If blocking is set to 1, the thread blocks and wait for
        the lock to be released. The release() method of the new lock object is used to release the lock when
        it is no longer required.
"""
# Generic Syntax
# thread.start_new_thread ( function, args[, kwargs] )

import threading
import time

# Example 1
# Define a function for the thread


def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(thread_name, time.ctime(time.time()))

# Create 2 threads as follows
try:
    threading._start_new_thread(print_time, ('Thread - 1', 2,))
    threading._start_new_thread(print_time, ('Thread - 2', 4,))
except:
    print("Error : Unable to start thread!")


# Example 2
# Threading Module! Define a function for the thread
exit_flag = 0


class MyNewThread(threading.Thread):

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self._thread_id = thread_id
        self._name = name
        self._counter = counter

    def run(self):
        print("Starting =", self._name)
        print_time(self._name, 5, self._counter)
        print("Exiting =", self._name)


def print_time(thread_name, counter, delay):
    while counter:
        if exit_flag:
            thread_name.exit()
        time.sleep(delay)
        print("%s: %s" % (thread_name, time.ctime(time.time())))
        counter -= 1

# Create New Threads
thread_one = MyNewThread(1, "Thread - 1", 1)
thread_two = MyNewThread(2, "Thread - 2", 2)

# Start New Threads
thread_one.start()
thread_two.start()


# Example 3
# Synchronizing Threads

class SimpleSyncThread(threading.Thread):

    def __init__(self, threads_id, names, counters):
        threading.Thread.__init__(self)
        self._threads_id = threads_id
        self._names = names
        self._counters = counters

    def run(self):
        print("Starting Thread -", self._names)
        print_time(self._names, 3, self._counters)


def printing_time(threads_name, delays, counters):
    while counters:
        time.sleep(delays)
        print("%s: %s" % (threads_name, time.ctime(time.time())))
        counters -= 1

thread_lock = threading.Lock()
sync_threads = []

# Creating Threads
thread_01 = SimpleSyncThread(1, "Sync-Thread-01", 1)
thread_02 = SimpleSyncThread(2, "Sync-Thread-02", 2)

# Start Threads
thread_01.start()
thread_02.start()

# Appending Threads
sync_threads.append(thread_01)
sync_threads.append(thread_02)

# Wait for all threads to complete
for thread in sync_threads:
    thread.join()
print("Exiting Main Thread")
