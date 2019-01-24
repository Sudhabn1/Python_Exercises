"""
    Number data types store numeric values. They are immutable data types, means that changing the value of a
    number data type results in a newly allocated object.
"""
# Printing few numbers and it's type

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
print("--------------------------")
