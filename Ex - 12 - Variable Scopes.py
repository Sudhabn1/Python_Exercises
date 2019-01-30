"""
    A variable declared outside of the function or in global scope is known as global variable.
    This means, global variable can be accessed inside or outside of the function.

    Meanwhile, a variable declared inside the function's body or in the local scope is known as local variable.
"""

global_variable_example = 'Global Variable Output'


def global_generic_variable_scope(var_injection):
    print("Inside Function Call =", global_variable_example)
    print("Value Injected =", var_injection)

print("Completed Execution!")

# Testing
global_generic_variable_scope('Global Output')

print("--------------------------")


def local_generic_variable_scope(var_injection):
    global_variable_example = 'Local Variable Output'
    # Same variable declared inside function provides different output
    print("Inside Function Call =", global_variable_example)
    print("Value Injected =", var_injection)


# Testing

local_generic_variable_scope('Local Output')  # Here, local variable is used and output is displayed
print("Global Var =", global_variable_example)  # Here, we can directly access global variable by using print value

print("--------------------------")


injected_value = 20  # Same Name --> Global Variable & Local Variable


def sample_function():
    injected_value = 10
    print("Inside Function, Local Scope =", injected_value)

# Testing
sample_function()
print("Outside Function, Global Scope =", injected_value)

print("--------------------------")


some_value = 'Rajesh'
print("Global Value (Before) =", some_value)


def using_global_keyword_sample():
    global some_value  # Using global keyword
    some_value += ' Kumar'
    print("Inside Function =", some_value)

# Testing

using_global_keyword_sample()
print("Outside Function =", some_value)

print("--------------------------")
