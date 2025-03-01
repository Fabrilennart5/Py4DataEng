# Clases are like blueprints for objects
# Objects are instances of a class
# they are helping us to create new objects


class Person:
    def __init__(self, name, age, dni):
        self.name = name
        self.age = age
        self.dni = dni

    # methods are functions inside a class
    def greet(self):
        print("Hello my name is: ", self.name)

    def my_dni(self):
        print("My dni is: ", self.dni)
