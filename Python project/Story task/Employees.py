from Person import Person
from Car import Car

class Employees(Person):
    def __init__(self, id, car, email, salary, distanceToWork, name, money, mood, healthRate):
        super().__init__(name, money, mood, healthRate)  
        self.id = id
        self.car = car  
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def drive(self, distance):
        if self.car.velocity <= 0:
            return "The car's velocity must be greater than zero."
        
        time = distance / self.car.velocity 
        return f"{self.name} will take {time * 60 } min to drive {distance} km using the {self.car.model} at {self.car.velocity} km/h."

    def work(self, hours):

        self.salary += hours * 20  
        return f"{self.name} has worked for {hours} hours and earned {hours * 20} more. New salary: {self.salary}."

    def refuel(self):
        if self.car.fuel_rate < 100:
            fuel_needed = 100 - self.car.fuel_rate  
            self.car.fuel_rate = 100  
            self.money -= fuel_needed * 0.5  
            return f"{self.name} refueled the car. The car is now at full fuel. Remaining money: {self.money}."
        else:
            return f"{self.name}'s car is already full on fuel."

    def send_mail(self):
        return f"Email sent to {self.email}. Subject: 'Work Update'."
