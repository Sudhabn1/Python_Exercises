"""
    Object-oriented programming (OOP) is a programming paradigm that uses objects and their interactions to
    design applications and computer programs. There are some basic programming concepts in OOP:

        Abstraction
        Polymorphism
        Encapsulation
        Inheritance
    The abstraction is simplifying complex reality by modeling classes appropriate to the problem.
    The polymorphism is the process of using an operator or function in different ways for different data input.
    The encapsulation hides the implementation details of a class from other objects.
    The inheritance is a way to form new classes using classes that have already been defined.
"""
# Code for some sample classes, methods and instance methods


class Flight:
    print("Inside Class")

    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError("No Airline Code {}".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid Airline Code {}".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid Route Number {}".format(number))

        self._number = number

    def number(self):
        print(self._number)
        return self._number

    def airline(self):
        print(self._number[:2])
        return self._number[:2]


class Aircraft:

    def __init__(self, registration, model, num_rows, num_of_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_of_seats_per_row = num_of_seats_per_row

    def registration(self):
        print(self._registration)
        return self._registration

    def model(self):
        print(self._model)
        return self._model

    def seating_plan(self):
        print(range(1, self._num_rows + 1), "ABCD"[:self._num_of_seats_per_row])
        return range(1, self._num_rows + 1), "ABCD"[:self._num_of_seats_per_row]

print("--------------------------")

# Generic OOP's Code


class Parrot:

    # Class Attribute
    species = 'bird'

    # Instance Attributes
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # Instance Method
    def sing(self, language):
        print("Parrot sings in" + language)
        return language

parrot_01 = Parrot('Tobi', 'Grey')
parrot_02 = Parrot('Sumo', 'Green')

print("Accessing First Parrot's Class Attribute =", parrot_01.species)
print("Accessing Second Parrot's Class Attribute =", parrot_02.species)
print("First Parrot's Name & Color =", parrot_01.name, parrot_01.color)
print("Second Parrot's Name & Color =", parrot_02.name, parrot_02.color)

# Calling Instance Methods
get_parrot_01_langauage = parrot_01.sing('Hindi')
get_parrot_02_langauage = parrot_02.sing('Kannada')
print("First Parrot's Singing Language =", get_parrot_01_langauage)
print("Second Parrot's Singing Language =", get_parrot_02_langauage)

print("--------------------------")

# Inheritance OOP's Logic


class Bird:

    def __init__(self):
        print("Bird is ready!")

    def who_is_this(self):
        print("Bird")

    def swim(self):
        print("Swim Faster")

# Child Class


class Penguin(Bird):

    def __init__(self):
        super().__init__()  # Calling super function
        print("Penguin is ready!")

    def who_is_this(self):
        print("Penguin")

    def swim(self):
        print("I can't swim faster!")

# Instantiation
peggy = Penguin()
peggy.who_is_this()
peggy.swim()

print("--------------------------")

# Encapsulation OOP's Logic


class Computer:

    def __init__(self):
        print("Inside Computer Class")
        self._brand = 'Lenovo'

    def model(self):
        model = 'T440S'

    def price(self, price):
        price = 40000
        if price > 4000:
            print("You are planning to pay more!")
        else:
            print("You are planning to pay less!")

# Instantiation

purchase_computer = Computer()
purchase_computer.model()
purchase_computer.price(35000)  # Trying to pay 35K for this computer

print("--------------------------")

# Polymorphism OOP's Logic


class Dog:

    def __init__(self):
        print("Inside Dog's Class")

    def run(self):
        print("Dogs can run!")

# Child Class


class Labrador:

    def __init__(self):
        print("Inside Labrador Class")

    def run(self):
        print("Labrador can also run quick!")


# Common Interface


def lets_test_running_state(any_dog):
    any_dog.run()

# Instantiation
puppy_01 = Dog()
puppy_02 = Labrador()

# Same function, different (poly) outputs taking object instantiation mechanism
lets_test_running_state(puppy_01)
lets_test_running_state(puppy_02)
