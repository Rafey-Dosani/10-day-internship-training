import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# Load dataset
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

# Encode Yes/No
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

# Models
logistic_model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

random_forest_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train
logistic_model.fit(X_train, y_train)
random_forest_model.fit(X_train, y_train)

# Predictions
logistic_pred = logistic_model.predict(X_test)
random_forest_pred = random_forest_model.predict(X_test)

# Function to evaluate
def evaluate_model(name, y_test, predictions):

    print("\n==============================")
    print(name)
    print("==============================")

    print("Accuracy:",
          accuracy_score(y_test, predictions))

    print("Precision:",
          precision_score(
              y_test,
              predictions,
              average="weighted",
              zero_division=0
          ))

    print("Recall:",
          recall_score(
              y_test,
              predictions,
              average="weighted",
              zero_division=0
          ))

    print("F1 Score:",
          f1_score(
              y_test,
              predictions,
              average="weighted",
              zero_division=0
          ))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))

    print("\nClassification Report:")
    print(
        classification_report(
            y_test,
            predictions,
            target_names=label_encoder.classes_,
            zero_division=0
        )
    )


# Evaluate both models
evaluate_model(
    "Logistic Regression",
    y_test,
    logistic_pred
)

evaluate_model(
    "Random Forest",
    y_test,
    random_forest_pred
)