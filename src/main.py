from src.models.Vehicle import ElectricCar, ElectricScooter
from src.models.Hub import Hub
from src.models.HubMain import createHubs, displayHubs, addVehiclesToExistingHub
from src.models.SearchVehicles import SearchVehicle

print("\nWelcome to Eco-Ride Urban Mobility System!")

"""
vehicle = ElectricCar(100, "Hyndai", 75, 5)
print("Total trip cost in car is", vehicle.calculate_trip_cost(500))

vehicleScooter = ElectricScooter(101, "TVS", 80, 85)
print("Total trip cost in scooter is", vehicleScooter.calculate_trip_cost(30))
"""
hubs = {}

while True:
    choice = int(input("\nEnter: \n1. Add new hub \n2. Add Vehicles to existing hub \n3. Display hubs \n4. Search vehicles \n5. Categorized View \n6. Exit\n"))

    if choice == 1:
        createHubs(hubs)
    elif choice == 2: 
        addVehiclesToExistingHub(hubs)
    elif choice == 3: 
        displayHubs(hubs)
    elif choice == 4:
        search_vehicle = SearchVehicle(hubs)
        searchchoice = int(input("\nEnter 1 to search by hub location or 2 to search by battery status: "))
        if searchchoice == 1:
            searchHub = input("Enter the hub location to search for: ")
            search_vehicle.search_by_hubLoc(searchHub)
        elif searchchoice == 2:
            search_vehicle.search_by_batteryStatus()
        else:
            print("Invalid choice!")
    elif choice == 5:
        searchView = SearchVehicle(hubs)
        searchView.categorized_view()
    elif choice == 6: 
        break
    else:
        print("Invalid choice!")