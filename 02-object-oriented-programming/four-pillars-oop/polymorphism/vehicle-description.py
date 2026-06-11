# Polymorphism allows objects of different classes to be treated as objects of a common superclass. Python's dynamic typing makes polymorphism particulary flexible.


class vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class electric_vechicle(vehicle):
    def __init__(self, make, model, year, battery_capacity):
        super().__init__(make, model, year)
        self.battery_capacity = battery_capacity


def vehicle_description(vehicle):
    return vehicle.get_info()


car = vehicle_description("Toyota", "Camry", 2022)
ev = electric_vechicle("Tesla", "Model Y", 2023, 75)

print(vehicle_description(car))  # output: 2022 Toyota Camry
print(vehicle_description(ev))  # output 2023 Tesla Model Y with 75 kWh battery

# Note : Both objects respond to the same method call but provide different implementations - that's polymorphism in action.
