class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def buy(self):
        self.money -= 10
        return int(self.money)

    def eat(self, meals):
        if 5 >= meals >= 3:
            self.healthRate = "100%"
        elif meals == 2:
            self.healthRate = "75%"
        elif meals == 1:
            self.healthRate = "50%"
        else:
            return "Invalid input. Please enter a number between 1 and 5."
        return f"{self.name}'s healthRate is {self.healthRate}"

    def sleep(self, sleeper):
        if sleeper == 7:
            self.mood = "happy"
        elif 0 < sleeper < 7:
            self.mood = "tired"
        elif 7 < sleeper <= 24:
            self.mood = "lazy"
        elif sleeper > 24:
            self.mood = "unconscious"
        else:
            return "Invalid sleep duration."
        return f"{self.name} is {self.mood}"
