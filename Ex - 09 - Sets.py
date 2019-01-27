"""
    A set is an unordered collection of items.
    Every element is unique (no duplicates) and must be immutable (which cannot be changed).
    However, the set itself is mutable. We can add or remove items from it.
"""

# Creating Set

sample_set = {291, 'Ram', 3819}
print("Displaying Values =", sample_set)

# Creating Empty Set
empty_set_declaration = {}
print(type(empty_set_declaration))  # Type will be dictionary by default, change it to set() and see results
empty_set_declaration = set()
print("After Modifications =", type(empty_set_declaration))

# Changing Set

changing_set_example = {1, 3, 4, 7, 6, 8, 5}
print("Output = ", changing_set_example)
changing_set_example.add(2)  # Adding 2 Value
print("After Changes =", changing_set_example)

another_set = {'Amar', 'Zaheer', 'Thomas', 'Suresh', 'Mahesh'}
print("Displaying Set (String Values) =", another_set)  # Order not followed, don't get confused!
print("After Invoking Sort() =", sorted(another_set))

print("--------------------------")

