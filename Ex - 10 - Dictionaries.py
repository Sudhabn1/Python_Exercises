"""
    Python dictionary is an unordered collection of items.
    While other compound data types have only value as an element, a dictionary has a key: value pair.
    Dictionaries are optimized to retrieve values when the key is known.
"""

sample_dictionary = {'a': 'Agra', 'b': 'Bangalore', 'c': 'Chennai', 'd': 'Delhi', 'e': 'Erode'}
print()
print("Displaying Dictionary =", sample_dictionary)

mixed_sample_dictionary = {'a': 'Agra', 'b': 28819, 'c': 'Chennai', 'd': 99817.291, 'e': 'Erode', 'f': 382991}
print()
print("Displaying Mixed Dictionary =", mixed_sample_dictionary)

# Access Elements

access_elements_dictionary = {'a': 'Apple', 'b': 'Banana', 'c': 'Cat', 'd': 'Dog', 'e': 'Elephant'}
print("Access Element =", access_elements_dictionary.get('d'))
print("Access Element =", access_elements_dictionary.get('b'))
print("Displaying Keys (All keys available in Dictionary) =", access_elements_dictionary.keys())

# Modifying Elements

new_element_add_dictionary = {'a': 'Apple', 'b': 99100, 'c': 9901991}
print("Displaying (Before modifications) =", new_element_add_dictionary)
new_element_add_dictionary['d'] = 'Donut'
print("Displaying (After adding new element) =", new_element_add_dictionary)

modify_elements_dictionary = {'a': 'Agra', 'b': 8819, 'c': 'Chennai', 'd': 399817.291, 'e': 'Erode', 'f': 99534}
print("Displaying (Before modifications) =", modify_elements_dictionary)
modify_elements_dictionary['c'] = 'Calcutta'  # Changing Value
print("Displaying (After modifications) =", modify_elements_dictionary)

delete_element_dictionary = {'Name': 'Dinesh', 'Age': 38, 'City': 'Mumbai', 'Profession': 'LIC Agent', 'Salary': 99999}
print("Displaying Values (Before deletion) =", delete_element_dictionary)
delete_element_dictionary.__delitem__('Salary')
delete_element_dictionary.pop('Profession')
print("Displaying Values (After deletion) =", delete_element_dictionary)

print("--------------------------")

# Generic Dictionary Operations

generic_sample_dictionary = {'Name': 'Prithvi', 'Age': 28, 'City': 'Pune', 'Profession': 'Cab Driver', 'Salary': 125000}
copied_dictionary = generic_sample_dictionary.copy()
print("After Copying =", copied_dictionary)

print("Items() Option =", generic_sample_dictionary.items())
print("Getting Values Only =", generic_sample_dictionary.values())
print("Getting Length =", len(generic_sample_dictionary))
print("Getting Class Details =", generic_sample_dictionary.__class__)

print("--------------------------")

print("Displaying Dictionary Attributes =", dir(generic_sample_dictionary))
print("Provide Documentation Info =", generic_sample_dictionary.__doc__)

print("--------------------------")

# Dictionary Comprehension

square_value_dictionary = {x: x * x for x in range(20)}  # One of the important mechanism!
print("Square Values =", square_value_dictionary)

odd_or_even = {x: x % 2 == 0 for x in range(20)}
print("Displaying Odd / Even State =", odd_or_even)

print("--------------------------")
