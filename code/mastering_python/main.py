def main():
    # Here we import the class
    from classes_objects import Person
    # Here we create an instance of the class Person
    person_1 = Person("Fabri", 32, "123456789")
    # Here we call the method my_dni()
    person_1.my_dni()
    # Here we call the method my_age()
    person_1.greet()


# then we call the function main()

if __name__ == "__main__":
    main()
