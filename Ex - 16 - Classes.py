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
