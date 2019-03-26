##########################################
###### INHERITANCE AND POLYMORPHISM ######
##########################################

class Wheel():
    def __init__(self):
        self.broken = False

class Vehicle(): # This class is abstract it serves just for a purpose of other classes implementing it.
    def can_ride(self):
        raise NotImplementedError("Subclass must implement this exception")

class WheeledVehicle(Vehicle): # This class extends our Vehicle class, which means it inherits it's methods and attributes
    def __init__(self):
        Vehicle.__init__(self)
        self.wheels = []
    
    def can_ride(self): # This class overrides the inherited can_ride() method.
        return self.do_all_wheels_work()
    
    def do_all_wheels_work(self):
        if not type(self.wheels) is type([]) or self.wheels.__len__() < 1:
            return False
        
        for wheel in self.wheels:
            if(not isinstance(wheel, Wheel) or wheel.broken):
                return False
        
        return True

vehicle = Vehicle()
# print(vehicle.can_ride())

wheeled_vehicle = WheeledVehicle()
print(wheeled_vehicle.can_ride())

wheeled_vehicle.wheels.append(Wheel())
print(wheeled_vehicle.can_ride())

wheeled_vehicle.wheels[0].broken = True
print(wheeled_vehicle.can_ride())

class Engine():
    def __init__(self):
        self.needs_oil = True
    
    def works(self):
        return not self.needs_oil
        
class Car(WheeledVehicle):
    def __init__(self):
        WheeledVehicle.__init__(self)
        self.engine = Engine()
    
    def can_ride(self):
        return self.do_all_wheels_work() and self.engine.works()

car = Car()
print(car.can_ride())

car.engine.needs_oil = False
print(car.can_ride())

car.wheels.append(Wheel())
print(car.can_ride())

class Ruler():
    def __init__(self, length):
        self.length = length

ruler = Ruler(5)
print(ruler)
# print(len(ruler))
del ruler

class MagicRuler(Ruler):
    def __init__(self, length):
        Ruler.__init__(self, length)

    def __str__(self):
        return "|....;...." * self.length + "|"
    
    def __len__(self):
        return self.length
    
    def __del__(self):
        print("You've broken such a lovely ruler.")

ruler = MagicRuler(5)
print(ruler)
print(str(ruler))
print(len(ruler))
print(len(str(ruler)))
del ruler
