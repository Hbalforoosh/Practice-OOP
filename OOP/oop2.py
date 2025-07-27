class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.__speed = speed

    def accelerate(self, amount):
        if amount > 0:
            self.__speed += amount
            return f"Accelerated by {amount}.current speed: {self.__speed}"

    def brake(self, amount):
        if amount > 0:
            self.__speed -= amount
            if self.__speed < 0:
                self.__speed = 0
            return f"Braked by {amount}.current speed: {self.__speed}"

    def get_speed(self):
        return self.__speed


car1 = Car("pride", 100)
print(car1.accelerate(50))
print(car1.brake(20))
print(car1.brake(10))
print(f"finall_speed: {car1.get_speed()}")
