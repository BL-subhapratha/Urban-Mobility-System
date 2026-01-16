from src.models.Vehicle import ElectricCar, ElectricScooter
from src.models.Hub import Hub
from src.models.HubMain import createHubs, displayHubs, addVehiclesToExistingHub

print("\nWelcome to Eco-Ride Urban Mobility System!")

"""
vehicle = ElectricCar(100, "Hyndai", 75, 5)
print("Total trip cost in car is", vehicle.calculate_trip_cost(500))

vehicleScooter = ElectricScooter(101, "TVS", 80, 85)
print("Total trip cost in scooter is", vehicleScooter.calculate_trip_cost(30))
"""
hubs = {}

while True:
    choice = int(input("\nEnter: \n1. Add new hub \n2. Add Vehicles to existing hub \n3. Display hubs \n4. Exit\n"))

    match choice:
        case 1: createHubs(hubs)
        case 2: addVehiclesToExistingHub(hubs)
        case 3: displayHubs(hubs)
        case 4: break