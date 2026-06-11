# Inheritance allows a class to inherit attributes and methods from another class


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"


class ElectricVechicle(Vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity

    def get_info(self):
        return f"{super().get_info()} with {self.battery_capacity} kWh battery"


# Notice how we use super().__init__() to call base class constructor with arguments. This is a common pattern when extending classes.
