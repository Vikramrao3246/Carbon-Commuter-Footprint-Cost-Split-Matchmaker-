
import csv
import os
from datetime import datetime

FILE_NAME = "commuters.csv"


# Create CSV file if it does not exist
def create_file():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "name",
                "source",
                "dest",
                "time",
                "fare"
            ])


# Validate departure time
def validate_time(time_str):

    try:
        datetime.strptime(time_str, "%H:%M")
        return True

    except ValueError:
        return False


# Register a new commuter
def register_commuter():

    print("\n===== STUDENT REGISTRATION =====")

    while True:
        name = input("Enter student name: ").strip()

        if name and any(ch.isalpha() for ch in name):
            break

        print("Invalid name. Please enter a valid name.")

    while True:
        source = input("Enter your source: ").strip()

        if source:
            break

        print("Source cannot be empty.")

    while True:
        dest = input("Enter your destination: ").strip()

        if dest:
            break

        print("Destination cannot be empty.")

    while True:
        time_str = input("Enter departure time (HH:MM): ").strip()

        if validate_time(time_str):
            break

        print("Invalid time! Example: 08:30")

    while True:
        try:
            fare = float(input("Enter estimated fare: "))

            if fare > 0:
                break

            print("Fare must be greater than zero.")

        except ValueError:
            print("Please enter a valid number.")

    commuter = {
        "name": name,
        "source": source,
        "dest": dest,
        "time": time_str,
        "fare": fare
    }

    create_file()

    with open(FILE_NAME, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            name,
            source,
            dest,
            time_str,
            fare
        ])

    print("\nRegistration successful!")
    print("Student:", name)

    return commuter


# Load all registered commuters
def load_commuters():

    create_file()

    commuters = []

    with open(FILE_NAME, "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:
            row["fare"] = float(row["fare"])
            commuters.append(row)

    return commuters


# Display registered students
def display_commuters():

    commuters = load_commuters()

    print("\n===== REGISTERED STUDENTS =====")

    if not commuters:
        print("No students registered yet.")

    else:
        for i, student in enumerate(commuters, 1):

            print(f"\nStudent {i}")
            print("Name:", student["name"])
            print("Source:", student["source"])
            print("Destination:", student["dest"])
            print("Time:", student["time"])
            print("Fare:", student["fare"])

    return commuters


# Test registration module
if __name__ == "__main__":

    create_file()

    while True:

        print("\n===== REGISTRATION MENU =====")
        print("1. Register Student")
        print("2. View Registered Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_commuter()

        elif choice == "2":
            display_commuters()

        elif choice == "3":
            print("Registration module closed.")
            break

        else:
            print("Invalid choice! Try again.")
