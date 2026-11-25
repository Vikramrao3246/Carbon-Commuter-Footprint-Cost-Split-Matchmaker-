# Commuter Carbon Footprint & Cost-Split Matchmaker

A Python project built for our Computational Thinking and Programming course (2026CSAE100) at Bennett University.

Many day-scholar students commuting to Bennett University from nearby areas like Pari Chowk, Depot, Delta 1, Knowledge Park, and Alpha 1 book separate cabs even when they travel the same route around the same time. This project matches students on the same route within a 15-minute window, splits cab fares fairly, estimates CO2 saved, and shows bar charts using Matplotlib.

## Files & Features
- registration.py: Creates commuters.csv if missing, checks student inputs (name, source, destination, HH:MM time, and fare), and lets users register or view commuters
- vikram_matching.py: Groups students with matching source and destination (ignoring case and extra spaces) whose departure times are within 15 minutes of each other
- mahi_carbon.py: Checks vehicle count and distance, then calculates individual and shared CO2 emissions (at 0.12 kg per vehicle per km), CO2 saved, and saving percentage
- fare_split.py: Splits total cab fare equally among group members, calculates money saved per student, and warns if sharing costs more than traveling solo
- dashboard.py: Plots two Matplotlib bar charts comparing individual vs. shared CO2 emissions and money saved per student
- main.py: Connects all modules into one console flow with try-except handling and printed reports
- commuters.csv: Stores saved commuter records

## Setup & Run
Install matplotlib first (csv, os, and datetime come built-in with Python):
pip install matplotlib

Step 1: Register commuters
python registration.py

Step 2: Run the matchmaker after matching
For each matched group, enter:
- number of shared vehicles and distance in km (for CO2 savings)
- total cab fare and original fare per student (for fare splitting)
Then view the printed reports and Matplotlib charts:
python main.py

## Team (Batch 71)
- Vikram Yadav (S26CSEU2534): Main integration and route/time matching
- Krish Jha (S26CSEU2525): Registration, input validation, and CSV storage
- Anushka Chaurasia (S26CSEU2510): Fare splitting and savings output
- Maahi Bansal (S26CSEU2540): Carbon footprint and savings calculation
- Harsh Pandey (S26CSEU2538): Matplotlib dashboard charts
