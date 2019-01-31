"""
    A module allows you to logically organize your Python code.
    Grouping related code into a module makes the code easier to understand and use.
    A module is a Python object with arbitrarily named attributes that you can bind and reference.
    Simply, a module is a file consisting of Python code. A module can define functions, classes and variables.
    A module can also include runnable code.
"""

# Import Module (name.py)
import name

# Use below print command to get functions defined inside the module
print(dir(name))  # We can see 'print_name' as an available function, which can be called from this script

# Invoke Function
name.print_name('Ramesh')
