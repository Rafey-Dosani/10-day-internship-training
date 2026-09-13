import pandas as pd
import os


# ==============================
# 1. LOAD CLEANED DATASET
# ==============================

input_file = "../data-cleaning/facility_data_cleaned.csv"

df = pd.read_csv(input_file)

print("==============================")
print("FACILITY DATA ANALYSIS")
print("==============================")


# ==============================
# 2. BASIC DATASET INFORMATION
# ==============================

print("\n--- DATASET SHAPE ---")
print(df.shape)

print("\n--- FIRST 5 RECORDS ---")
print(df.head())


# ==============================
# 3. DESCRIPTIVE STATISTICS
# ==============================

print("\n--- DESCRIPTIVE STATISTICS ---")

numerical_columns = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "footfall",
    "complaints"
]

print(df[numerical_columns].describe())


# ==============================
# 4. KEY STATISTICS
# ==============================

print("\n--- KEY STATISTICS ---")

statistics = pd.DataFrame({
    "Mean": df[numerical_columns].mean(),
    "Median": df[numerical_columns].median(),
    "Minimum": df[numerical_columns].min(),
    "Maximum": df[numerical_columns].max(),
    "Standard Deviation": df[numerical_columns].std()
})

print(statistics)


# ==============================
# 5. LOCATION-WISE ANALYSIS
# ==============================

print("\n--- AVERAGE CLEANLINESS BY LOCATION ---")

avg_cleanliness = (
    df.groupby("location")["cleanliness_score"]
    .mean()
    .sort_values()
)

print(avg_cleanliness)


print("\n--- TOTAL COMPLAINTS BY LOCATION ---")

total_complaints = (
    df.groupby("location")["complaints"]
    .sum()
    .sort_values(ascending=False)
)

print(total_complaints)


print("\n--- AVERAGE WASTE LEVEL BY LOCATION ---")

avg_waste = (
    df.groupby("location")["waste_level"]
    .mean()
    .sort_values(ascending=False)
)

print(avg_waste)


# ==============================
# 6. CORRELATION ANALYSIS
# ==============================

print("\n--- CORRELATION MATRIX ---")

correlation = df[numerical_columns].corr()

print(correlation)


# ==============================
# 7. IDENTIFY KEY FINDINGS
# ==============================

print("\n==============================")
print("KEY INSIGHTS")
print("==============================")


# Insight 1
lowest_clean_location = avg_cleanliness.idxmin()
lowest_clean_score = avg_cleanliness.min()

print(
    f"\n1. Lowest average cleanliness:"
    f" {lowest_clean_location}"
    f" ({lowest_clean_score:.2f})"
)


# Insight 2
highest_complaint_location = total_complaints.idxmax()
highest_complaints = total_complaints.max()

print(
    f"\n2. Highest total complaints:"
    f" {highest_complaint_location}"
    f" ({highest_complaints})"
)


# Insight 3
highest_waste_location = avg_waste.idxmax()
highest_waste = avg_waste.max()

print(
    f"\n3. Highest average waste level:"
    f" {highest_waste_location}"
    f" ({highest_waste:.2f})"
)


# Insight 4
footfall_complaints_corr = correlation.loc[
    "footfall",
    "complaints"
]

print(
    f"\n4. Footfall vs Complaints correlation:"
    f" {footfall_complaints_corr:.2f}"
)


print("\nAnalysis completed successfully!")