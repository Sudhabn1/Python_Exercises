"""
    A module allows you to logically organize your Python code.
    Grouping related code into a module makes the code easier to understand and use.
    A module is a Python object with arbitrarily named attributes that you can bind and reference.
    Simply, a module is a file consisting of Python code. A module can define functions, classes and variables.
    A module can also include runnable code.
"""

# Import Module (name.py)
import name

# Another Mechanism (You can import module in below format)
# from name import print_name
# from name import *

# Importing Mechanism (Import by renaming!)
import name as name_function

# Import
import sys

# Use below print command to get functions defined inside the module
print(dir(name))  # We can see 'print_name' as an available function, which can be called from this script

# Invoke Function
name.print_name('Ramesh')

# Importing Mechanism (Import by renaming!)
# import name as name_function
print(dir(name_function))
print("--------------------------")

# Python Module Search Path
# import sys (It's always a good step to add import command at start of the script)
# While importing a module, Python looks at several places.
# Interpreter first looks for a built-in module then (if not found) into a list of directories defined in sys.path
print(sys.path)
