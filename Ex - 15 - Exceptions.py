"""
    Python provides two very important features to handle any unexpected error in your Python programs
    and to add debugging capabilities! Exception Handling − This would be covered in this script.
    a) Exception Handling/Standard Exceptions.
    b) Assertions.
"""

import os
import sys


# IOError
try:
    file_handling = open("txt")  # To test this script, give a wrong file name. You can see exception!
    file_handling.write("Modified via Script implemented for Python exceptions!")

except IOError:
    print("Error: Can't read the or locate the file/file path")

else:
    print("Modifications are applied to this Python file, check the same")
    file_handling.close()


# FileNotFoundError
try:
    file_handling = open("txt")  # To test this script, give a wrong file name. You can see exception!
    file_handling.write("Modified via Script implemented for Python exceptions!")

except (IOError, FileNotFoundError):
    print("Error: Can't read the or locate the file/file path. FileNotFoundError")

else:
    print("Modifications are applied to this Python file, check the same")
    file_handling.close()


# ZeroDivisionError
one_input = int(input("Enter first number = "))
second_input = int(input("Enter second number = "))

while True:
    try:
        print("{0} / {1} is {2}".format(one_input, second_input, one_input/second_input))
        break

    except ZeroDivisionError:
        print("Cannot divide via Zero")
        one_input = int(input("Enter first number = "))
        second_input = int(input("Enter second number = "))

# ValueError
try:
    user_age = int(input("Enter your age = "))
    if user_age < 0 or user_age > 80:

        raise ValueError

except ValueError:
    print("Invalid Age!")

# RuntimeError
# We are using import os and import sys modules for this scenario!
try:
    os.mkdir(":\\python_exception")  # Forcefully not giving C:\ path
    print("New Directory Created")
    print(sys.copyright)

    raise (OSError, RuntimeError)

except (OSError, RuntimeError, SystemError):
    print("Exceptions Noticed. Check OS & SYS modules accordingly!")

# IndexError
sample_list = ['Ram', 'Sita', 'Hanuman', 'Lakshman', 100, 200, 300, 400]
print("Sample List Length =", sample_list.__len__())
try:
    index_10_value = sample_list[10]
    print("Index 10's Value =", index_10_value)

    raise IndexError

except IndexError as IE:
    print("Looks like, Index error! Can the index value passed in the try block.")
    print("Exception's Class Info =", IE.__class__)

# Cleanup Code (FINALLY BLOCK)
another_sample_list = [11, 22, 33, 44, 'Delhi', 'Mysore', 'Chennai', 'Pune']
print("Another Sample List Length =", another_sample_list.__len__())
try:
    get_index_value = another_sample_list[10]
    print("Index 10's Value =", get_index_value)

    raise IndexError

except IndexError as IE:
    print("Looks like, Index error! Can the index value passed in the try block.")
    print("Exception's Class Info =", IE.__class__)

finally:
    if IndexError:
        get_index_value = another_sample_list[4]
        print("Getting Index Value =", get_index_value)
        print("Finally Block Executed !")
