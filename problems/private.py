'''#class Car:
    def __init__(self, brand, speed):
        self.__brand = brand   # private attribute
        self.__speed = speed   # private attribute

    def get_brand(self):
        return self.__brand
car = Car("Tesla", 120)
#print(car.__brand)   # ❌ AttributeError
print(car.get_brand())  # ✅ Tesla
print(car._Car__brand)  # 🚨 Works, but not recommended
'''
from abc import ABC, abstractmethod

class Vehicle(ABC):   # Abstract Base Class
    @abstractmethod
    def start(self):
        pass

# ❌ This will fail because Vehicle has an abstract method
# v = Vehicle()   # Uncommenting this line gives TypeError

class Car(Vehicle):
    def start(self):
        return "Car engine starts with a key"

class Bike(Vehicle):
    def start(self):
        return "Bike starts with a kick"

vehicles = [Car(), Bike()]
for v in vehicles:
    print(v.start())
