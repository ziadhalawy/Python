class Car:
    def __init__(self, model, velocity, fuelRate):
        
        self.model = model
        self.velocity = velocity  
        self.fuelRate = fuelRate  

    def run(self, distance, velocity):
        if self.fuelRate <= 0:
            print("The car cannot run because it has no fuel.")
            return
        
        self.velocity = velocity  
        print(f"The car's velocity is now {self.velocity} km/h.")

        
        traveled_distance = 0
        fuel_consumption_per_km = 10 / 10  

        while self.fuelRate > 0 and traveled_distance < distance:

            step_distance = min(10, distance - traveled_distance)  
            fuel_needed = fuel_consumption_per_km * step_distance

            if self.fuelRate - fuel_needed >= 0:
                traveled_distance += step_distance
                self.fuelRate -= fuel_needed
            else:

                traveled_distance += self.fuelRate / fuel_consumption_per_km
                self.fuelRate = 0  
                print("The car has run out of fuel!")
                break


        remaining_distance = max(0, distance - traveled_distance)
        self.stop(remaining_distance)

    def stop(self, remaining_distance):
        if remaining_distance > 0:
            print(f"The car stopped before reaching the destination. Remaining distance: {remaining_distance:.2f} km.")
        else:
            print("The car has reached its destination.")



fiat = Car("Fiat 128", 0, 100)
fiat.run(100, 50)
