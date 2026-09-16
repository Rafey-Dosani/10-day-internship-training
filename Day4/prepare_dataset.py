import pandas as pd

# Load cleaned dataset
df = pd.read_csv("dataset/facility_data_cleaned.csv")

# Convert inspection date
df["inspection_date"] = pd.to_datetime(df["inspection_date"])

# Create a hygiene risk score
df["risk_score"] = (
    (10 - df["cleanliness_score"]) +
    df["odor_score"] +
    df["waste_level"] +
    (df["complaints"] / 5)
)

# Add risk based on water availability
df["risk_score"] += df["water_availability"].map({
    "Yes": 0,
    "No": 3
})

# Create risk category
def classify_risk(score):
    if score < 10:
        return "LOW"
    elif score < 16:
        return "MEDIUM"
    else:
        return "HIGH"

df["hygiene_risk"] = df["risk_score"].apply(classify_risk)

# Display result
print(df[[
    "facility_id",
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "complaints",
    "water_availability",
    "risk_score",
    "hygiene_risk"
]])

# Show category distribution
print("\nRisk Distribution:")
print(df["hygiene_risk"].value_counts())

# Save prepared dataset
df.to_csv("dataset/facility_data_prepared.csv", index=False)

print("\nPrepared dataset saved successfully!")