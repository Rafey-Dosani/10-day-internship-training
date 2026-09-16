import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

# Load prepared dataset
df = pd.read_csv("dataset/facility_data_prepared.csv")

# Select features
X = df[
    [
        "cleanliness_score",
        "odor_score",
        "waste_level",
        "water_availability",
        "footfall",
        "complaints"
    ]
].copy()

# Target
y = df["hygiene_risk"]

# Convert Yes/No to numbers
X["water_availability"] = X["water_availability"].map({
    "Yes": 1,
    "No": 0
})

# Encode target
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -----------------------------
# Logistic Regression
# -----------------------------

logistic_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

logistic_model.fit(X_train, y_train)

# -----------------------------
# Random Forest
# -----------------------------

random_forest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

random_forest_model.fit(X_train, y_train)

# -----------------------------
# Results
# -----------------------------

print("Models trained successfully!")

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

print("\nClasses:")
print(label_encoder.classes_)