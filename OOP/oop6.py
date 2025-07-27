from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} | {self.model} car started")

    def stop(self):
        print(f"{self.brand} | {self.model} car stoped")


class Motorcycle(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} | {self.model} Motorcycle started")

    def stop(self):
        print(f"{self.brand} | {self.model} Motorcycle stoped")


car1 = Car("saipa", "pride")
mot1 = Motorcycle("taktaz", "125")
vehicles = [car1, mot1]

for vehicle in vehicles:
    vehicle.start()
    vehicle.stop()
