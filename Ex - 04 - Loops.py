"""
    In general, statements are executed sequentially.
    The first statement in a function is executed first, followed by the second, and so on.
    There may be a situation when you need to execute a block of code several number of times.
    Programming languages provide various control structures that allow for more complicated execution paths.

    Loop Type & Description

        WHILE LOOP
            Repeats a statement or group of statements while a given condition is TRUE.
            It tests the condition before executing the loop body.

        FOR LOOP
            Executes a sequence of statements multiple times and abbreviates the code that manages the loop variable.

        NESTED LOOP
            You can use one or more loop inside any another while loop, for loop or do..while loop.
"""

# While Loop

simple_count = 0
while simple_count < 10:
    simple_count += 1
    print("Loop Executed =", simple_count)
print("Good Bye!")
print("--------------------------")


another_count = 0
while another_count < 5:
    another_count += 1
    print(another_count, "is the while loop's value")
else:
    if another_count == 5:
        print("Ending while loop execution!")
print("--------------------------")


# Takes user's input
user_input = int(input("Enter an integer value :"))
total_value = 0
iterable_value = 1

while iterable_value <= user_input:
    total_value = total_value + iterable_value
    iterable_value += 1
    print("Sum Value =", total_value)
print("End of the execution")
print("--------------------------")


# For Loop

sample_string = 'Bangalore'
for each_letter in sample_string:
    print(each_letter)
print("Printed every letter of the word :", sample_string)
print("--------------------------")


# For Loop (Includes Indexing)

fruits = ['Mango', 'Apple', 'Pine', 'Orange', 'Papaya']
for each_fruit in fruits:
    print("Fruit Name =", each_fruit, "& it's Index value =", fruits.index(each_fruit))
print("Good Bye!")
print("--------------------------")


# For Loop (Is this a Prime number?)

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print('%d equals %d * %d' % (num, i, j))
            break
    else:
            print(num, 'is a prime number')
print("Good Bye!")
print("--------------------------")


# Nested Loop

x = 2
while x <= 100:
    y = 2
    while y <= x / y:
        if not x % y:
            break
        y += 1
    if y > x / y:
        print(x, " is a prime number")
    x += 1
print("Done")
print("--------------------------")

