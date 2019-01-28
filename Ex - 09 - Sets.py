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

# Removing Elements

remove_elements_set = {29, 381, 'Ramesh', 'Xavier', 399.9661, 99, 'Bharat'}
print("Displaying Values (Before removal operation) =", remove_elements_set)
remove_elements_set.remove('Xavier')
print("Displaying Values (After removal operation) =", remove_elements_set)

discard_element_set = {23379, 93381, 'Hemanth', 'Thomas', 12.9661, 9281, 'Modi'}
print("Displaying Values (Before discard operation) =", discard_element_set)
discard_element_set.discard('Hemanth')
print("Displaying Values (After discard operation) =", discard_element_set)

print("--------------------------")

# Generic Operations

yet_another_set = {'Mahesh', 'Sushma', 'Arun', 'Raja', 298891.27, 8482.J, 'Rani'}
print("Displaying Values (Before pop() operation) =", yet_another_set)
yet_another_set.pop()  # One element will be removed from set in a random fashion
print("Displaying Values (After pop() operation) =", yet_another_set)

one_more_set = {'Samuel', 'Maria', 'Xavier', 'Ram', 'Bharat', 'Ganesh', 2910.001, 888888, 10029, 'Eshwar'}
print("Displaying Values (Before clear() operation) =", one_more_set)
one_more_set.clear()
print("Displaying Values (After clear() operation) =", one_more_set)

print("--------------------------")

# Set Operations (Union, Intersection, Difference & Symmetric)

Set_001_A = {1, 2, 3, 4, 5}
Set_002_B = {4, 5, 6, 7, 8}
print("Union Operation =", Set_001_A | Set_002_B)
print("Intersection Operation =", Set_001_A & Set_002_B)
print("Difference Operation =", Set_001_A - Set_002_B, "&", Set_002_B - Set_001_A)
print("Symmetric Operation =", Set_001_A ^ Set_002_B)

print("--------------------------")
