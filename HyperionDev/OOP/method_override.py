name = input("Enter your name: ")
age = int(input("Enter your age: "))
hair_colour = input("Enter your hair colour: ")
eye_colour = input("Enter your eye colour: ")

class Adults:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    # Method called can_drive() that prints the name of the person and that they are old enough to drive.
    def can_drive(self):
        print(f"{self.name} is old enough to drive")

# Create a subclass of the adult class named “Child” that has the same attributes, 
# but overrides the can_drive method to print the persons name and that they are too young to drive.
class Child(Adults):
    def can_drive(self):
        print(f"{self.name} is too young to drive")

# Create some logic that determines if the person is 18 or older and create an instance of the Adult class if this is true. 
# Otherwise, create an instance of the Child class. Once the object has been created, 
# call the can_drive() method to print out whether the person is old enough to drive or not.
if age >= 18:
    person = Adults(name, age, hair_colour, eye_colour)
    person.can_drive()
else:
    person = Child(name, age, hair_colour, eye_colour)
    person.can_drive()
