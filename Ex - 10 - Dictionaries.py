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

print("--------------------------")
