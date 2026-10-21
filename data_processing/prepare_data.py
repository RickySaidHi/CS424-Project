# Cleans our study space data and makes the files our visualizations use.
# python prepare_data.py

import matplotlib.pyplot as plt
import pandas as pd

# Load our data
data = pd.read_csv("../Updated_Dataset.csv")
locations = pd.read_csv("locations.csv")
fixes = pd.read_csv("fixes.csv")

# Blank out the values we know are wrong
for visit, column in zip(fixes["visit_id"], fixes["column"]):
    data.loc[data["visit_id"] == visit, column] = None

# Recalculate these instead of trusting the spreadsheet formulas
data["available_chairs"] = data["total_chairs"] - data["occupied_chairs"]
data["available_tables"] = data["total_tables"] - data["occupied_tables"]
data["chair_occupancy_pct"] = data["occupied_chairs"] / data["total_chairs"] * 100
data["table_occupancy_pct"] = data["occupied_tables"] / data["total_tables"] * 100
data = data.drop(columns=["chair_occupancy_rate", "table_occupancy_rate"])

# Print any visits that are wrong
problems = data[data["occupied_tables"] > data["occupied_chairs"]]
print("Visits with more occupied tables than chairs:", list(problems["visit_id"]))

# Add new columns
data = data.merge(locations, on="location")
data["session_id"] = data["date"] + " " + data["time_of_day"]
data["table_chair_gap"] = data["table_occupancy_pct"] - data["chair_occupancy_pct"]
data["people_per_table"] = data["occupied_chairs"] / data["occupied_tables"]
data["has_open_table"] = (data["available_tables"] > 0).astype(float)
data.loc[data["available_tables"].isna(), "has_open_table"] = None
data.round(2).to_csv("../processed_data/observations_clean.csv", index=False)

# Q1: average occupancy for each lounge at each time of day
q1 = data.groupby(["location_label", "time_of_day"])[["chair_occupancy_pct", "table_occupancy_pct"]].mean()
q1.round(2).to_csv("../processed_data/q1_by_time_of_day.csv")

# Q2: the same lounge, day and time of day, on a rainy day vs a sunny day
q2 = data.pivot_table(index=["location_label", "day", "time_of_day"], columns="weather",
    values="chair_occupancy_pct")[["Rain", "Sunny"]].dropna()
q2.round(2).to_csv("../processed_data/q2_rain_vs_sun.csv")

# Q4 and our new question: open seats, open tables and people per table for each lounge
q4 = data.groupby("location_label")[["chair_occupancy_pct", "table_occupancy_pct", "available_chairs",
    "has_open_table", "people_per_table"]].mean()
q4.round(2).sort_values("chair_occupancy_pct").to_csv("../processed_data/q4_by_location.csv")

# How many visits we have for each day and time of day
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
times = ["Morning", "Midday", "Afternoon"]
coverage = pd.crosstab(data["day"], data["time_of_day"]).reindex(index=days, columns=times, fill_value=0)
coverage.to_csv("../processed_data/coverage.csv")

# Chart of the visit counts
plt.imshow(coverage > 0, cmap="Blues", aspect="auto")
for row in range(len(days)):
    for col in range(len(times)):
        count = coverage.iloc[row, col]
        plt.text(col, row, count, ha="center", va="center", color="white" if count > 0 else "black")
plt.xticks(range(len(times)), times)
plt.yticks(range(len(days)), days)
plt.title("Number of visits")
plt.tight_layout()
plt.savefig("../visualizations/coverage_grid.png", dpi=160)

print("Saved", len(data), "visits to processed_data and the chart to visualizations")