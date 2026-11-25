# Carbon-Commuter-Footprint-Cost-Split-Matchmaker-

Commuter Carbon Footprint & Cost-Split MatchmakerA Python CLI and visual reporting application built by a team of 5 to group commuters traveling along the same route within a 15-minute departure window, calculate $$\text{CO}_2$$ emissions saved from shared rides, split cab fares fairly, and display visual savings charts.
✨ Key Features Student Registration & CSV Storage (registration.py): Validates student names, routes (source and dest), HH:MM departure times, and positive estimated fares, persisting records to commuters.csv.Route & Time Matching (vikram_matching.py): Groups commuters with matching case-insensitive source and destination routes whose departure times are within 15 minutes of each other.Carbon Footprint Calculation (mahi_carbon.py): Computes individual emissions, shared ride emissions, $$\text{CO}_2$$ saved (in $$\text{kg}$$), and percentage saved using an emission factor of $$0.12\text{ kg CO}_2$$ per vehicle per km.Fare Split Calculation (fare_split.py): Divides total cab fare across group members, calculates per-student savings against the original fare, and warns if shared travel costs more than individual travel.Savings Dashboard (dashboard.py): Uses matplotlib to generate bar charts comparing Individual vs. Shared Ride $$\text{CO}_2$$ Emissions ($$\text{kg}$$) and Money Saved Per Student ($$\text{Rs.}$$).
 
 📂 Project Structure.
├── main.py              # Main entry point orchestrating matching, carbon, fare, and charts
├── registration.py      # Standalone CLI & helpers for registering and loading commuters
├── vikram_matching.py   # Route and ±15-minute departure time grouping logic
├── mahi_carbon.py       # CO2 emission and savings calculation module
├── fare_split.py        # Group cab fare split and savings calculator
├── dashboard.py         # Matplotlib visualizations for carbon and money savings
└── commuters.csv        # Auto-generated CSV file storing registered commuter records

🚀 Prerequisites & InstallationPython: Python 3.xDependency: matplotlib (all other imports—csv, os, datetime—are part of the Python standard library)Clone the repository:git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
Install matplotlib:pip install matplotlib
💻 UsageStep 1: Register CommutersRun registration.py to add students and save entries to commuters.csv:python registration.py
Use the menu (1 to register a student, 2 to view registered students, 3 to exit).Step 2: Run the Matchmaker & View ReportsRun main.py to group matched commuters, enter shared vehicle count, trip distance ($$\text{km}$$), and cab fares ($$\text{Rs.}$$), and open the savings dashboard:python main.py
🧮 Calculation FormulasCarbon Emissions:$$$$\text{Individual Emissions} = \text{Students} \times \text{Distance} \times 0.12\text{ kg CO}_2$$$$$$$$\text{Shared Emissions} = \text{Vehicles} \times \text{Distance} \times 0.12\text{ kg CO}_2$$$$Fare Split:$$$$\text{Fare Per Student} = \frac{\text{Total Cab Fare}}{\text{Number of Students}}$$$$$$$$\text{Money Saved} = \text{Original Fare} - \text{Fare Per Student}$$$$👥 Team (5 Members)Module / ResponsibilityFileContributorStudent Registration & CSV Storageregistration.pyTeam Member 1Route & Time Matchmakingvikram_matching.pyVikramCarbon Footprint Calculationmahi_carbon.pyMahiFare Split Calculationfare_split.pyTeam Member 4Dashboard & Main Integrationdashboard.py, main
