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
    def __init__(self, greeting):
        self.defaultName = "Person"
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

        if not isinstance(self.engine, Engine):
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


class VehicleService():
    def fix_vehicle(self, vehicle):
        pass

service = VehicleService()

service.fix_vehicle(bike)
bike.can_ride()