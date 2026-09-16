import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("dataset/facility_data_prepared.csv")

# Features
features = [
    "cleanliness_score",
    "odor_score",
    "waste_level",
    "water_availability",
    "footfall",
    "complaints"
]

X = df[features].copy()
y = df["hygiene_risk"]

# Encode water availability
X["water_availability"] = X["water_availability"].map({
    "Yes": 1,
    "No": 0
})

# Encode target
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Train model using complete dataset
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# -----------------------------
# New facility input
# -----------------------------

print("Enter facility details:\n")

cleanliness = float(input("Cleanliness score (0-10): "))
odor = float(input("Odor score (0-10): "))
waste = float(input("Waste level (0-10): "))
water = input("Water available? (Yes/No): ")
footfall = float(input("Footfall: "))
complaints = float(input("Number of complaints: "))

water_value = 1 if water.lower() == "yes" else 0

new_facility = pd.DataFrame([{
    "cleanliness_score": cleanliness,
    "odor_score": odor,
    "waste_level": waste,
    "water_availability": water_value,
    "footfall": footfall,
    "complaints": complaints
}])

# Prediction
prediction = model.predict(new_facility)

risk = label_encoder.inverse_transform(prediction)[0]

print("\n==============================")
print("Predicted Hygiene Risk:", risk)
print("==============================")