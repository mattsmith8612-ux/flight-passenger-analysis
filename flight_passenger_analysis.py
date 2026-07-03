"""
Flight Passenger Analysis

This project explores airline passenger data using pandas and matplotlib.
The analysis investigates:
- passenger trends over time,
- average passenger numbers by year,
- average passenger numbers by month,
- basic time-series patterns.
"""

import pandas as pd
from matplotlib import pyplot as plt


# Load the flights dataset from a CSV file
file = "flights.csv"
data = pd.read_csv(file)


# Create a datetime column by combining the year and month columns
data["datetime"] = pd.to_datetime(
    data["year"].astype(str) + "-" + data["month"].astype(str)
)


# Display the first few rows and basic information about the dataset
print(data.head())
data.info()


# Plot passenger numbers over time
plt.figure()
plt.plot(data["datetime"], data["passengers"])
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.title("Flight Passengers Over Time")
plt.savefig("flight_passengers_over_time.png")
plt.show()


# Calculate the average number of passengers per year
yearly_average = data.groupby("year")["passengers"].mean().reset_index()


# Plot the yearly average number of passengers
plt.figure()
plt.plot(yearly_average["year"], yearly_average["passengers"])
plt.xlabel("Year")
plt.ylabel("Average Passengers")
plt.title("Average Passengers per Year")
plt.savefig("average_passengers_per_year.png")
plt.show()


# Extract the month number from the datetime column
data["month_number"] = data["datetime"].dt.month


# Calculate the average number of passengers for each month
monthly_average = data.groupby("month_number")["passengers"].mean().reset_index()


# Plot the average number of passengers for each month
plt.figure()
plt.bar(monthly_average["month_number"], monthly_average["passengers"])
plt.xlabel("Month")
plt.xticks(
    monthly_average["month_number"],
    [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ],
)
plt.ylabel("Average Passengers")
plt.title("Average Passengers per Month")
plt.savefig("average_passengers_per_month.png")
plt.show()
