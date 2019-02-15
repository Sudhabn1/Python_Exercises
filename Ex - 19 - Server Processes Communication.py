"""
    Server process : Whenever a python program starts, a server process is also started.
    From there on, whenever a new process is needed, the parent process connects to the server and requests it to
    fork a new process. A server process can hold Python objects and allows other processes to
    manipulate them using proxies. Multiprocessing module provides a Manager class which controls a server process.
    Hence, managers provide a way to create data which can be shared between different processes.
"""
import multiprocessing


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
