class Car:
    def __init__(self, brand, speed):
        self.__brand = brand   # private attribute
        self.__speed = speed   # private attribute

    def get_brand(self):
        return self.__brand
car = Car("Tesla", 120)
#print(car.__brand)   # ❌ AttributeError
print(car.get_brand())  # ✅ Tesla
print(car._Car__brand)  # 🚨 Works, but not recommended

