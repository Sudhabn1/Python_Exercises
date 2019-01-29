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
