"""
    In Python, function is a group of related statements that perform a specific task.
    Functions help break our program into smaller and modular chunks.
    As our program grows larger and larger, functions make it more organized and manageable.
    Furthermore, it avoids repetition and makes code reusable.
"""

# Sample Function


def odd_or_even(number):
    if number % 2 == 0:
        print(number, "= Even")
    else:
        print(number, "= Odd")

sample_range = range(1, 21)  # Let's define a range and inject value to above mentioned function
print()
print("Displaying Range Elements =", sample_range)
for each_value in sample_range:
    odd_or_even(each_value)
print("Iteration Done!")

print("--------------------------")

# Sample Function (Includes Arguments)


def greet_person(name):
    if type(name) is str:
        print("Hello", name)
        print("Have a great day ahead!")
    else:
        print(name, " = Name should be a string value & not any other type!")

greet_person("Ramesh")  # Calling greet_person function with String value
greet_person(32)  # Calling greet_person function with Integer value

print("--------------------------")

# Sample Function (Default Values)


def wishing_person(name, message="Good Morning!"):  # Message is having a default value as "Good Morning!"
    print("Hello ", name)
    print(message)
    print("Function Completed!")

# Testing
wishing_person(name='Kiran')
wishing_person("Mahesh", "Good Evening!")  # Modifying default value of message

print("--------------------------")


# Functions (Arbitrary Arguments)

def wishing_entire_members(*names):
    for name in names:
        print("Hey", name)
        print("How are you? Good Morning!")
print("Completed Execution")

# Testing
wishing_entire_members("Mahi", "Dhoni", "Virat", "Rohit")

print("--------------------------")
