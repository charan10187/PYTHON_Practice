'''class Employee:
    company = "ABC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self, amount):
        self.salary += amount

emp1 = Employee("Ravi", 30000)
emp1.increase_salary(5000)

print(emp1.salary)

# 35000

'''

'''
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()

# Animal speak

'''

'''class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()

# Dog bark
'''
'''
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

d = Dog()
d.speak()

# Animal speaks
# Dog barks

'''
'''
class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()

# Bark
# Meow
'''

'''
class BankAccount:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("deposite completed")
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print('withdraw completed')
        else:
            print('In Sufficent Funds')
    def display_balance(self):
        print(self.balance)
account = BankAccount("Charan", 10000)

account.deposit(2000)
account.withdraw(3000)

account.display_balance()

'''
''' conversion to list comprehension 
numbers = [10, 15, 20, 25, 30, 35]

result = []

for num in numbers:
    if num > 20:
        result.append(num)

print(result)

# print([num for num in numbers if num>20 ])

'''
'''
numbers = [1, 2, 3, 4, 5, 6]

result = [num * 2 for num in numbers if num % 2 == 0]

print(result)
'''


'''
numbers = [1, 2, 3, 4]

result = {num: num * num for num in numbers}

print(result)

'''
'''
numbers = [2, 4, 6, 8]

result = list(map(lambda x: x ** 2 + 1, numbers))

print(result)

'''
'''
numbers = [1, 2, 3, 4, 5, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

'''

'''

| Function   | Purpose                              |
| ---------- | ------------------------------------ |
|  map()     | Transform every element              |
|  filter()  | Keep elements satisfying a condition |

'''
