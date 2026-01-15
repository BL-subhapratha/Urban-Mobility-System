from abc import ABC, abstractmethod

#UC1: define vehicle class and initialize attributes
class Vehicle(ABC):
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = battery_percentage
        #UC2: private attribute
        self.__maintenance_status = ''

    #UC2: getters and setters
    @property
    def get_maintenance_status(self):
        return self.__maintenance_status
    
    @property
    def battery_percentage(self):
        return self._battery_percentage
    
    @battery_percentage.setter
    def battery_percentage(self, value):
        if not (0 <= value <= 100):
            print("Battery percentage must be between 0 and 100.")
        self._battery_percentage = value

    #UC4: Abstraction
    @abstractmethod
    def calculate_trip_cost(self, distance):
        return distance

#UC3: Inheritance
class ElectricCar (Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    #UC5: Polymorphism
    def calculate_trip_cost(self, distance):
        return f"$"+ str(5.00 + (0.50 * distance))
    
    
class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    #UC5: Polymorphism
    def calculate_trip_cost(self, time):
        return f"$"+ str(1.00 + (0.15 * time))