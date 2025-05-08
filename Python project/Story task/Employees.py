import Person
import Car

class Employees(Person):
    def __init__(self, id, car, email, salary, distanceToWork, name, money, mood, healthRate):
        super().__init__(name, money, mood, healthRate)
        self.id = id
        self.car = car  # An instance of the Car class
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork

    def drive(self, distance):
        if self.car.velocity <= 0:
            return "The car's velocity must be greater than zero."
        
        time = distance / self.car.velocity
        return f"{self.name} will take {time} hours to drive {distance} km using the {self.car.make}  at {self.car.velocity} km/h."



toyota = Car("Toyota", "Corolla", 60)

john = Employees(
    id=101,
    car=toyota,
    email="john.doe@example.com",
    salary=5000,
    distanceToWork=20,
    name="John",
    money=2000,
    mood="Happy",
    healthRate=90,
)



print(john.drive(180))  




"""    def work(self):
        pass

    def refuel(self):
        pass

    def send_mail(self):
        pass
"""