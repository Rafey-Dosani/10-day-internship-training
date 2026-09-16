# Day 4 - Facility Hygiene Risk Prediction

## Objective

Predict facility hygiene risk as **LOW, MEDIUM, or HIGH** using machine learning.

## Dataset

* 48 facility records
* Cleaned dataset from Day 3
* Features: cleanliness score, odor score, waste level, water availability, footfall, and complaints

## Workflow

1. Data preprocessing
2. Risk category creation
3. Train-test split
4. Model training
5. Model evaluation
6. New facility risk prediction

## Models Used

* Logistic Regression
* Random Forest

## Evaluation

Models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

Additional Random Forest feature-importance analysis was performed.

## Technologies

Python, Pandas, Scikit-learn, Matplotlib

## Limitations

The dataset contains only 48 records, and the hygiene-risk labels were generated using predefined rules rather than real expert-labelled data.
