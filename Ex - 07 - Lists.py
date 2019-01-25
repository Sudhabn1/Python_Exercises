"""
    The most basic data structure in Python is the sequence.
    Each element of a sequence is assigned a number - its position or index.
    The first index is zero, the second index is one, and so forth.
"""

example_list = ['Ram', 8392, 944.33819, 9329338.0J, 'Suresh']
print()
print("Displaying an entire list items created above =", example_list)

# Indexing

for each_item in example_list:
    print("Item =", each_item, "& Index =", example_list.index(each_item))

# length

print("List Length [example_list] =", len(example_list))

# Getting Element (By using Index value)

print("Get Element [Uses Index Value] =", example_list.__getitem__(2))

# Reversing Elements

print("Printing Elements (Before reverse operation) =", example_list)
example_list.reverse()
print("Printing Elements (After reverse operation) =", example_list)

print("--------------------------")

# Sorting Elements

need_sorting_list = [3, 9, 1, 4922, 85, 833]
print("Displaying Results (Before sort() operations) =", need_sorting_list)
need_sorting_list.sort()
print("Displaying Results (After sort() operations) =", need_sorting_list)

# Sorting Elements (Str & Int Items)

mixed_sorting_list = [3, 9, 1, 'Ram', 'Zara', 'Amar', 4922, 85, 833.332, 'Mahesh']
print("Displaying Results (Before sort() operations) =", mixed_sorting_list)
mixed_sorting_list.sort(key=str)
print("Displaying Results (After sort(key=str) operations) =", mixed_sorting_list)

print("--------------------------")

# Remove & Pop Operations

remove_string_elements = ['Ram', 'Zara', 'Amar', 'Mahesh', 392, 9912, 1, 49920]
print("Before Removal Operations =", remove_string_elements)
remove_string_elements.remove(392)
print("Removing Element (392)")
print("After Removal Operations =", remove_string_elements)
print("Removing Element ('Mahesh)")
remove_string_elements.remove('Mahesh')
print("After Removal Operations =", remove_string_elements)

print("--------------------------")
