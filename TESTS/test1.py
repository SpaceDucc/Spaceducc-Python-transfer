class Vehicle :
    color = "Black"
    def __init__(self, name, max_speed, mileage) :
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity) :
        return capacity
    
    def fare(self) :
        return self.seating_capacity() * 2

class Bus(Vehicle) :
    def seating_capacity(self, capacity = 50) :
        return super().seating_capacity(capacity = 50)
    
    def fare(self) :
        return super().fare() * 0.9

bus1 = Bus("Happy Bus", 200, 2000)

print("Vehicle name:", bus1.name, "Speed:", bus1.max_speed, "Mileage:", bus1.mileage, "Vehicle color:", bus1.color)

print(bus1.seating_capacity())

print("Total bus fare is:", bus1.fare())