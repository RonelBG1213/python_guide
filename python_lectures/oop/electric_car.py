from car import Car

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)  # Call the parent constructor
        self.battery_capacity = battery_capacity

    def start_engine(self):
        print(f"The {self.brand} {self.model} silently powers on with a {self.battery_capacity} kWh battery")

    def charge_battery(self):
        print(f"Charging the {self.brand} {self.model}'s battery...")
