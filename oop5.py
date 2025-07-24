class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, new_value):
        if isinstance(new_value, (int, float)):
            self.__celsius = new_value
            print("seccessful")
        else:
            print("Error setter")

    @property
    def farenhit(self):
        return (self.__celsius * 9 / 5) + 32


temp1 = Temperature(100)
print(f"Current Celsius: {temp1.celsius}")
print(f"Current Farenhit: {temp1.farenhit}")

temp1.celsius = 30
print(f"Update Celsius: {temp1.celsius}")
print(f"Update Farenhit: {temp1.farenhit}")

temp1.celsius = "cool"
