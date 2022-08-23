#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle(): # super class
    def __init__(self, bodysytle):
        self.bodystyle = bodysytle

    def drive(self,speed):
        self.mode ="driving"
        self.speed = speed




class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self,speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, has_SideDoor):
        super().__init__("Motorcycle")
        if(has_SideDoor):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self,speed):
        super().drive(speed)
        print("Driving at" , self.enginetype, " motorcyle at", self.speed)

car1 = Car("gas") # engine type
car2 = Car("electric")
mc1 = Motorcycle("gas", True)
mc2 = Motorcycle("electric", False)






print(mc1.wheels)
print(mc2.wheels)
print(car1.enginetype)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(50)
