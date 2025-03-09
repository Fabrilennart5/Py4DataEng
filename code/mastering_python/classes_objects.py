# Classes are like blueprints for creating objects.
# Objects are instances of a class, and they encapsulate data (attributes) and behavior (methods).

class Person:
    """
    A class to represent a person.

    Attributes:
        name (str): The name of the person.
        age (int): The age of the person.
        dni (str): The identification number of the person.
    """

    def __init__(self, name: str, age: int, dni: str):
        """
        Constructs all the necessary attributes for the Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            dni (str): The identification number of the person.
        """
        self.name = name
        self.age = age
        self.dni = dni

    def greet(self) -> None:
        """
        Prints a greeting message with the person's name.
        """
        print(f"Hello, my name is {self.name}.")

    def show_dni(self) -> None:
        """
        Prints the person's identification number (DNI).
        """
        print(f"My DNI is {self.dni}.")
