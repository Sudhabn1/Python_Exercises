"""
    Variables are nothing but reserved memory locations to store values.
    This means that when you create a variable you reserve some space in memory.
    By assigning different data types to variables, you can store integers, decimals or characters in these variables.

    Standard Data Types

        The data stored in memory can be of many types.
        Ex - A person's age is stored as a numeric value and his or her address is stored as alphanumeric characters.
        Python has various standard data types that are used to define the operations possible on them!

    Python has five standard data types −

        Numbers
        String
        List
        Tuple
        Dictionary
"""

# Assigning Values

counter = 100
miles = 95.33
name = "John"

print("Counter = ", counter)
print("Miles =", miles)
print("Name =", name)


# Multiple Assignment

A = B = C = 1
X, Y, Z = 10, 20, "Ram"

print("A =", A, "| B =", B, "| C =", C)
print("X =", X, "| Y =", Y, "| Z =", Z)

print("--------------------------")


# Numbers
variable_1 = 25
variable_2 = 338.09
variable_3 = 6639279
variable_4 = 34.33j

print("Variable 1 Type =", type(variable_1))
print("Variable 2 Type =", type(variable_2))
print("Variable 3 Type =", type(variable_3))
print("Variable 4 Type =", type(variable_4))

print("--------------------------")


# Strings

sample_string = "Hello, you are in Bengaluru city!"
another_string = "Indeed, it's a great city."

print("Sample String = ", sample_string)
print("String Length =", len(sample_string))
print("Display String's character taking 8 as index =", sample_string[8])
print("Display String's character taking 18 as index =", sample_string[18])
print("Display String's characters between 18 to 27 =", sample_string[18:27])
print("Combing 2 String values =", sample_string + " " + another_string)

print("--------------------------")


# Lists

sample_list = [22, 48, "John", 2338.933, "Amar", 77733829]

print("Displaying Sample List = ", sample_list)
print("Displaying Sample List's Length =", len(sample_list))
print("Displaying Sample List's [2] index value =", sample_list[2])
print("Displaying Sample List's [2] to [5] index value =", sample_list[2:5])

print("--------------------------")


# Tuples

sample_tuple = ('Ram', 18822819, 281.33, 94, 'Suresh', 3884.99j)

print("Displaying Sample Tuple = ", sample_list)
print("Displaying Sample Tuple's Length =", len(sample_tuple))
print("Displaying Sample Tuple's [2] index value =", sample_tuple[2])
print("Displaying Sample Tuple's [2] to [5] index value =", sample_tuple[2:5])

print("--------------------------")


# Dictionary

sample_dictionary = {'Name': 'Ram', 'Age': 22, 'Place': 'Bangalore', 'Profession': 'Engineer'}

print("Displaying Sample Dictionary =", sample_dictionary)
print("Displaying all keys within Dictionary =", sample_dictionary.keys())
print("Displaying value taking key into consideration =", sample_dictionary.get('Age'))
print("Displaying length of Dictionary =", len(sample_dictionary))

print("--------------------------")
