#####################
###### CLASSES ######
#####################

class SimpleGreeter(): # Class is definition of object's behavior and properties. There can be multiple instances of objects of the same class.
    def __init__(self): # Every method of a class gets instance that it's called on as a first argument.
        print("Hello, Person.")
    

simple_greeter = SimpleGreeter() # This calls constructor (__init__ method) and returns new instance object of a class.

class Greeter():
    def __init__(self, greeting): # Constructor of this class gets one argument.
        self.greeting = greeting  # You can change attributes of instance throught the self argument.
        print(f"{greeting}, Person.")


greeter1 = Greeter("What's up") # Creates instance of Greeter class with "What's up" as constructor argument. 
print(greeter1.greeting) # You can access objects attributes throught dot notation.

greeter2 = Greeter("Hey there") # Creates another instance of the same class with different constructor argument.
print(greeter2.greeting) # Here you can see this instance has different greeting attribute, which was set in constructor.

class BetterGreeter():
    def __init__(self, greeting):
        self.greeting = greeting

    def greet(self): # Class methods get the instance as first argument without passing them in a call.
        print(f"{self.greeting}, Person.") # self.greeting is the attribute that was set in the constructor.

betterGreeter = BetterGreeter("Hey")
betterGreeter.greet() 
betterGreeter.greeting = "Yo" # We can change objects attributes through dot notation.
betterGreeter.greet() # Here you can see, this instances greet() method will use the changed greeting.

class SophisticatedGreeter():
    def __init__(self, greeting):
        self.defaultName = "Person"
        self.greeting = greeting

    def greet(self, name = None): # We can assign default value to object argument so it becomes optional.
        if(name is None):
            name = self.defaultName  # If the argument wasn't passed in call, we'll use defaultName attibute.
        print(f"{self.greeting}, {name}.")


sophisticatedGreeter = SophisticatedGreeter("Hi there")
sophisticatedGreeter.greet() # Greet with defaultName
sophisticatedGreeter.greet("Friend") # Greet passed name

class Wheel():
    def __init__(self):
        self.broken = False


class Engine():
    def __init__(self):
        self.needs_oil = True

class Bike():
    def __init__(self):
        self.wheels = []

    def can_ride(self):
        if(len(self.wheels) < 1):
            return False

        for wheel in self.wheels:
            if wheel.broken:
                return False
        return True

class Car():
    def __init__(self):
        self.wheels = []
        self.engine = None

    def can_ride(self):
        if self.engine is None:
            return False

        if not isinstance(self.engine, Engine): # Checks if the engine attribute is instance of Engine class so we can safely use class methods.
            return False

        if self.engine.needs_oil:
            return False

        return True

class Rock():
    broken_wheels = 0
    def break_wheel(self, transport):
        for wheel in transport.wheels:
            if not wheel.broken:
                wheel.broken = True
                self.broken_wheels += 1
                break

class VehicleFactory():
    def manufacture_bike(self):
        new_bike = Bike()
        self.add_wheels(new_bike, 2)
        return new_bike

    def manufacture_car(self):
        new_car = Car()
        self.add_wheels(new_car, 4)
        self.add_engine(new_car)
        return new_car

    def add_engine(self, vehicle):
        if vehicle.engine is None:
            vehicle.engine = Engine()

    def add_wheels(self, vehicle, number_of_wheels):
        if not hasattr(vehicle, "wheels"):
            return
        if not type(vehicle.wheels) is type([]):
            return

        for _ in range(number_of_wheels):
            vehicle.wheels.append(Wheel())

factory = VehicleFactory()
bike = factory.manufacture_bike()
rock = Rock()
print(bike.can_ride())
rock.break_wheel(bike)
print(bike.can_ride())
car = factory.manufacture_car()
print(car.can_ride())

##### HOMEWORK #####
# Create VehicleService class
# This class has a method fix_vehicle that takes vehicle as a argument
# Method fix_vehicle repairs all broken wheels on vehicle, if it has any and refils oil into vehicle's engine if it has any.
####################

class VehicleService():
    def fix_vehicle(self, vehicle):
        print("This method fixes any vehicle.")

service = VehicleService()

service.fix_vehicle(car)
print(car.can_ride())
service.fix_vehicle(bike)
print(bike.can_ride())