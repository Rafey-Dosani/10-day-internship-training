import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


# ==============================
# 1. LOAD CLEANED DATASET
# ==============================

input_file = "../data-cleaning/facility_data_cleaned.csv"
output_folder = "../visualizations"

# Create visualization folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

df = pd.read_csv(input_file)

print("==============================")
print("FACILITY DATA VISUALIZATION")
print("==============================")


# ==============================
# 2. BAR CHART
# Average Cleanliness by Location
# ==============================

avg_cleanliness = (
    df.groupby("location")["cleanliness_score"]
    .mean()
    .sort_values()
)

plt.figure(figsize=(8, 5))

avg_cleanliness.plot(kind="bar")

plt.title("Average Cleanliness Score by Location")
plt.xlabel("Location")
plt.ylabel("Average Cleanliness Score")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/avg_cleanliness_by_location.png"
)

plt.close()

print("Chart 1 saved successfully!")


# ==============================
# 3. BAR CHART
# Total Complaints by Location
# ==============================

total_complaints = (
    df.groupby("location")["complaints"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))

total_complaints.plot(kind="bar")

plt.title("Total Complaints by Location")
plt.xlabel("Location")
plt.ylabel("Total Complaints")
plt.xticks(rotation=0)

plt.tight_layout()

plt.savefig(
    f"{output_folder}/complaints_by_location.png"
)

plt.close()

print("Chart 2 saved successfully!")


# ==============================
# 4. HISTOGRAM
# Cleanliness Score Distribution
# ==============================

plt.figure(figsize=(8, 5))

plt.hist(
    df["cleanliness_score"],
    bins=8,
    edgecolor="black"
)

plt.title("Distribution of Cleanliness Scores")
plt.xlabel("Cleanliness Score")
plt.ylabel("Number of Facilities")

plt.tight_layout()

plt.savefig(
    f"{output_folder}/cleanliness_histogram.png"
)

plt.close()

print("Histogram saved successfully!")


# ==============================
# 5. SCATTER PLOT
# Footfall vs Complaints
# ==============================

plt.figure(figsize=(8, 5))

plt.scatter(
    df["footfall"],
    df["complaints"]
)

plt.title("Footfall vs Complaints")
plt.xlabel("Footfall")
plt.ylabel("Number of Complaints")

plt.tight_layout()

plt.savefig(
    f"{output_folder}/footfall_vs_complaints.png"
)

plt.close()

print("Scatter plot saved successfully!")


# ==============================
# 6. CORRELATION HEATMAP
# ==============================

numerical_columns = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "footfall",
    "complaints"
]

correlation = df[numerical_columns].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig(
    f"{output_folder}/correlation_heatmap.png"
)

plt.close()

print("Correlation heatmap saved successfully!")


print("\n==============================")
print("ALL VISUALIZATIONS CREATED!")
print("==============================")