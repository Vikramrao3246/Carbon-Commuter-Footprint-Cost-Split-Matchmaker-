# Maahi's Carbon Footprint Calculation Module
def calculate_carbon_savings(students, vehicles, distance):

    emission = 0.12  # CO2 emission per vehicle per km

    if students <= 0 or vehicles <= 0 or distance <= 0:
        return "Please enter positive values."

    elif vehicles > students:
        return "Vehicles cannot be more than students."

    else:

        individual = students * distance * emission

        shared = vehicles * distance * emission

        saved = individual - shared

        saving_percentage = (saved / individual) * 100

        return {
            "students": students,
            "vehicles": vehicles,
            "distance": distance,
            "individual_emission": round(individual, 2),
            "shared_emission": round(shared, 2),
            "carbon_saved": round(saved, 2),
            "saving_percentage": round(saving_percentage, 2)
        }
