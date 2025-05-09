# Office class (add this method)
class Office:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)
    
    def fire(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.id != emp_id]

    def get_all_employees(self):
        return self.employees

    def check_lateness(self, emp_id, move_hour):
        # Assume office starts at 9 AM
        if move_hour > 9:
            print(f"Employee {emp_id} is late. Salary deduction applies.")
            # You can add logic here to deduct salary or whatever behavior you need
        else:
            print(f"Employee {emp_id} is on time.")
    
    def reward(self, emp_id, reward_amount):
        for emp in self.employees:
            if emp.id == emp_id:
                emp.salary += reward_amount
                print(f"Employee {emp.name} has received a reward of {reward_amount}. New salary: {emp.salary}")
                break

    def deduct(self, emp_id, deduction_amount):
        for emp in self.employees:
            if emp.id == emp_id:
                emp.salary -= deduction_amount
                print(f"Employee {emp.name} has been deducted {deduction_amount}. New salary: {emp.salary}")
                break
