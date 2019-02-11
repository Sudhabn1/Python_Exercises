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
#while 1:
#    pass


# Example 2
# Define a function for the thread
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
