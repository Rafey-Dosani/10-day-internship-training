import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load prepared dataset
df = pd.read_csv("dataset/facility_data_prepared.csv")

# Features
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

# Convert Yes/No to numerical values
X["water_availability"] = X["water_availability"].map({
    "Yes": 1,
    "No": 0
})

# Encode target:
# HIGH = 0, LOW = 1, MEDIUM = 2
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

print("\nFeatures:")
print(X.columns.tolist())

print("\nTarget classes:")
print(label_encoder.classes_)

print("\nPreprocessing completed successfully.")