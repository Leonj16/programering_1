"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = Model
        self.speed = 0

car1 = Car("Volvo", "V60")
car2 = Car("BMW", "320i")

print(car1.brand)

"""
"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(self.name + " says woof!")

dog1 = Dog("Bosse", 5)
"""

class Bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def show_balance(self):
        print("Owner:, self.owner")
        print("Balance:", self.balance)

account1 = Bankaccount("Anna", 1000)

account1.show_balance()

account1.deposit(500)