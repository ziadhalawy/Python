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
        
            if 5 >= meals and meals >= 3:
                self.healthRate = "100%"
                return f"{self.name}'s healthRate is {self.healthRate}"        
            elif meals == 2:
                self.healthRate = "75%"
                return f"{self.name}'s healthRate is {self.healthRate}"        
            elif meals ==1 :
                self.healthRate = "50%"
                return f"{self.name}'s healthRate is {self.healthRate}"
            else:
                return "invalid please enter num from 1 to 5"
                  



    def sleep(self, sleeper):
        if sleeper == 7:
            self.mood = "happy"
            return f"{self.name} is happy"
        elif 0 < sleeper < 7:
            self.mood = "tired"
            return f"{self.name} is tired"
        elif 7 < sleeper <= 24:
            self.mood = "lazy"
            return f"{self.name} is lazy"
        elif sleeper > 24:
            self.mood = "unconscious"
            return f"{self.name} is in a coma or dead :)"
        else:
            return "Invalid sleep duration."


ziad = Person("ziad", 1000, "happy", "")


