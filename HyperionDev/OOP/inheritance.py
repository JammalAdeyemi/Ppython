# Parent class for a car from which we can extend to a subclass
class Car:
    #class variable for whether engine is running or not
    is_running = False
    # constructor that allows us to set the make and model as instance variables
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # this method starts the engine
    def start_car(self):
        self.is_running = True

    # this method turns off the engine the engine
    def turn_off_car(self):
        self.is_running = False

    # this method prints the make and model to console
    def show_make_and_model(self):
        print(f"This vehicle is a {self.make} {self.model}")

# We are inheriting all of the attributes and methods from the Car class by passing it as an argument to the PickupTruck class
class PickupTruck(Car):
    # this is an additional class variable that is specific to the PickupTruck class
    is_loaded = False
    # this method loads the truck
    def load(self):
        self.is_loaded = True
    # this method removes the load from the truck
    def unload(self):
        self.is_loaded = False

# create a pickup truck object
pickup_truck_1 = PickupTruck("Toyota", "Hilux")
# we are calling a method that we created in the subclass this changes the variables from False to True
pickup_truck_1.load()
# we are calling a method inherited from the parent class
pickup_truck_1.start_car()
# we print out to values so that we can see that both of the above methods worked
print(pickup_truck_1.is_running)
print(pickup_truck_1.is_loaded)
# lastly we are calling another method that was inherited
# from the parent class
pickup_truck_1.show_make_and_model()
