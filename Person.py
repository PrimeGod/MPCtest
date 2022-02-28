# -*- coding: utf-8 -*-
"""

This module demonstrates a simple implementation of a Person class.

Based upon the rules cited in the test email

By Philippe Langevin

"""


class Person(object):
    """The Person class has an init method taking the initial age
    as attribute for creating a new Person as an object.
    This class allows the user to 'age' the Person by 1 year object with its
    method year_passes().
    This class allows the user to get a statement on the age of the Person
    with the method what_am_i()

    """
    age = -1
    
    def __init__(self, initial_age):
        """Constructor of the Person class

    Gives an initial age to the Person

    Args:
        initial_age (int): The initial age of the Person object


    Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If 'initial_age' is lower than 0.
        TypeError: If 'initial_age is not the right type.

    """
        if initial_age < 0:
            raise ValueError("The value of 'age' passed as parameter must be higher than 0.")
        if type(initial_age) != int:
            raise TypeError("The value passed as parameter must be an integer.")
        else:
            self.age = initial_age
    
    def what_am_i(self):
        """This function prints a statement based on the age of the person.
        Under an age of 13, between 13 and 18, and 18 and older.

    """
        if self.age < 13:
            print("You are young")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager")
        else:
            print("You are an adult")

    def year_passes(self):
        """This function adds a year to the age of the Person object
    """
        self.age += 1
    