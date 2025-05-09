class Car:
    def __init__(self, model, velocity, fuel_rate):
        self.model = model
        self.velocity = velocity
        self.fuel_rate = fuel_rate

    def run(self, distance, velocity):
        if self.fuel_rate <= 0:
            print("The car cannot run because it has no fuel.")
            return

        self.velocity = velocity
        print(f"The car's velocity is now {self.velocity} km/h.")

        traveled_distance = 0
        fuel_consumption_rate = 10

        while self.fuel_rate > 0 and traveled_distance < distance:
            step_distance = min(10, distance - traveled_distance)
            fuel_needed = fuel_consumption_rate
            
            if self.fuel_rate >= fuel_needed:
                traveled_distance += step_distance
                self.fuel_rate -= fuel_needed
            else:
                max_distance_with_fuel = (self.fuel_rate / fuel_consumption_rate) * 10
                traveled_distance += max_distance_with_fuel
                self.fuel_rate = 0
                print("The car has run out of fuel!")
                break

        remaining_distance = max(0, distance - traveled_distance)
        self.stop(remaining_distance)

    def stop(self, remaining_distance):
        self.velocity = 0
        if remaining_distance > 0:
            print(f"The car stopped before reaching the destination. Remaining distance: {remaining_distance:.2f} km.")
        else:
            print("The car has reached its destination.")
