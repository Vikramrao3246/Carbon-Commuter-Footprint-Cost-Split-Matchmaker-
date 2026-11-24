
def calculate_fare(total_fare, students, original_fare):

    if total_fare <= 0:
        print("Total fare should be more than 0.")
        return None

    if students <= 0:
        print("Students should be more than 0.")
        return None

    if original_fare < 0:
        print("Original fare cannot be negative.")
        return None

    fare_per_student = total_fare / students
    money_saved = original_fare - fare_per_student

    print("\n--- Fare Split Report ---")
    print(f"Number of students: {students}")
    print(f"Total cab fare: Rs. {total_fare:.2f}")
    print(f"Fare per student: Rs. {fare_per_student:.2f}")
    print(f"Original fare per student: Rs. {original_fare:.2f}")
    print(f"Money saved per student: Rs. {money_saved:.2f}")
    if money_saved < 0:
        print("Warning: Shared ride is more expensive than individual travel.")
    elif money_saved == 0:
        print("No money saved.")
    return {
        "money_saved": round(money_saved, 2),
        "fare_per_student": round(fare_per_student, 2)
    }
