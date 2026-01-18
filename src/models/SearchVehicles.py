#UC8: Search vehicles by hub location or battery status
from .Vehicle import ElectricCar, ElectricScooter

class SearchVehicle:
    def __init__(self, hubs):
        self.hubs = hubs

    def search_by_hubLoc(self, location):
        hubfound = False
        
        for hub_name, hub in self.hubs.items():
            for vehicle in hub.vehicles:
                if hub_name.lower() == location.lower():
                    hubfound = True
                    print(vehicle)
        if not hubfound:
            print("No veicles found in the hub!")
                
    def search_by_batteryStatus(self):
        for hub in self.hubs.values():
            battery_vehicles = filter(lambda v: v.battery_percentage > 80, hub.vehicles)
            for vehicle in battery_vehicles:
                print(vehicle)

    #UC9: Categorized View
    def categorized_view(self):
        for hub_name, hub in self.hubs.items():
            cars = filter(lambda v: isinstance(v, ElectricCar), hub.vehicles)
            scooters = filter(lambda v: isinstance(v, ElectricScooter), hub.vehicles)
        
            print(f"\nHub: {hub_name}")
            print("Cars:")
            for c in cars:
                print(c)

            print("Scooters:")
            for s in scooters:
                print(s)
