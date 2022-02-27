'''
Example of Person Class for technical test
By Philippe Langevin
'''

class Person(object):
    age = -1   

    def __init__(self, initial_age):
        if self.age >= 0 and type(self.age) == int:
            self.age = initial_age
        else:
            print("The input parameter 'age' of the constructor" +
            "isn't valid")
    
    def what_am_i(self):
        if self.age < 13:
            print("You are young")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager")
        else:
            print("You are an adult")

    def year_passes(self):
        self.age += 1