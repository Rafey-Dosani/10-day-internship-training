import pandas as pd
import numpy as np
import os


# ==============================
# 1. LOAD DATASET
# ==============================

input_file = "../data-cleaning/facility_data.csv"
output_file = "../data-cleaning/facility_data_cleaned.csv"

df = pd.read_csv(input_file)

print("Dataset loaded successfully!\n")

print("First 5 rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# ==============================
# 2. BASIC DATA INFORMATION
# ==============================

print("\n--- DATASET INFORMATION ---")
print(df.info())

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE ROWS ---")
print("Exact duplicate rows:", df.duplicated().sum())


# ==============================
# 3. REMOVE EXACT DUPLICATES
# ==============================

df = df.drop_duplicates()

print("\nDataset shape after removing duplicates:")
print(df.shape)


# ==============================
# 4. HANDLE MISSING VALUES
# ==============================

# Numerical columns
numerical_columns = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "footfall",
    "complaints"
]

# Fill missing numerical values with median
for column in numerical_columns:
    df[column] = df[column].fillna(df[column].median())


# Fill missing location with "Unknown"
df["location"] = df["location"].fillna("Unknown")


# Fill missing water availability with mode
df["water_availability"] = df["water_availability"].fillna(
    df["water_availability"].mode()[0]
)


# ==============================
# 5. HANDLE INVALID NUMERICAL DATA
# ==============================

# Valid score range: 0 to 10

df.loc[
    (df["cleanliness_score"] < 0) |
    (df["cleanliness_score"] > 10),
    "cleanliness_score"
] = np.nan


df.loc[
    (df["odor_score"] < 0) |
    (df["odor_score"] > 10),
    "odor_score"
] = np.nan


df.loc[
    (df["waste_level"] < 0) |
    (df["waste_level"] > 10),
    "waste_level"
] = np.nan


# Footfall and complaints cannot be negative

df.loc[df["footfall"] < 0, "footfall"] = np.nan

df.loc[df["complaints"] < 0, "complaints"] = np.nan


# Fill invalid values with median
for column in numerical_columns:
    df[column] = df[column].fillna(df[column].median())


# ==============================
# 6. HANDLE INVALID CATEGORICAL DATA
# ==============================

valid_water_values = ["Yes", "No"]

df.loc[
    ~df["water_availability"].isin(valid_water_values),
    "water_availability"
] = np.nan


# Fill invalid/missing values with mode
df["water_availability"] = df["water_availability"].fillna(
    df["water_availability"].mode()[0]
)


# ==============================
# 7. HANDLE INVALID DATES
# ==============================

df["inspection_date"] = pd.to_datetime(
    df["inspection_date"],
    errors="coerce"
)

print("\nInvalid/Missing Dates:")
print(df["inspection_date"].isnull().sum())


# Remove rows with invalid dates
df = df.dropna(subset=["inspection_date"])


# ==============================
# 8. OUTLIER DETECTION USING IQR
# ==============================

outlier_columns = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "footfall",
    "complaints"
]

print("\n--- OUTLIER ANALYSIS ---")

for column in outlier_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print(f"\n{column}")
    print("Lower Bound:", lower_bound)
    print("Upper Bound:", upper_bound)
    print("Number of Outliers:", len(outliers))


# ==============================
# 9. SAVE CLEANED DATASET
# ==============================

os.makedirs("../dataset", exist_ok=True)

df.to_csv(output_file, index=False)

print("\n==============================")
print("DATA CLEANING COMPLETED")
print("==============================")

print("\nFinal Dataset Shape:")
print(df.shape)

print("\nCleaned dataset saved at:")
print(output_file)

print("\nFinal Missing Values:")
print(df.isnull().sum())