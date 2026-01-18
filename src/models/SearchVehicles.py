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

    #UC10: count of vehicles by status
    def count_by_status(self):
        for hub in self.hubs.values():
            available_vehicles = [v for v in hub.vehicles if v.maintenance_status == 'Available']
            onTrip_vehicles = [v for v in hub.vehicles if v.maintenance_status == 'On Trip']
            underMaintenance_vehicles = [v for v in hub.vehicles if v.maintenance_status == 'Under Maintenance']

        print(f"Count of Available vehicles: {len(available_vehicles)}")
        print(f"Count of On Trip vehicles: {len(onTrip_vehicles)}")
        print(f"Count of Under Maintenance vehicles: {len(underMaintenance_vehicles)}")
