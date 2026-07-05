# intances the both s1 and s2 have different address
class student:
    pass
s1=student()
s2=student()
print(s1)
print(s2)
class car:
    def __init__(self,colour,speed):
        self.colour= colour
        self.speed=speed
    def horn(self):
        print("beep")
car1=car ("red",200)
print(car1.colour,"\n",car1.speed)
car1.horn()  
#contructer
class Robot:
    def __init__(self, name):     # constructor
        self.name = name
        print(f"{name} has been built!")

r = Robot("Bolt")  
# inharitance
class car:
    def __init__(self,colour,speed):
        self.colour= colour
        self.speed=speed
class super_car(car):
    def turbo(self):
        print("high speed")
car=super_car("red",300)
print(car.speed)
car.turbo()
#Polymorphism
class Dog:
    def make_sound(self):
        print("Woof!")

class Cat:
    def make_sound(self):
        print("Meow!")

for animal in [Dog(), Cat()]:
    animal.make_sound()   # same method name, different behavior
#encapsulation
class Robot:
    def __init__(self):
        self.battery = 100      

    def charge(self):
        self.battery = 100
        print("Charged!")

    def get_battery(self):
        return self.battery

r = Robot()
print(r.get_battery())   
# print(r.__battery)  won't work directly — protected
#method overriding
class Robot:
    def move(self):
        print("Generic moving")

class DroneRobot(Robot):
    def move(self):                 # overriding parent's move()
        print("Flying through the air")

d = DroneRobot()
d.move()   # "Flying through the air" — NOT the parent's version
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass    # every shape MUST define how to calculate its own area

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2