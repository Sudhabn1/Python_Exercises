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
