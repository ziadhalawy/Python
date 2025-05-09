from Car import Car
from Employees import Employees
from Office import Office
from Person import Person


# Static Ziad Information
ziad_car = Car("Toyota", 120, 100)  # Example car object for Ziad
ziad = Employees(
    id=1,
    car=ziad_car,
    email="ziadHalawy@example.com",  # Static email
    salary=5000,
    distanceToWork=20,
    name="Ziad",  # Static name
    money=3000,
    mood="neutral",
    healthRate="80%"
)

# Creating an office and hiring Ziad (for demonstration purposes)
office = Office("Tech Corp")
office.hire(ziad)


def show_menu():
    print("\n---- Choose an option ----")
    print("1. Drive Ziad to work")
    print("2. Check Ziad's lateness")
    print("3. Deduct salary from Ziad")
    print("4. Reward Ziad")
    print("5. Buy something for Ziad")
    print("6. Ziad's health check")
    print("7. Ziad's sleep status")
    print("8. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            # Drive Ziad
            distance = float(input("Enter the distance Ziad wants to drive (in km): "))
            print(ziad.drive(distance))

        elif choice == "2":
            # Check Ziad's lateness
            move_hour = float(input("Enter the hour Ziad is leaving: "))
            office.check_lateness(emp_id=ziad.id, move_hour=move_hour)

        elif choice == "3":
            # Deduct salary from Ziad
            deduction = float(input("Enter the deduction amount for Ziad: "))
            office.deduct(ziad.id, deduction)

        elif choice == "4":
            # Reward Ziad
            reward = float(input("Enter the reward amount for Ziad: "))
            office.reward(ziad.id, reward)

        elif choice == "5":
            # Buy something for Ziad
            print(ziad.buy())

        elif choice == "6":
            # Ziad's health check
            meals = int(input("How many meals has Ziad eaten (1-5): "))
            print(ziad.eat(meals))

        elif choice == "7":
            # Ziad's sleep status
            sleep_hours = int(input("How many hours did Ziad sleep: "))
            print(ziad.sleep(sleep_hours))

        elif choice == "8":
            # Exit
            print("Exiting the program.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
