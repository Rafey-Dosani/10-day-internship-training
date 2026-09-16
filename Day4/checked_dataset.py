import pandas as pd

file_path = "dataset/facility_data_cleaned.csv"

df = pd.read_csv(file_path)

print(df.to_string())