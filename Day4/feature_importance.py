import pandas as pd
import matplotlib.pyplot as plt

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

# Train Random Forest
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Feature importance
importance = pd.Series(
    model.feature_importances_,
    index=features
).sort_values(ascending=False)

print("Feature Importance:")
print(importance)

# Plot
importance.plot(kind="bar")

plt.title("Random Forest Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.tight_layout()

plt.savefig("feature_importance.png")

plt.show()

print("\nFeature importance saved as feature_importance.png")