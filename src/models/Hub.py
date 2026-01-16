from .Vehicle import ElectricCar, ElectricScooter

#UC6: Multiple Hubs
class Hub:
    def __init__(self, name):
        self.name = name
        self.vehicles = []

    def addVehicles(self):
        numVehicles = int(input(f"\nEnter number of vehicles to add to hub {self.name}: "))

        for i in range(numVehicles):
            vehiclechoice = int(input("\nEnter 1 for electric car and 2 for electric scooter: "))

            print(f"\nEnter the vehicle details for {i+1}:")
            newvehicleid = int(input(f"{i+1} Vehicle id: "))
            newmodel = input(f"{i+1} Vehicle model: ")
            newbatteryper = int(input(f"{i+1} Battery percentage: "))

            if(vehiclechoice == 1):
                newseating = int(input(f"{i+1} Seating Capacity: "))
                newElectricCar = ElectricCar(newvehicleid, newmodel, newbatteryper, newseating)
                self.vehicles.append(newElectricCar)
            elif vehiclechoice == 2:
                newspeedlimit = int(input(f"{i+1} Max Speed Limit: "))
                newElectricScooter = ElectricScooter(newvehicleid, newmodel, newbatteryper, newspeedlimit)
                self.vehicles.append(newElectricScooter)
            else:
                print("Invalid choice!")

        return self.vehicles
            