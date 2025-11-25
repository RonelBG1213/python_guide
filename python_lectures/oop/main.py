import car
from electric_car import ElectricCar
from car_private import Car_private

my_car = car.Car("Toyota", "Corolla")

my_car.start_engine()
my_car.stop_engine()

my_electric_car = ElectricCar("Tesla", "Model S", 100)
my_electric_car.start_engine()
my_electric_car.charge_battery()



car = Car_private("Toyota", "Corolla")
print(car.get_model())

car.set_model("Camry")
print(car.get_model())
