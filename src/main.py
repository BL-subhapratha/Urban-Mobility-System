from src.models.Vehicle import ElectricCar, ElectricScooter

print("Welcome to Eco-Ride Urban Mobility System!")

vehicle = ElectricCar(100, "Hyndai", 75, 5)
print("Total trip cost in car is", vehicle.calculate_trip_cost(500))

vehicleScooter = ElectricScooter(101, "TVS", 80, 85)
print("Total trip cost in scooter is", vehicleScooter.calculate_trip_cost(30))