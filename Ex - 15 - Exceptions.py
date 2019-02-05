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

    raise (OSError, RuntimeError)

except (OSError, RuntimeError):
    print("Exceptions Noticed. Check OS & SYS modules accordingly!")
