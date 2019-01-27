"""
    A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.
    Differences between tuples and lists are, the tuples cannot be changed unlike lists!
    Also, tuples use parentheses, whereas lists use square brackets.
"""


sample_tuple_01 = ('Ram', 3492, 'Suresh')

sample_tuple_02 = (28839.23, 'Hemanth', 684.J, 'Bangalore')

print()
print(sample_tuple_01)
print(sample_tuple_02)

# Displaying ID

print("sample_tuple_01 - ID =", id(sample_tuple_01))
print("sample_tuple_02 - ID =", id(sample_tuple_02))

# Equality Test

tuple_001 = ('Ram', 3492, 'Suresh')
print()
print("ID - tuple_001 =", id(tuple_001))
tuple_002 = tuple_001
print("ID - tuple_002 =", id(tuple_001))
print("Both tuples are having same ID's, where assignment attaches name to an object!")

print("--------------------------")
