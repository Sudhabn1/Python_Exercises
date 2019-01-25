"""
    Number data types store numeric values. They are immutable data types, means that changing the value of a
    number data type results in a newly allocated object.
"""
# Printing few numbers and it's type

import math

sample_numbers = [453, 2819.332, -.6545+0J]
print()
for number_val in sample_numbers:
    print(number_val, "Type =", type(number_val))

print("--------------------------")


# Type Conversion

example_number = 1833
print("Number =", example_number, "Type =", type(example_number))
print("Changing it to Float type :", float(example_number))
print("Changing it to Complex type :", complex(example_number))
print("--------------------------")


# Mathematical Operations

number1 = 2883
number2 = 3882.048727
number3 = 83002.38822+0J

# Method abs() returns absolute value of x - the (positive) distance between x and zero
print("Absolute Value =", abs(number1))
print("Absolute Value =", abs(number2))
print("Absolute Value =", abs(number3))

# Method exp() returns exponential of a variable

num_01 = 36
num_02 = 21
num_03 = 364.92
print("Exponential Value =", math.exp(num_01))
print("Exponential Value =", math.exp(num_02))
print("Exponential Value =", math.exp(num_03))
print("Exponential Value =", math.exp(math.pi))

# Method floor() returns floor of x - the largest integer not greater than x

number_1 = 2883
number_2 = 82889.293811

print("Floor Value =", math.floor(number_1))
print("Floor Value =", math.floor(number_2))

print("--------------------------")
