class Animal:
    def eat(self):
        print("Eating food")

class Dog(Animal):
    def speak(self):
        print("Bark!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

pets = [Dog(), Cat()]

for pet in pets:
    pet.eat()   # Both can eat (inherited from Animal)
    pet.speak() # Each speaks differently
