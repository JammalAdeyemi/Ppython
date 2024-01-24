# Define parent class
class Computer():
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd

# Define subclass
class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model

# Create a laptop object
vivobook = Laptop('Asus', 8, 512, 'Vivobook')
# Print laptop’s features
print('Computer make:', vivobook.computer)
print('Computer model:', vivobook.model)
print(f"This computer has {vivobook.ram}GB of RAM.")
print(f"This computer has {vivobook.ssd}GB of SSD storage.")
print()


# Method Overriding -Overriding is the ability of a class to change the implementation of a method provided by a parent class.
class Father():
    def transport(self):
        print("The transport used is a car")
class Son(Father):
    def transport(self):
        print("The transport used is a bicycle")

son_1 = Son()
# this will output "The transport used is a bicycle" because the inherited method is being overridden by the Son subclass
print("Example 2")
son_1.transport()