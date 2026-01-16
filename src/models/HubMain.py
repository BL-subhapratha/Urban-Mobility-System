from .Hub import Hub

#UC6: Multiple hubs
def createHubs(hubs):
    
    hub_name = input("\nEnter Hub name: ")

    if hub_name in hubs:
        print("Hub already exists!")
        return

    hub = Hub(hub_name)
    hub.addVehicles()
    hubs[hub_name] = hub

    return hubs

def addVehiclesToExistingHub(hubs):
    hub_name = input("\nEnter existing Hub name: ")

    hub = hubs.get(hub_name)
    if not hub:
        print("Hub not found!")
        return
    hub.addVehicles()

    return hubs

def displayHubs(hubs):

    for hub_name, hub in hubs.items():
        print(f"\nHub name - {hub_name}")
        print("-" * 40)

        for vehicle in hub.vehicles:
            print(vehicle)
            print()