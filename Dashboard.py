import matplotlib.pyplot as plt


def show_dashboard(carbon_results, fare_results):

    # Carbon Savings Graph
    if carbon_results:

        individual = sum(
            result["individual_emission"]
            for result in carbon_results
        )

        shared = sum(
            result["shared_emission"]
            for result in carbon_results
        )

        plt.figure(figsize=(7, 5))

        plt.bar(
            ["Individual Ride", "Shared Ride"],
            [individual, shared]
        )

        plt.title("Carbon Emission Comparison")
        plt.ylabel("CO2 Emission (kg)")
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()

    # Money Savings Graph
    if fare_results:

        savings = [
            result["money_saved"]
            for result in fare_results
        ]

        plt.figure(figsize=(7, 5))

        plt.bar(
            [f"Group {i+1}" for i in range(len(savings))],
            savings
        )

        plt.title("Money Saved Per Student")
        plt.ylabel("Money Saved (Rs.)")
        plt.grid(axis="y", linestyle="--", alpha=0.5)
        plt.tight_layout()

    plt.show()
