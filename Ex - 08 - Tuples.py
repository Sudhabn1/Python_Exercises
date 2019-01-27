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
print("Assigning from one reference to another, puts two name tags to an object.")
print(tuple_001)
print(tuple_002)

print("--------------------------")

# Generic Tuple Operations

tuple_007 = ('Yogesh', 'Bangalore', 'Idly', 329091, 293.3772, 'Delhi', 291, 952, 'KKR', 'RCB', 'Virat')
tuple_008 = (3881, 9486142938.4992, 37, 887452.27610020991, 3889, 583, 8331)
print("Length =", len(tuple_007))
print("Get Index Value =", tuple_007.index('Bangalore'))
print("Tuple's Size =", tuple_007.__sizeof__())
print("Tuple's Class Info =", tuple_007.__class__)
print("Value (Virat) Contains Test =", tuple_007.__contains__('Virat'))
print("Value (Dhoni) Contains Test =", tuple_007.__contains__('Dhoni'))
print("Object's Attributes List =", tuple_007.__dir__())

print("--------------------------")

# Few Tuple Operations

print("Get Value (Index Value 10) =", tuple_007.__getitem__(10))
print("Another Way - Tuple's Length (__len__) =", tuple_007.__len__())
tiny_tuple = ('Chennai', 'Modi')
print("After Adding 2 Elements - ID Changed =", id(tuple_007.__add__(tiny_tuple)))
print("However, 'tuple_007' ID =", id(tuple_007))
print("Max Element =", max(tuple_008))
print("Min Element =", min(tuple_008))
print("All Elements Iterable? all() =", all(tuple_008))
print("--------------------------")
