class Car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

class ElectricCar(Car):
    def __init__(self, name, model, year, battery_capacity):
        super().__init__(name, model, year)
        self.battery_capacity = battery_capacity

class GasCar(Car):
    def __init__(self, name, model, year, fuel_efficiency):
        super().__init__(name, model, year)
        self.fuel_efficiency = fuel_efficiency

car_type = input("Enter car type (Electric/Gas): ")
name = input("Enter Name: ")
model = input("Enter model: ")
year = input("Enter year: ")


if car_type == "Electric":
    battery_capacity = int(input("Enter battery capacity(kWh): "))
    car_instance = ElectricCar(name, model, year, battery_capacity)
    print(f"Car Information:\n \t{car_instance.year} {car_instance.name} {car_instance.model}\n \tBattery Capacity:{car_instance.battery_capacity} kWh")
elif car_type == "Gas":
    fuel_efficiency = int(input("Enter fuel efficiency(MPG): "))
    car_instance = GasCar(name, model, year, fuel_efficiency)
    print(f"Car Information:\n \t{car_instance.year} {car_instance.name} {car_instance.model}\n  \tFuel Efficiency:{car_instance.fuel_efficiency} MPG")
else:
    print("Invalid car type.")