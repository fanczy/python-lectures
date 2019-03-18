#####################
###### CLASSES ######
#####################

class SimpleGreeter():
    def __init__(self):
        print("Hello, Person.")
    

simple_greeter = SimpleGreeter()

class Greeter():
    def __init__(self, greeting):
        self.greeting = greeting
        print(f"{greeting}, Person.")


greeter1 = Greeter("What's up")
print(greeter1.greeting)

greeter2 = Greeter("Hey there")
print(greeter2.greeting)

class BetterGreeter():
    def __init__(self, greeting):
        self.greeting = greeting

    def greet(self):
        print(f"{self.greeting}, Person.")

betterGreeter = BetterGreeter("Hey")
betterGreeter.greet()
betterGreeter.greeting = "Yo"
betterGreeter.greet()

class SophisticatedGreeter():
    defaultName = "Person"

    def __init__(self, greeting):
        self.greeting = greeting
        self.greet()

    def greet(self):
        print(f"{self.greeting}, {self.defaultName}.")


sophisticatedGreeter = SophisticatedGreeter("Hi there")

class SuperGreeter():
    def __init__(self, greeting):
        self.greeting = greeting

    def greet(self, name):
        print(f"{self.greeting}, {name}.")

superGreeter = SuperGreeter("Hello")

superGreeter.greet("Friend")

##### excercise #####
# Upgrade SuperGreeter into UberGreeter, UberGreeter has attribute defaultName.
# greet method has one optional argument name
# if greet is called without a name, it will use defaultName property.
#######################

class Wheel():
    broken = False

class Motor():
    broken = False
    needs_oil = False

class Bike():
    wheels = []

class Car():
    wheels = []
    motor = None

class TransportFactory():
    def __init__(self, name):
        self.name = name

    def manufacture_bike(self):
        new_bike = Bike()
        self.add_wheels(new_bike, 2)
        self.__add_brand(new_bike)
        return new_bike
    
    def manufacture_car(self):
        new_car = Car()
        self.add_wheels(new_car, 4)
        self.add_motor(new_car)
        self.__add_brand(new_car)
        return new_car
    
    def add_wheels(self, transport, number_of_wheels):
        if(not hasattr(transport, "wheels")):
            return

        for _ in range(number_of_wheels):
            transport.wheels.append(Wheel())

    def add_motor(self, transport):
        if(not hasattr(transport, "motor")):
            transport.motor = Motor()

    def __add_brand(self, transport): # private method can't be accessed outside of class
        transport.brand = self.name
    
superFactory = TransportFactory("SuperFactory")

bike = superFactory.manufacture_bike()
print(bike.brand)

car = superFactory.manufacture_car()
print(car.brand)


