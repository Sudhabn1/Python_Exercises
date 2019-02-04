"""
    Python provides two very important features to handle any unexpected error in your Python programs
    and to add debugging capabilities! Exception Handling − This would be covered in this script.
    a) Exception Handling/Standard Exceptions.
    b) Assertions.
"""

# IO Error
try:
    file_handling = open("txt")  # To test this script, give a wrong file name. You can see exception!
    file_handling.write("Modified via Script implemented for Python exceptions!")
except IOError:
    print("Error: Can't read the or locate the file/file path")
else:
    print("Modifications are applied to this Python file, check the same")
    file_handling.close()

# File Not Found Error
try:
    file_handling = open("txt")  # To test this script, give a wrong file name. You can see exception!
    file_handling.write("Modified via Script implemented for Python exceptions!")
except (IOError, FileNotFoundError):
    print("Error: Can't read the or locate the file/file path. FileNotFoundError")
else:
    print("Modifications are applied to this Python file, check the same")
    file_handling.close()
