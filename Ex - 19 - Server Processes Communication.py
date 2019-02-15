"""
    Server process : Whenever a python program starts, a server process is also started.
    From there on, whenever a new process is needed, the parent process connects to the server and requests it to
    fork a new process. A server process can hold Python objects and allows other processes to
    manipulate them using proxies. Multiprocessing module provides a Manager class which controls a server process.
    Hence, managers provide a way to create data which can be shared between different processes.
"""
import multiprocessing

# Example 1 Manager Class


def print_records(records):
    """
        function to print record(tuples) in records(list)
    """
    for record in records:
        print("Name = {0}\nScore = {1}\n".format(record[0], record[1]))


def insert_record(record, records):
    """
        function to add a new record to records(list)
    """
    records.append(record)
    print()
    print("New Record Included\n")


if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        records = manager.list([('Sam', 95), ('Ram', 97), ('Niki', 91), ('Joe', 84), ('Dave', 77)])
        new_record = ('Carl', 93)

        # Creating new processes
        process_01 = multiprocessing.Process(target=insert_record(new_record, records))
        process_02 = multiprocessing.Process(target=print_records(records))

        # Start processes
        process_01.start()
        process_02.start()

        # Join processes
        process_01.join()
        process_02.join()

print("--------------------------")

# Example 2 Queue & Pipe

# Queue : A simple way to communicate between process with multiprocessing is to use a Queue to pass messages
# back and forth. Any Python object can pass through a Queue.
# Note: The multiprocessing.Queue class is a near clone of queue.Queue.

# Pipes : A pipe can have only two endpoints. Hence, it is preferred over queue when only
# two-way communication is required. Multiprocessing module provides Pipe() function which returns a pair
# of connection objects connected by a pipe. The two connection objects returned by Pipe()
# represent the two ends of the pipe. Each connection object has send() and recv() methods (among others).


def square_list(mylist, myqueue):
    """
        function to square a given list
    """
    for num in mylist:
        myqueue.put(num * num)


def print_queue(myqueue):
    print("Queue Elements -")
    while not myqueue.empty():
        print(myqueue.get())
    print("Queue is now empty!")


if __name__ == "__main__":
    mylist = [1, 4, 7, 9]
    myqueue = multiprocessing.Queue()

    # Creating processes
    prc1 = multiprocessing.Process(target=square_list(mylist, myqueue))
    prc2 = multiprocessing.Process(target=print_queue(myqueue))

    # Running processes
    prc1.start()
    prc2.start()

    # Joining processes
    prc1.join()
    prc2.join()

print("--------------------------")


# Example 3 Queue & Pipe


def sender(conn, msgs):
    for msg in msgs:
        conn.send(msg)
        print("Sent the message - {}".format(msg))
    conn.close()


def receiver(conn):
    while 1:
        msg = conn.recv()
        if msg == "End":
            break
        print("Received the message - {}".format(msg))

if __name__ == "__main__":
    msgs = ["Hello", "Hey", "Good", "Bad", "End"]

    # Creating a pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    # Creating a new process
    pr_01 = multiprocessing.Process(target=sender(parent_conn, msgs))
    pr_02 = multiprocessing.Process(target=receiver(child_conn))

    # Starting process
    pr_01.start()
    pr_02.start()

    # Wait until processes finish
    pr_01.join()
    pr_02.join()
